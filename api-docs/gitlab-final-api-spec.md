# GitLab 연동 최종 API 명세

SSAGY가 lab.ssafy.com(GitLab CE, self-hosted)에 호출하는 API의 최종 목록.
각 API 상단에 **참조 문서**(이 저장소 `api-docs/gitlab_rest_defuddle_markdown/` 내 카테고리·번호)를 명시한다.

## 공통 사항

- **Base URL:** `https://lab.ssafy.com/api/v4`
- **인증 주체 구분:**
  - `[팀장 OAuth]` — 최초 연동 시 팀장의 GitLab OAuth access token으로만 호출 (봇 토큰으로 호출 불가)
  - `[봇 토큰]` — 발급된 Project Access Token. 운영 중 모든 수집·자동화 호출의 기본
- **페이지네이션 공통:** 목록 API는 `page`(기본 1), `per_page`(기본 20, 최대 100) 사용.
  응답 헤더 `X-Next-Page`가 빈 값이 될 때까지 순회한다. **기본 20개 잘림 사고 주의** (members/all 실측에서 확인됨).
- **공통 에러 처리:**

| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `401` | 토큰 만료/폐기 | 봇 토큰 상태 점검 → rotate 실패 이력 확인 → 팀장 재연동 안내 |
| `403` | 권한(access_level) 부족 | 온보딩 시 권한 사전 검증으로 예방. 발생 시 기능 비활성 + 안내 |
| `404` | 리소스 없음 또는 **권한 없음(GitLab은 403 대신 404를 자주 반환)** | 권한 문제 가능성 포함해 진단 |
| `429` | Rate limit | `Retry-After` 헤더만큼 대기 후 재시도 (클라이언트 공통 백오프) |

---

# Phase A. 인증·온보딩

## A-1. 현재 사용자 조회

> **참조:** `_162-users` #28 (Retrieve current user details)

### 기본 정보
- **기능:** 토큰 소유자 본인의 프로필을 조회한다.
- **Endpoint:** `GET /api/v4/user`
- **인증:** Bearer Token 필요 `[팀장 OAuth]` 또는 `[봇 토큰]`
- **권한:** 없음 (인증만 되면 가능)

### 설명
용도 3가지. ① 팀장 GitLab 연동 직후 `gitlab_user_id` 확보(linked_identities 저장), ② 봇 토큰 발급/rotate 직후 **토큰 유효성 검증**(가장 싼 검증 호출), ③ 팀원이 GitLab OAuth 연동(verified 승격) 시 신원 확인.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {token}` |

Path/Query/Body 없음.

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | GitLab user id (**핵심 저장 값**) | `30128` |
| `username` | string | 아이디 | `11kkh19` |
| `name` | string | 표시 이름 | `강기호` |
| `avatar_url` | string | 아바타 | `https://...` |

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `401` | 토큰 무효 | 검증 실패로 간주, 상위 플로우에서 처리 |

### 주의 사항
- rotate 트랜잭션에서 "새 토큰 검증" 단계로 반드시 이 API를 사용한다.

---

## A-2. 내 프로젝트 목록 조회 (온보딩 프로젝트 탐색)

> **참조:** `_129-projects` #12 (List all projects)

### 기본 정보
- **기능:** 인증 사용자가 멤버인 프로젝트 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects`
- **인증:** Bearer Token 필요 `[팀장 OAuth]`
- **권한:** 없음

### 설명
온보딩에서 팀 프로젝트 후보를 가져온다. `membership=true` + `min_access_level=30`으로 서버 사이드에서 후보를 좁힌 뒤, 클라이언트에서 스코어링(`S\d{2}P\d{2}` 네이밍 +100, `namespace.kind=="group"` && `s{기수}-*-sub{n}` 패턴 +50, `project_access.access_level>=40` +20, 최근 활동 +10, miniproject/user 네임스페이스 감점)하여 상위 후보를 카드로 제시하고 사용자가 확정한다. `simple=true`는 `permissions`가 빠지므로 **사용 금지**.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 팀장 OAuth 토큰 | `Bearer {token}` |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `membership` | boolean | Y(우리 규칙) | false | 내가 멤버인 프로젝트만 | `true` |
| `min_access_level` | integer | Y(우리 규칙) | - | 30 이상 → 공유그룹(20) 소속 잡음 제거 | `30` |
| `archived` | boolean | N | - | 아카이브 제외 | `false` |
| `order_by` | string | N | created_at | 최근 활동순 정렬 | `last_activity_at` |
| `sort` | string | N | desc | 정렬 방향 | `desc` |
| `per_page` | integer | N | 20 | 최대 100 | `50` |

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 프로젝트 ID (**저장**) | `1373907` |
| `name` | string | 스코어링 신호 1 | `S15P11A502` |
| `path_with_namespace` | string | 경로 | `s15-webmobile1-sub1/S15P11A502` |
| `namespace.kind` | string | 스코어링 신호 (`group`/`user`) | `group` |
| `namespace.full_path` | string | 스코어링 신호 2 | `s15-webmobile1-sub1` |
| `namespace.id` | integer | 그룹 ID (참고 저장) | `1396257` |
| `default_branch` | string | 초기 설정 자동화에 사용 | `main` |
| `last_activity_at` | string | 스코어링 신호 | ISO 8601 |
| `permissions.project_access.access_level` | integer | 스코어링 신호 + 발급 가능 판정 | `40` |
| `web_url` | string | 딥링크 | `https://lab.ssafy.com/...` |

### Errors
공통 에러 참조.

### 주의 사항
- 후보 자동 선택 금지 — 반드시 사용자 확정 UX를 거친다.

---

## A-3. 프로젝트 상세 조회

> **참조:** `_129-projects` #16 (Retrieve a project)

### 기본 정보
- **기능:** 확정된 프로젝트의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}`
- **인증:** Bearer Token 필요 `[팀장 OAuth]` (연동 시) / `[봇 토큰]` (운영 중 갱신)
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명
연동 확정 직후 `default_branch`, `web_url`, `permissions.project_access.access_level`을 재확인·저장한다. access_level이 40 미만이면 봇 토큰 발급이 불가하므로 여기서 온보딩을 중단하고 "Maintainer 권한의 팀장이 연동해야 합니다"를 안내한다.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1373907` |

### Response
#### `200 OK`
A-2와 동일 구조의 단일 객체. 저장 필드: `id, name, path_with_namespace, default_branch, web_url, namespace.id`.

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `404` | 접근 권한 없음/삭제됨 | 연동 해제 처리 + 재연동 안내 |

---

## A-4. Project Access Token(봇 토큰) 발급

> **참조:** `_04-access-tokens` #18 (Create a project access token)

### 기본 정보
- **기능:** 프로젝트 전용 봇 토큰을 발급한다.
- **Endpoint:** `POST /api/v4/projects/{id}/access_tokens`
- **인증:** Bearer Token 필요 — **반드시 `[팀장 OAuth]` (사용자 자격 토큰). 봇 토큰으로 호출 불가** (원문: "You must use a personal access token with this endpoint")
- **권한:** Project Maintainer(40) 이상. 자기 권한보다 높은 `access_level`의 토큰은 생성 불가

### 설명
연동의 핵심 단계. 발급 후 모든 수집·웹훅·자동화는 이 토큰으로 수행하므로 팀장 OAuth 토큰 만료와 무관하게 동작한다. 응답의 `token` 평문은 **이 응답에서만 노출**되므로 즉시 암호화 저장한다. 봇 계정의 `user_id`도 저장한다(봇이 남긴 코멘트/이벤트 식별용).

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 팀장 OAuth 토큰 | `Bearer {oauth}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |

#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | - | 봇 이름 (팀에게 보임) | `ssagy-bot` |
| `scopes` | array | Y | - | `api` 하나로 read/write/hook 전부 커버 | `["api"]` |
| `access_level` | integer | Y(우리 규칙) | 10~50 | 웹훅 생성·브랜치 보호에 40 필요 | `40` |
| `expires_at` | string | Y(우리 규칙) | YYYY-MM-DD | 프로젝트 종료일 + 여유 | `2026-08-30` |

```json
{ "name": "ssagy-bot", "scopes": ["api"], "access_level": 40, "expires_at": "2026-08-30" }
```

### Response
#### `201 Created`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `token` | string | **평문 토큰, 이 응답에서만 노출** | `glpat-...` |
| `id` | integer | 토큰 ID (revoke 시 필요) | `602` |
| `user_id` | integer | 봇 계정 user id (**저장**) | `31999` |
| `expires_at` | string | 만료일 (rotate 스케줄 기준) | `2026-08-30` |

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `400` | scopes/access_level 검증 실패, 또는 인스턴스에서 PAT 기능 비활성 | 관리자 정책 문제면 플랜 B(토큰 수동 붙여넣기)로 폴백 |
| `401` | OAuth 토큰 만료 | OAuth 재승인 유도 |
| `404` | Maintainer 미만 | 온보딩 사전 검증으로 예방 |

### 주의 사항
- 발급 직후 `GET /user`(A-1)를 봇 토큰으로 호출해 검증 후 `active` 상태로 저장한다.
- lab.ssafy.com(CE)에서 이 기능이 관리자에 의해 꺼져 있을 가능성 → **POC 1순위 검증 항목**.

---

## A-5. 봇 토큰 자가 회전 (rotate)

> **참조:** `_04-access-tokens` #15 (Rotate a project access token — self)

### 기본 정보
- **기능:** 봇 토큰이 자기 자신을 새 토큰으로 교체한다.
- **Endpoint:** `POST /api/v4/projects/{id}/access_tokens/self/rotate`
- **인증:** Bearer Token 필요 — `[봇 토큰]` 자신 (팀장 개입 불필요)
- **권한:** 토큰 자신

### 설명
만료 7일 전 스케줄러가 호출한다. 성공 시 **구 토큰은 즉시 무효화**되므로 트랜잭션 순서가 중요하다: ① rotate 호출 → ② 새 토큰을 `pending`으로 저장 → ③ 새 토큰으로 `GET /user` 검증 → ④ `active` 승격. ①과 ② 사이 서버 장애 시 토큰 유실 → 복구는 팀장 재연동(A-4)뿐이므로 재연동 버튼을 UI에 상시 노출한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | **현재 봇 토큰** | `Bearer glpat-...` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |

#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expires_at` | string | N | YYYY-MM-DD | 새 만료일 (미지정 시 짧게 잡힘 → 항상 명시) | `2026-09-30` |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `token` | string | **새 평문 토큰** | `glpat-rotated...` |
| `id` | integer | 새 토큰 ID | `603` |
| `expires_at` | string | 새 만료일 | `2026-09-30` |

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `401` | 구 토큰 이미 무효 | 팀장 재연동 안내 |
| `403`/`405` | rotate 비허용(인스턴스 정책/버전) | 폴백: A-4 재발급 플로우 |

### 주의 사항
- rotate 계열은 GitLab 16.x+ 기능 → `GET /api/v4/version`으로 인스턴스 버전 사전 확인 (**POC 항목**).

---

## A-6. 봇 토큰 폐기 (연동 해제)

> **참조:** `_04-access-tokens` #20 (Revoke a project access token)

### 기본 정보
- **기능:** 봇 토큰을 폐기한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/access_tokens/{token_id}`
- **인증:** Bearer Token 필요 `[팀장 OAuth]` 또는 `[봇 토큰]`
- **권한:** Project Maintainer 이상

### 설명
워크스페이스에서 "GitLab 연동 해제" 시 호출한다. 등록해둔 웹훅 삭제(B-1의 DELETE)와 함께 실행해 잔여물을 남기지 않는다.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |
| `token_id` | integer | Y | A-4/A-5에서 저장한 토큰 ID | `603` |

### Response
#### `204 No Content`

### 주의 사항
- 폐기 후 DB의 토큰 레코드는 삭제하지 말고 `revoked` 마킹 (감사 이력).

---

## A-7. 프로젝트 직접 멤버 조회 (팀원 후보 카드)

> **참조:** `_91-members` #08 (List all direct members of a project)

### 기본 정보
- **기능:** 프로젝트에 **직접 추가된** 멤버만 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/members`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
"GitLab에서 누구세요?" 매핑 카드의 소스. 실측 결과 `/members/all`(A-8)에는 상위 그룹 상속 멤버(SSAFY 운영진·코치·sysadmin, 전원 access_level 40)가 다수 포함되므로, **팀원 카드는 직접 멤버 기준**으로 만든다. 직접 멤버에도 코치가 섞이면 멤버십 `created_at`(팀원은 프로젝트 생성 시점인 2026-07 근처, 운영진은 2019~2024)과 username 패턴(`sysadmin`, `*.ssafy`, 이름 내 "코치")으로 보조 필터링한다.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `per_page` | integer | Y(우리 규칙) | 20 | **기본 20 잘림 방지** | `100` |

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | gitlab_user_id (**매핑 키**) | `30128` |
| `username` | string | 아이디 | `11kkh19` |
| `name` | string | 카드 표시 이름 | `강기호` |
| `avatar_url` | string | 카드 아바타 | `https://...` |
| `access_level` | integer | 참고용 (팀장 판정에 쓰지 말 것) | `40` |
| `created_at` | string | 멤버십 등록일 (운영진 필터 신호) | `2026-07-14T...` |

### 주의 사항
- "access_level 40 = 팀장" 규칙은 폐기됨(운영진 전원 40). 우리 서비스의 팀장 = 워크스페이스 생성·봇 토큰 발급자.

---

## A-8. 프로젝트 전체 멤버 조회 (상속 포함)

> **참조:** `_91-members` #10 (List all members of a project)

### 기본 정보
- **기능:** 직접 멤버 + 상위 그룹 상속 멤버 전체를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/members/all`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
팀원 카드용이 아니라 **이벤트/코멘트 author 매핑 사전**으로 사용한다. 코치·컨설턴트가 MR에 코멘트를 달 수 있으므로 상속 멤버까지 알아두면 "알 수 없는 사용자" 처리가 줄어든다. 통계 집계에서는 A-7 기반 팀원 6명으로만 필터링한다.

### Request
A-7과 동일 + path 끝에 `/all`. `per_page=100` 필수 (실측: 상속 멤버만 20명 이상 → 기본값이면 팀원이 2페이지로 밀림).

### Response
A-7과 동일 구조.

---

# Phase B. 초기 설정 자동화 (온보딩 마법사)

## B-1. 웹훅 목록 조회 (중복 방지)

> **참조:** `_68-hooks` #27 (List all webhooks for a project)

### 기본 정보
- **기능:** 프로젝트에 등록된 웹훅 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/hooks`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Project Maintainer 이상

### 설명
웹훅 생성(B-2) 전에 호출해 우리 수신 URL의 훅이 이미 있으면 생성 대신 갱신(B-3)한다. 재연동·재실행 시 중복 훅 방지가 목적. 연동 해제 시에는 여기서 찾은 hook_id로 `DELETE /projects/{id}/hooks/{hook_id}`(같은 카테고리 #31)를 호출한다.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | hook id | `101` |
| `url` | string | 수신 URL (우리 것인지 비교 키) | `https://api.ssagy.io/...` |
| `push_events` 등 | boolean | 구독 상태 | `true` |

---

## B-2. 웹훅 등록

> **참조:** `_68-hooks` #28 (Add a webhook to a project)

### 기본 정보
- **기능:** 프로젝트에 이벤트 웹훅을 등록한다.
- **Endpoint:** `POST /api/v4/projects/{id}/hooks`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Project Maintainer 이상

### 설명
"웹훅 수동 설정 제거"라는 제품 핵심 가치의 구현 지점. push/MR/note/pipeline/issue 이벤트를 구독하고, `token`(시크릿)을 심어 수신 시 `X-Gitlab-Token` 헤더로 위조 요청을 차단한다. 팀원별 커밋 집계를 위해 브랜치 필터는 `all_branches`.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 봇 토큰 | `Bearer glpat-...` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |

#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `url` | string | Y | https | 우리 수신 엔드포인트 (워크스페이스 식별자 포함) | `https://api.ssagy.io/webhooks/gitlab/{key}` |
| `name` | string | N | - | 훅 이름 | `SSAGY` |
| `token` | string | Y(우리 규칙) | - | 수신 검증 시크릿 (응답에 미반환) | 랜덤 32자 |
| `push_events` | boolean | Y | - | 커밋 수집 | `true` |
| `merge_requests_events` | boolean | Y | - | MR 알림·보드 | `true` |
| `note_events` | boolean | Y | - | 코멘트 → 리뷰 반응 감지 | `true` |
| `pipeline_events` | boolean | Y | - | 빌드 상태 | `true` |
| `issues_events` | boolean | Y | - | 이슈 메트릭 | `true` |
| `branch_filter_strategy` | string | Y(우리 규칙) | wildcard/regex/all_branches | 전 브랜치 push 수집 | `all_branches` |
| `enable_ssl_verification` | boolean | Y | - | SSL 검증 | `true` |

### Response
#### `201 Created`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | hook id (**저장** — 테스트/로그/삭제에 필요) | `101` |
| `alert_status` | string | 훅 상태 (`executable`) | `executable` |
| `token_present` | boolean | 시크릿 설정 여부 | `true` |

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `422` | URL 형식/사설 IP 차단 정책 | 수신 서버가 공인 도메인·HTTPS인지 확인 |

### 주의 사항
- lab.ssafy.com 아웃바운드 웹훅 방화벽 정책 → **POC 검증 항목** (테스트 발사 B-4로 확인).

---

## B-3. 웹훅 수정

> **참조:** `_68-hooks` #30 (Update a project webhook)

### 기본 정보
- **기능:** 기존 웹훅의 URL/구독 이벤트를 갱신한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/hooks/{hook_id}`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Project Maintainer 이상

### 설명
B-1에서 우리 훅이 이미 발견됐을 때 생성 대신 호출(멱등 재연동). Body는 B-2와 동일 스키마.

### Request / Response
B-2와 동일 (path에 `hook_id` 추가, 성공 시 `200 OK`).

---

## B-4. 테스트 웹훅 발사 (연동 검증)

> **참조:** `_68-hooks` #33 (Trigger a test webhook)

### 기본 정보
- **기능:** 지정 트리거 타입의 테스트 페이로드를 즉시 발송시킨다.
- **Endpoint:** `POST /api/v4/projects/{id}/hooks/{hook_id}/test/{trigger}`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Project Maintainer 이상

### 설명
웹훅 등록 직후 호출 → 우리 서버가 수 초 내 수신하면 온보딩 UI에 "연동 완료 ✓" 표시. end-to-end(방화벽 포함) 검증을 온보딩 단계에서 끝내는 장치.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |
| `hook_id` | integer | Y | B-2에서 저장한 hook id | `101` |
| `trigger` | string | Y | 테스트 이벤트 타입 | `push_events` |

### Response
#### `201 Created` (본문 없음에 준함 — 실제 검증은 우리 수신 서버에서)

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `429` | **웹훅당·사용자당 분당 5회 제한** | 온보딩 재시도 버튼에 쿨다운 필수 |
| `422` | 트리거할 데이터 없음 (빈 레포에 push 테스트 등) | 다른 trigger로 시도 또는 안내 |

---

## B-5. 웹훅 전송 로그 조회

> **참조:** `_68-hooks` #32 (List all events — project hook)

### 기본 정보
- **기능:** 웹훅이 발송한 이벤트 이력(응답 코드 포함)을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/hooks/{hook_id}/events`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Project Maintainer 이상

### 설명
운영 중 유실 진단용. `response_status`가 4xx/5xx인 이벤트를 찾아 B-6으로 재전송한다. 폴링 보정(C-6)과 함께 이중 안전망.

### Request
#### Path parameters
`id`, `hook_id` (B-4와 동일).

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | event id (재전송 키) | `9001` |
| `trigger` | string | 이벤트 종류 | `push_hooks` |
| `response_status` | integer | 우리 서버가 반환한 코드 | `500` |

---

## B-6. 웹훅 이벤트 재전송

> **참조:** `_68-hooks` #34 (Resend a webhook event)

### 기본 정보
- **기능:** 실패한 웹훅 이벤트를 다시 발송시킨다.
- **Endpoint:** `POST /api/v4/projects/{id}/hooks/{hook_id}/events/{event_id}/resend`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Project Maintainer 이상

### Request
Path: `id`, `hook_id`, `event_id`(B-5에서 획득).

### Response
`201 Created`. 실제 결과는 수신 서버에서 확인.

---

## B-7. 브랜치 목록 조회

> **참조:** `_21-branches` #01 (List all repository branches)

### 기본 정보
- **기능:** 저장소의 브랜치 목록(보호 여부·머지 여부·head 커밋 포함)을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/branches`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
용도 3가지. ① 저장소 건강 진단: default 브랜치의 `protected` 여부 검사, ② 브랜치 보호 자동 적용(B-8) 전 사전 확인(이미 보호 시 스킵), ③ 커밋 백필 시 브랜치별 수집 루프의 입력.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `per_page` | integer | Y(우리 규칙) | 20 | 잘림 방지 | `100` |
| `sort` | string | N | name_asc | 최근 갱신순 | `updated_desc` |

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `name` | string | 브랜치명 | `main` |
| `protected` | boolean | 보호 여부 (**진단 키**) | `true` |
| `merged` | boolean | 기본 브랜치 병합 완료 여부 | `false` |
| `default` | boolean | 기본 브랜치 여부 | `true` |
| `commit.id` | string | head 커밋 SHA | `a1b2...` |
| `web_url` | string | 딥링크 | `https://...` |

---

## B-8. 브랜치 보호 적용

> **참조:** `_21-branches` #06 (Protect a single branch)

### 기본 정보
- **기능:** 단일 브랜치에 보호 설정을 적용한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/repository/branches/{branch}/protect`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Project Maintainer / Owner

### 설명
초기 설정 자동화의 "main 직접 push 금지" 항목. CE에서 동작하는 범위의 기본 보호만 적용한다(필수 승인 수 강제는 Premium이라 불가 — 대신 "승인 0건 머지 감지 알림"으로 소프트 대체). **B-10(파일 커밋)보다 나중에 실행**해야 봇의 초기 커밋이 막히지 않는다.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |
| `branch` | string | Y | 대상 브랜치 (URL 인코딩) | `main` |

#### Body
| 필드 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `developers_can_push` | boolean | Y(우리 규칙) | false | 직접 push 금지 | `false` |
| `developers_can_merge` | boolean | Y(우리 규칙) | false | MR 머지는 허용 | `true` |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `protected` | boolean | `true` 확인 |

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `409` | 이미 보호된 브랜치 | B-7 사전 확인으로 예방, 발생 시 성공 취급 |

---

## B-9. 사용 언어 통계 조회

> **참조:** `_129-projects` #28 (Retrieve programming language usage information)

### 기본 정보
- **기능:** 저장소의 언어별 사용 비중(%)을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/languages`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
초기 설정 마법사에서 기술스택을 자동 감지해 `.gitignore` 템플릿(Java/Spring, TS/React 등)을 선택한다. 빈 레포면 빈 객체가 오므로 사용자 수동 선택으로 폴백.

### Request
Path: `id`.

### Response
#### `200 OK`
```json
{ "Java": 65.5, "TypeScript": 24.0, "HTML": 10.5 }
```

---

## B-10. 파일 자동 커밋 (.gitignore / MR·이슈 템플릿)

> **참조:** `_36-commits` #02 (Create a commit)

### 기본 정보
- **기능:** 여러 파일의 생성/수정을 단일 커밋으로 원격 브랜치에 반영한다.
- **Endpoint:** `POST /api/v4/projects/{id}/repository/commits`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Developer 이상

### 설명
`.gitignore`, `.gitlab/merge_request_templates/Default.md` 등 초기 파일들을 커밋 1개로 생성한다. **이미 존재하는 파일에 `create` 액션을 쓰면 400** → 사전에 파일 존재를 확인해 `create`/`update`를 분기한다. 브랜치 보호(B-8)보다 먼저 실행한다.

### Request
#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `branch` | string | Y | - | 대상 브랜치 | `main` |
| `commit_message` | string | Y | - | 커밋 메시지 | `chore: SSAGY 초기 설정` |
| `actions` | array | Y | 1개 이상 | `{action, file_path, content}` 배열. action: `create`/`update`/`delete`/`move` | 아래 참조 |

```json
{
  "branch": "main",
  "commit_message": "chore: SSAGY 초기 설정",
  "actions": [
    { "action": "create", "file_path": ".gitignore", "content": "node_modules/\n.env*\n*.pem\n..." },
    { "action": "create", "file_path": ".gitlab/merge_request_templates/Default.md", "content": "## 작업 내용\n..." }
  ]
}
```

### Response
#### `201 Created`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 생성된 커밋 SHA | `b2c3...` |
| `web_url` | string | 딥링크 | `https://...` |

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `400` | 기존 파일에 create / 보호 브랜치 push 불가 | 존재 확인 후 분기 / B-8 이전에 실행 |

---

# Phase C. 데이터 수집 (백필 + 증분 + 폴링 보정)

## C-1. 커밋 목록 조회 (핵심 메트릭)

> **참조:** `_36-commits` #01 (List all repository commits)

### 기본 정보
- **기능:** 브랜치·작성자·기간 필터로 커밋 이력을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
커밋 수·LoC(추가/삭제 라인)·시간대 히트맵의 원천. **백필 전용** — 운영 중 증분은 push 웹훅이 담당한다. 한 번에 한 `ref_name`만 조회 가능하므로 백필은 B-7의 브랜치 목록을 돌며 브랜치별 수집 후 커밋 `id`(SHA)로 dedupe한다. `with_stats=true`로 라인 통계를 함께 받는다.

### Request
#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ref_name` | string | Y(백필 루프) | default branch | 대상 브랜치 | `feature/login` |
| `since` | string | N | - | 시작 시각 (ISO 8601) | `2026-07-14T00:00:00Z` |
| `until` | string | N | - | 종료 시각 | `2026-07-25T00:00:00Z` |
| `with_stats` | boolean | Y(우리 규칙) | false | LoC 통계 포함 | `true` |
| `per_page` | integer | Y | 20 | 최대 100 | `100` |
| `page` | integer | - | 1 | `X-Next-Page` 헤더 따라 순회 | `2` |

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 커밋 SHA (**dedupe 키**) | `a1b2...` |
| `title` | string | 메시지 첫 줄 | `feat: add login` |
| `author_name` / `author_email` | string | 작성자 (**이메일↔user_id 매핑 필요**) | `kkh@...` |
| `committed_date` | string | 집계 기준 시각 | ISO 8601 |
| `stats.additions` / `stats.deletions` | integer | LoC | `45` / `10` |
| `web_url` | string | 딥링크 | `https://...` |

### 주의 사항
- `author_email`↔팀원 매핑은 push 웹훅 페이로드(user_id + 커밋 이메일 동시 포함)로 학습하고, 미매핑분은 온보딩에서 수동 지정.

---

## C-2. MR 목록 조회 (보드·사이클타임·병목)

> **참조:** `_93-merge-requests` #16 (List all project merge requests)

### 기본 정보
- **기능:** 프로젝트 MR 목록을 상태·기간·작성자·리뷰어로 필터 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
용도별 호출 프리셋 3가지.
① 백필: `state=all&order_by=updated_at&sort=desc`
② 증분 동기화: `state=all&updated_after={마지막 동기화 시각}` (**증분 키**)
③ 병목 감지(30분 폴링): `state=opened&updated_before={now-24h}&order_by=updated_at&sort=asc` → 결과가 곧 "24h+ 미반응 MR 목록".
응답만으로 MR 보드·사이클타임(`merged_at - created_at`)·리뷰 코멘트 수(`user_notes_count`)가 채워진다.

### Request
#### Query parameters (우리가 쓰는 것만)
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `state` | string | Y | opened | `opened`/`merged`/`closed`/`all` | `all` |
| `updated_after` | string | 증분 시 | - | ISO 8601 | `2026-07-25T09:00:00Z` |
| `updated_before` | string | 병목 시 | - | ISO 8601 | `2026-07-24T09:00:00Z` |
| `order_by` | string | N | created_at | `updated_at`/`merged_at` 지원 | `updated_at` |
| `sort` | string | N | desc | 정렬 | `asc` |
| `author_id` / `reviewer_id` | integer | N | - | 팀원별 필터 | `30128` |
| `with_merge_status_recheck` | boolean | N | false | merge_status 비동기 재계산 요청 | `true` |
| `per_page` | integer | Y | 20 | 최대 100 | `100` |

### Response
#### `200 OK` (배열, 주요 필드)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `iid` | integer | MR 내부 번호 (**딥링크·상세 조회 키**) | `15` |
| `title` / `state` / `draft` | - | 보드 카드 | - |
| `author.username` / `reviewers[]` | object | 담당자 표시 | - |
| `created_at` / `updated_at` / `merged_at` | string | 사이클타임 계산 | ISO 8601 |
| `has_conflicts` | boolean | 컨플릭트 뱃지 | `false` |
| `detailed_merge_status` | string | 머지 가능 판정 (merge_status는 deprecated) | `mergeable` |
| `user_notes_count` | integer | 리뷰 반응 지표 | `3` |
| `source_branch` / `target_branch` | string | 카드 표시 | - |
| `web_url` | string | 딥링크 (`+"/diffs"` = diff 탭 직행) | `https://...` |

### 주의 사항
- 목록의 `merge_status`류는 캐시가 낡을 수 있음 → 알림 발송 직전에는 C-3 단건 조회로 재확인 (오탐 방지).

---

## C-3. MR 단건 상세 조회

> **참조:** `_93-merge-requests` #19 (Retrieve a merge request)

### 기본 정보
- **기능:** MR 1건의 상세(파이프라인·diff refs·정확한 머지 상태 포함)를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
① MR 상세 페이지 렌더, ② 알림 발송 직전 상태 재확인(컨플릭트/머지가능), ③ "지금 머지 가능" 신호 계산(승인 완료 ∧ `head_pipeline.status == "success"` ∧ `has_conflicts == false`)에 사용.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |
| `merge_request_iid` | integer | Y | MR IID | `15` |

### Response
#### `200 OK` (C-2 필드 + 추가분)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `detailed_merge_status` | string | 정확한 머지 판정 | `mergeable` |
| `changes_count` | string | 변경 파일 수 | `"12"` |
| `head_pipeline.status` | string | 최신 빌드 상태 | `success` |
| `head_pipeline.web_url` | string | 파이프라인 딥링크 | `https://...` |
| `diff_refs` | object | base/head/start SHA | - |

---

## C-4. MR 변경 내용(diff) 조회 — AI 리뷰 입력

> **참조:** `_93-merge-requests` #27 (Retrieve merge request changes) ※ 대체 API: 같은 카테고리 #28 (List all merge request diffs — changes가 deprecated 방향이므로 신규 구현 시 #28 우선 검토)

### 기본 정보
- **기능:** MR의 전체 파일별 diff를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/changes`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
AI 사전 코드 리뷰·리뷰어 가이드·머지 전 시크릿 게이트·컨플릭트 조기 경보(열린 MR 간 `new_path` 교집합)의 입력. LLM에 넘기기 전 방어 로직 필수: `too_large`(파일 스킵), `generated_file`(lock 파일 등 스킵), `overflow`(전체 초과 → 파일 목록만 요약).

### Request
#### Path parameters
C-3과 동일.

#### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `unidiff` | boolean | N | Unified diff 포맷으로 수신 | `true` |

### Response
#### `200 OK` (C-3 구조 + `changes[]`)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `changes[].new_path` / `old_path` | string | 파일 경로 (**교집합 계산 키**) | `src/UserService.java` |
| `changes[].diff` | string | 패치 텍스트 (LLM 입력) | `@@ -1,3 +1,5 @@...` |
| `changes[].new_file` / `deleted_file` / `renamed_file` | boolean | 변경 유형 | - |
| `changes[].too_large` | boolean | **true면 diff 비어 있음 → 스킵** | `false` |
| `changes[].generated_file` | boolean | 자동 생성 파일 → 스킵 | `false` |
| `overflow` | boolean | 전체 diff 한도 초과 | `false` |

---

## C-5. MR 승인 현황 조회

> **참조:** `_92-merge-request-approvals` #10 (Retrieve approval state for a merge request)

### 기본 정보
- **기능:** MR의 승인 여부·승인자 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approvals`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
MR 카드의 "승인 n명" 뱃지, "MR 승인됨" 알림, "승인 0건인데 머지됨" 소프트 가드 감지에 사용. CE에서 동작하는 기본 승인 조회 API다 (승인 "규칙/강제"는 Premium이라 사용하지 않음 — 같은 카테고리 #01~#09는 **제외 목록**).

### Request
Path: `id`, `merge_request_iid`.

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `approved` | boolean | 승인 존재 여부 | `true` |
| `approved_by[].user.username` | string | 승인자 | `pmk123` |
| `approved_by[].approved_at` | string | 승인 시각 | ISO 8601 |

### 주의 사항
- 원클릭 승인 기능을 넣을 경우 `POST .../approve`(같은 카테고리 #12)를 **팀원 개인 OAuth 토큰**으로 호출해야 함 (봇 토큰이면 봇 명의 승인이 됨). verified 연동 사용자에게만 노출.

---

## C-6. 프로젝트 이벤트 조회 (타임라인 + 웹훅 유실 보정)

> **참조:** `_52-events` #01 (List all visible events for a project)

### 기본 정보
- **기능:** 프로젝트에서 발생한 활동 이벤트(push/이슈/MR/코멘트 등)를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/events`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
① 대시보드 활동 타임라인 피드, ② 5~10분 주기 폴링으로 웹훅 유실분 보정(이벤트 소싱). `after`/`before`가 **날짜(YYYY-MM-DD) 단위**라 시각 필터 불가 → "오늘 날짜 조회 후 저장된 마지막 event id 이후만 insert" 방식으로 dedupe한다.

### Request
#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `after` | string | Y(폴링) | - | 이 날짜 이후 (YYYY-MM-DD) | `2026-07-24` |
| `action` | string | N | - | `pushed`/`merged`/`commented` 등 필터 | `pushed` |
| `target_type` | string | N | - | `issue`/`merge_request`/`note` 등 | `merge_request` |
| `sort` | string | N | desc | 정렬 | `desc` |
| `per_page` | integer | Y | 20 | 최대 100 | `100` |

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 이벤트 ID (**dedupe 키**) | `1001` |
| `action_name` | string | 액션 | `pushed to` |
| `target_type` / `target_title` | string | 대상 | `MergeRequest` |
| `author.id` / `author.username` | - | 발생 유저 (**user_id 기반 매핑**) | `30128` |
| `push_data.ref` / `commit_count` | - | push 상세 | `main` / `3` |
| `created_at` | string | 시각 | ISO 8601 |

---

## C-7. 사용자 기여 이벤트 조회 (사이드뷰 / 스크럼 초안)

> **참조:** `_52-events` #03 (Retrieve contribution events for a user)

### 기본 정보
- **기능:** 특정 사용자의 기여 활동(커밋 push, 이슈, MR, 코멘트)을 조회한다.
- **Endpoint:** `GET /api/v4/users/{id}/events`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 인증된 사용자

### 설명
사이드뷰의 "오늘/어제 내가 한 일"과 데일리 스크럼 자동 초안의 개인 단위 소스. 프로젝트 이벤트(C-6)를 사용자별로 필터링하는 것보다 호출이 단순하다. 단, 사용자의 **모든 프로젝트** 이벤트가 오므로 `project_id`로 후처리 필터링한다.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer | Y | 매핑된 gitlab_user_id | `30128` |

#### Query parameters
C-6과 동일 (`action`, `target_type`, `per_page`).

### Response
C-6과 동일 구조.

---

## C-8. 커밋 빌드 상태 조회

> **참조:** `_35-commit-statuses` #01 (List all commit statuses)

### 기본 정보
- **기능:** 특정 커밋에 결합된 빌드/파이프라인 상태 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/statuses`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** 프로젝트 멤버

### 설명
MR 카드·커밋 스트립의 빌드 상태 뱃지. D-1으로 Jenkins가 밀어넣은 상태를 다시 읽는 조회 짝이다. pipeline 웹훅이 실시간을 담당하므로 이 API는 백필·재확인용.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |
| `sha` | string | Y | 커밋 SHA | `a1b2...` |

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `status` | string | `pending`/`running`/`success`/`failed` | `success` |
| `name` | string | 잡 라벨 | `jenkins/build` |
| `target_url` | string | Jenkins 빌드 딥링크 | `https://...` |
| `finished_at` | string | 완료 시각 | ISO 8601 |

---

# Phase D. Jenkins 연동 (역방향 주입)

## D-1. 커밋 빌드 상태 등록/갱신

> **참조:** `_35-commit-statuses` #02 (Create or update a commit pipeline status)

### 기본 정보
- **기능:** 외부 CI(Jenkins)의 빌드 결과를 GitLab 커밋 상태로 기록한다.
- **Endpoint:** `POST /api/v4/projects/{id}/statuses/{sha}`
- **인증:** Bearer Token 필요 `[봇 토큰]`
- **권한:** Developer 이상

### 설명
우리 서버가 Jenkins 빌드 결과를 수신하면(Jenkins 연동 파트) 이 API로 GitLab 커밋에 상태를 역주입한다. 효과: GitLab MR 화면에도 빌드 뱃지가 생기고, `target_url`로 Jenkins 딥링크가 걸리며, C-3의 `head_pipeline`/C-8 조회와 일관된 상태가 유지된다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 봇 토큰 | `Bearer glpat-...` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer/string | Y | 프로젝트 ID | `1373907` |
| `sha` | string | Y | 빌드 대상 커밋 SHA | `a1b2...` |

#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `state` | string | Y | pending/running/success/failed/canceled/skipped | 빌드 상태 | `failed` |
| `ref` | string | N | - | 브랜치명 | `main` |
| `name` | string | Y(우리 규칙) | - | 상태 라벨 (갱신 시 동일 name으로 upsert) | `jenkins/build` |
| `target_url` | string | Y(우리 규칙) | - | Jenkins 빌드 상세 URL | `https://.../job/A502/15` |
| `description` | string | N | - | 요약 한 줄 | `Build #15 failed at test stage` |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 상태 ID | `891` |
| `status` | string | 반영된 상태 | `failed` |

### 주의 사항
- 같은 `sha`+`name` 조합으로 재호출하면 상태가 갱신된다 (pending → running → failed 순 전이).

---

# 제외 확정 목록 (호출하지 않음)

| API | 카테고리·번호 | 제외 사유 |
|---|---|---|
| MR 승인 규칙 CRUD | `_92` #01~#05 | Premium 전용 — lab.ssafy.com은 CE |
| 프로젝트/그룹 승인 정책 설정 | `_92` #06~#09 | Premium 전용 (필수 승인 수 강제 불가) |
| 그룹 웹훅 | `_68` #01~#05 | 사용자가 그룹 멤버가 아님(group_access null) → 403/404 |
| 그룹 멤버 추가/관리 | `_91` #02, #05, #06 | SSAFY가 그룹을 관리, 우리 권한 밖 |
| Service Account 계열 | `_04` #07~#14 | Admin 권한 필요 |
| Personal Access Token 전역 관리 | `_04` #27~#34 | 불필요 + PAT 수집은 보안 부채 (OAuth+봇 토큰으로 충분) |
| 커밋 cherry-pick/revert | `_36` #08, #09 | 쓰기 작업은 딥링크로 GitLab에 위임 (대체 금지 철학) |
| MR 머지/리베이스 실행 | `_93` #32, #35 | 동일 |
| 사용자 생성/수정/차단 등 | `_162` Admin 목록 | Admin 전용 |
| Uploads 계열 | `_129` #57~#63 | 유스케이스 없음 |

# POC 검증 체크리스트 (호출 전 확정 필요)

1. `GET /api/v4/version` — 인스턴스 버전 확인 (rotate self 엔드포인트는 16.x+)
2. A-4 실호출 — CE에서 Project Access Token 생성 허용 여부 (막혀 있으면 플랜 B: 토큰 수동 붙여넣기)
3. A-5 실호출 — self/rotate 동작 여부
4. B-2 → B-4 — lab.ssafy.com 아웃바운드 웹훅이 우리 서버(공인 도메인)에 도달하는지
5. A-7 — 직접 멤버 조회 결과가 실제 팀원 6명과 일치하는지 (`per_page=100` 필수)
6. lab.ssafy.com 프로필 → Settings → Applications 메뉴 존재 여부 (OAuth 앱 등록 가능 여부; 불가 시 연동 UX를 플랜 B로 설계)
