# Mattermost 연동 최종 API 명세

SSAGY가 meeting.ssafy.com(Mattermost self-hosted)에 호출하는 API의 최종 목록.
권한 판정 기준은 AGENTS.md의 **실효 권한 지도(system_user + team_user + channel_user 합집합, 2026-07-25 실측)**이다.
과거 `system_user` 12개 권한만 기준으로 한 summary 분석(`_17-webhooks` 등 "사용 가능 0개")은 **폐기**한다 — 웹훅/슬래시 명령어/발송 전부 가능함이 실증됐다.

## 공통 사항

- **Base URL:** `https://meeting.ssafy.com/api/v4` (incoming webhook 발송만 예외: `https://meeting.ssafy.com/hooks/{key}`)
- **인증 주체 구분:**
  - `[사용자 토큰]` — MM OAuth 앱(우리가 등록)을 통해 위임받은 각 사용자의 access token. 채널 생성·웹훅 생성 등 **모든 관리 작업은 그 사용자의 팀/채널 멤버십 권한으로** 실행됨
  - `[웹훅 URL]` — incoming webhook 발송. **인증 헤더 불필요**, URL 자체가 자격증명
- **`manage_own_*` 주의:** 웹훅·슬래시 명령어는 **생성한 계정만** 수정/삭제 가능. 연동 계정(팀장)이 바뀌면 기존 리소스를 지우지 못하므로, 생성자 user_id를 DB에 기록해 둔다.
- **공통 에러:** `401`(토큰 만료 → 재연동), `403`(권한/멤버십 없음), `404`(리소스 없음)

---

# Phase A. 연동·인증

## A-1. OAuth 앱 등록 (개발 단계 1회)

> **참조:** `_21-oauth` #01 (Register OAuth app) — 권한 `manage_oauth` ✅ (system_user)

### 기본 정보
- **기능:** SSAGY를 Mattermost OAuth 2.0 클라이언트로 등록한다.
- **Endpoint:** `POST /api/v4/oauth/apps`
- **인증:** Bearer Token 필요 `[개발자 계정 세션]`
- **권한:** `manage_oauth`

### 설명
운영 전 1회성 작업. 등록으로 얻는 `client_id`/`client_secret`으로 팀원들의 MM 계정 연동(OAuth authorization code flow)을 구현한다. 이후 모든 MM API 호출은 이 앱으로 위임받은 사용자 토큰으로 수행한다. GitLab의 linked_identities 패턴을 그대로 재사용한다.

### Request
#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `name` | string | Y | 앱 이름 (승인 화면에 표시) | `SSAGY` |
| `description` | string | Y | 짧은 설명 | `SSAFY 통합 워크스페이스` |
| `callback_urls` | string[] | Y | OAuth 콜백 | `["https://ssagy.io/auth/mm/callback"]` |
| `homepage` | string | Y | 서비스 홈페이지 | `https://ssagy.io` |

### Response
#### `201 Created`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | string | client_id (**환경변수 보관**) |
| `client_secret` | string | client_secret (**시크릿 보관, 응답에서만 노출 아님 — 조회 가능하나 유출 주의**) |

### 주의 사항
- 앱 생성자 계정만 수정/삭제 가능(`manage_oauth`는 본인 앱 한정) → 팀 공용 계정보다 유지 책임자 계정으로 등록.
- 토큰 발급 엔드포인트 등 메타데이터는 `GET /.well-known/oauth-authorization-server`(`_21-oauth` #08, 인증 불요)로 확인.

---

## A-2. 내 정보 조회 (연동 검증·신원 매핑)

> **참조:** 표준 MM API (문서 폴더 외) — 권한: 본인

### 기본 정보
- **기능:** 토큰 소유자 본인의 MM 프로필을 조회한다.
- **Endpoint:** `GET /api/v4/users/me`
- **인증:** Bearer Token 필요 `[사용자 토큰]`
- **권한:** 없음 (본인)

### 설명
MM OAuth 연동 직후 호출해 `id`(mm_user_id), `username`을 linked_identities에 저장한다. 토큰 유효성 검증용 최소 호출로도 사용.

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | mm_user_id (**매핑 키**) | `9f7x...` |
| `username` | string | 아이디 | `kkh_ssafy` |

---

## A-3. 내 팀 목록 조회

> **참조:** `_05-teams` #12 (Get a user's teams) — 권한: 본인 ✅

### 기본 정보
- **기능:** 사용자가 속한 팀 목록을 조회한다.
- **Endpoint:** `GET /api/v4/users/{user_id}/teams` (`user_id`에 `me` 사용 가능)
- **인증:** Bearer Token 필요 `[사용자 토큰]`
- **권한:** 본인 조회는 불요

### 설명
MM 연동 온보딩에서 "어느 팀에 SSAGY 채널을 만들까"의 선택지를 제공한다. SSAFY 특성상 대부분 팀이 1~2개라 자동 선택 + 확인 UX면 충분.

### Response
#### `200 OK` (배열)
| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | team_id (**저장 — 채널/웹훅/명령어 생성에 필요**) | `t1a2...` |
| `display_name` | string | 팀 표시 이름 | `Meeting! SSAFY` |

---

# Phase B. MM 초기 세팅 자동화 (온보딩 마법사)

> 이 Phase 전체가 "MM 웹훅 수동 설정 제거"의 구현이다. 순서: B-1 채널 생성 → B-2 팀원 추가 → B-3 웹훅 생성 → B-4 멘션 그룹 생성 → (선택) B-5 슬래시 명령어.

## B-1. 팀 알림 채널 생성

> **참조:** 표준 MM API (`_06-channels` 폴더, 기존 summary에서 권한 오판으로 제외됐던 항목) — 권한 `create_private_channel` ✅ (team_user)

### 기본 정보
- **기능:** SSAGY 알림 전용 채널을 생성한다.
- **Endpoint:** `POST /api/v4/channels`
- **인증:** Bearer Token 필요 `[사용자 토큰]` (연동 수행자)
- **권한:** `create_private_channel` (비공개) / `create_public_channel` (공개)

### 설명
팀 채팅과 알림이 섞이지 않도록 전용 채널(예: `a502-알림`)을 자동 생성한다. 비공개(P) 권장 — 다른 반 교육생에게 노출 방지. 이미 동명 채널이 있으면 400이 오므로 이름에 워크스페이스 키를 섞거나 조회 후 재사용한다.

### Request
#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `team_id` | string | Y | - | A-3에서 확보 | `t1a2...` |
| `name` | string | Y | URL-safe 소문자 | 채널 핸들 | `ssagy-a502-alerts` |
| `display_name` | string | Y | - | 표시 이름 | `A502 알림` |
| `type` | string | Y | `O`(공개)/`P`(비공개) | 비공개 권장 | `P` |

### Response
#### `201 Created`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | string | channel_id (**저장 — 웹훅·멤버 추가에 필요**) |

---

## B-2. 채널에 팀원 추가

> **참조:** 표준 MM API — 권한 `manage_public_channel_members` ✅ / 비공개는 `manage_private_channel_members` ✅ (channel_user)

### 기본 정보
- **기능:** 생성한 알림 채널에 팀원을 추가한다.
- **Endpoint:** `POST /api/v4/channels/{channel_id}/members`
- **인증:** Bearer Token 필요 `[사용자 토큰]` (채널 생성자)
- **권한:** 채널 멤버 관리 권한 (실측 확인됨)

### 설명
MM 연동을 마친 팀원의 mm_user_id를 대상으로 1인당 1회 호출. 아직 MM 연동 전인 팀원은 연동 완료 시점에 자동 추가한다. **타인을 "팀"에 추가하는 권한은 없지만(제외 목록), 이미 같은 팀에 있는 사람을 "채널"에 추가하는 것은 가능** — SSAFY는 전원이 같은 MM 팀 소속이므로 성립한다.

### Request
#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---:|---|
| `channel_id` | string | Y | B-1에서 저장 |

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `user_id` | string | Y | 팀원의 mm_user_id | `9f7x...` |

### Response
#### `201 Created` — 채널 멤버 객체

---

## B-3. Incoming Webhook 생성

> **참조:** `_17-webhooks` (기존 "사용 가능 0개" 판정 폐기) — 권한 `manage_own_incoming_webhooks` ✅ (team_user)

### 기본 정보
- **기능:** 알림 발송용 incoming webhook을 생성한다.
- **Endpoint:** `POST /api/v4/hooks/incoming`
- **인증:** Bearer Token 필요 `[사용자 토큰]` (연동 수행자)
- **권한:** `manage_own_incoming_webhooks`

### 설명
생성된 웹훅 `id`로 발송 URL(`https://meeting.ssafy.com/hooks/{id}`)이 결정된다. `bypass_incoming_webhook_channel_lock` 권한이 있으므로 발송 시 `channel` 필드로 기본 채널 외 다른 채널로도 보낼 수 있다 → **웹훅 1개로 팀 알림 전체 커버 가능**. 생성자만 수정/삭제 가능하므로 생성자 mm_user_id를 함께 저장한다.

### Request
#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `channel_id` | string | Y | 기본 발송 채널 (B-1) | `c3d4...` |
| `display_name` | string | N | 발신자 표시 이름 | `SSAGY` |
| `description` | string | N | 설명 | `SSAGY 통합 알림` |

### Response
#### `201 Created`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | string | webhook key (**암호화 저장** — 발송 URL 자체가 자격증명) |

### 주의 사항
- 목록 조회 `GET /api/v4/hooks/incoming?team_id=`, 삭제 `DELETE /api/v4/hooks/incoming/{hook_id}` — 재연동 시 중복 방지/정리에 사용 (own 한정).

---

## B-4. 커스텀 멘션 그룹 생성 (`@a502`)

> **참조:** `_24-groups` #03 (Create a custom group) — 권한 `create_custom_group` ✅ (system_user)

### 기본 정보
- **기능:** 팀원 전체를 한 번에 멘션할 커스텀 그룹을 생성한다.
- **Endpoint:** `POST /api/v4/groups`
- **인증:** Bearer Token 필요 `[사용자 토큰]`
- **권한:** `create_custom_group` (멤버 갱신은 `manage_custom_group_members`)
- **최소 서버 버전:** 6.3

### 설명
긴급 알림(빌드 실패, 컨플릭트)에 `@a502`를 붙여 채널 알림 설정과 무관하게 팀원 전원에게 멘션이 가도록 한다. `use_group_mentions` 권한(channel_user)으로 발송 메시지에서 사용 가능. `source: "custom"`, `allow_reference: true` 필수. 중복 방지는 `POST /groups/names`(`_24-groups` #26)로 사전 조회.

### Request
#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | 고유, at-mention용 | 멘션 핸들 | `a502` |
| `display_name` | string | Y | - | 표시 이름 | `A502 팀` |
| `source` | string | Y | `custom` 고정 | 그룹 소스 | `custom` |
| `allow_reference` | boolean | Y | `true` 고정 | 멘션 허용 | `true` |
| `user_ids` | string[] | Y | - | MM 연동 완료된 팀원들 | `["9f7x...", ...]` |

### Response
#### `201 Created`

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `501` | source/allow_reference 규칙 위반 | Body 고정값 확인 |

---

## B-5. 슬래시 명령어 등록 (선택)

> **참조:** `_33-integration-actions` 관련 (기존 판정 폐기) + 표준 MM Commands API — 권한 `manage_own_slash_commands` ✅ (team_user)

### 기본 정보
- **기능:** `/ssagy` 커스텀 슬래시 명령어를 팀에 등록한다.
- **Endpoint:** `POST /api/v4/commands`
- **인증:** Bearer Token 필요 `[사용자 토큰]`
- **권한:** `manage_own_slash_commands`

### 설명
`/ssagy mr`, `/ssagy 오늘요약` 같은 채팅 내 질의를 우리 서버로 라우팅한다. MM이 `url`로 POST(트리거한 user_id, channel_id, text 포함) → 우리 서버가 응답 JSON(`response_type: ephemeral|in_channel`, `text`) 반환. Ask-the-Team AI의 MM 진입점으로 활용.

### Request
#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `team_id` | string | Y | 대상 팀 | `t1a2...` |
| `trigger` | string | Y | 명령어 (슬래시 제외) | `ssagy` |
| `method` | string | Y | `P`(POST)/`G`(GET) | `P` |
| `url` | string | Y | 우리 수신 엔드포인트 | `https://api.ssagy.io/mm/commands` |
| `display_name` / `description` / `auto_complete` | - | N | 자동완성 노출 | - |

### Response
#### `201 Created` — `token` 포함 (수신 시 검증용, **저장**)

---

# Phase C. 알림 발송 (런타임)

## C-1. 채널 알림 발송 (주 경로)

> **참조:** incoming webhook 발송 (API v4 밖의 전용 경로)

### 기본 정보
- **기능:** 팀 채널에 알림 메시지를 발송한다.
- **Endpoint:** `POST https://meeting.ssafy.com/hooks/{webhook_key}`
- **인증:** 불필요 (**URL이 자격증명 — 유출 시 재생성**)
- **권한:** 없음

### 설명
모든 팀 단위 알림(MR 생성/승인/컨플릭트, 빌드 실패+AI 요약, 스크럼 리마인더, 주간 리포트)의 발송 경로. 마크다운·attachments 지원. `channel` 필드로 기본 채널 외 발송 가능(bypass 권한 실측 확인). 발송 시점 제어는 전부 우리 스케줄링 엔진이 담당한다.

### Request
#### Headers
| 이름 | 필수 | 설명 |
|---|---:|---|
| `Content-Type` | Y | `application/json` |

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `text` | string | Y | 마크다운 본문 (딥링크 포함) | `🔀 **MR !15 승인 완료** — [머지하러 가기](https://lab.ssafy.com/...)` |
| `channel` | string | N | 발송 채널 override (핸들명) | `ssagy-a502-alerts` |
| `username` / `icon_url` | string | N | 발신자 표시 커스텀 | `SSAGY` |
| `attachments` | array | N | 카드형 리치 메시지 | 색상 바, 필드 테이블 |

### Response
#### `200 OK` — body `ok`

### Errors
| HTTP 상태 | 발생 조건 | 처리 방법 |
|---:|---|---|
| `400` | 잘못된 payload / channel override 불가 | 기본 채널로 재시도 |
| `404` | 웹훅 삭제됨 | 재연동 유도 (B-3 재실행) |

---

## C-2. 개인 DM 알림 발송

> **참조:** `_06-channels` #04 (Create a direct message channel, `create_direct_channel` ✅) + 표준 Posts API (`create_post` ✅ channel_user)

### 기본 정보
- **기능:** 특정 팀원에게 1:1 DM 알림을 보낸다.
- **Endpoint:** ① `POST /api/v4/channels/direct` → ② `POST /api/v4/posts`
- **인증:** Bearer Token 필요 `[사용자 토큰]` (발신자 = 연동 계정)
- **권한:** ① `create_direct_channel` ② `create_post`

### 설명
리뷰 지연 리마인더, "지금 머지 가능" 신호 등 **개인 대상 알림** 전용 (incoming webhook은 채널 귀속이라 DM 불가). ①은 두 user_id 배열로 호출하며 기존 DM 채널이 있으면 그대로 반환(멱등)하므로 매번 호출해도 된다.

### Request
#### ① Body (배열)
```json
["<연동 계정 mm_user_id>", "<수신 팀원 mm_user_id>"]
```
→ 응답의 `id` = DM channel_id

#### ② Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `channel_id` | string | Y | ①의 결과 | `d5e6...` |
| `message` | string | Y | 마크다운 본문 | `⏰ MR !15 리뷰 요청 24시간 경과 — [리뷰하러 가기](...)` |

### Response
#### ② `201 Created` — post 객체

### 주의 사항
- 발신자가 "연동한 팀장 계정"으로 표시됨. 별도 봇 계정 표시가 필요하면 incoming webhook과 달리 커스텀 불가 — 알림 문구에 `[SSAGY]` 프리픽스로 구분.

---

# Phase D. 개인화·AI (사용자 위임 토큰)

## D-1. 팀 미읽음 수 조회

> **참조:** `_05-teams` #29 (Get team unreads for a user) — 권한: 로그인만 ✅

- **Endpoint:** `GET /api/v4/users/me/teams/unread`
- **용도:** 대시보드/사이드뷰에 "MM 안 읽은 메시지 n · 멘션 m" 뱃지. 응답: `[{team_id, msg_count, mention_count}]`

## D-2. 메시지 통합 검색

> **참조:** `_07-posts` #03 (Search posts across all teams) — 권한: 인증만 ✅

- **Endpoint:** `POST /api/v4/posts/search` (Body: `{"terms": "...", "is_or_search": false, "page": 0, "per_page": 20}`)
- **용도:** AI 통합 검색 / Ask-the-Team의 MM 소스. **반드시 질문한 사용자 본인의 위임 토큰으로 호출** — 그 사람이 볼 수 있는 범위만 검색되어 권한 문제가 원천 차단됨.

## D-3. AI 메시지 재작성

> **참조:** `_07-posts` #28 (Rewrite a message using AI) — 권한: 인증만, 서버 11.2+ ⚠️

- **Endpoint:** `POST /api/v4/posts/rewrite` (Body: `agent_id`, `message`, `action: shorten|improve_writing|summarize|custom...`)
- **용도:** "문서 초안 정제" 기획을 MM 내장 AI로 위임하는 선택지. **서버 버전·agent 존재가 전제** — POC에서 미지원이면 우리 LLM 모듈로 대체 (기능 자체는 유지).

## D-4. 채널 알림 설정 / 읽음 처리

> **참조:** `_06-channels` #37 (notify_props), #39 (mark_read), #41 (view) — 권한: 본인 ✅

- **용도:** SSAGY에서 알림 채널의 푸시 수준 조절(`push: mention`), 대시보드 "모두 읽음" 버튼, 딥링크 이동 시 읽음 동기화. 전부 후순위 편의 기능.

---

# 제외 확정 목록 (실효 권한 지도 기준으로도 불가)

| 기능 | 필요한 권한 | 판정 |
|---|---|---|
| MM 팀 생성 | `create_team` | ❌ 세 역할 모두에 없음 — "팀 생성 자동화"는 팀이 아니라 **채널 단위**로 구현 (B-1~B-3) |
| 타인을 팀에 추가 | `add_user_to_team` | ❌ 없음 — SSAFY는 전원이 이미 같은 팀이라 실제로 불필요 |
| 타인 웹훅/명령어 관리 | `manage_others_*` | ❌ own만 가능 — 생성자 고정 운영으로 회피 |
| 타인 계정/설정 조작 | `edit_other_users` | ❌ 없음 — 개인화는 각자 위임 토큰으로 |
| 시스템 콘솔 계열 | `manage_system` | ❌ 없음 |

# POC 검증 체크리스트

1. ✅ ~~incoming/outgoing webhook 생성~~ — UI 실증 완료 (2026-07-20 테스트 훅 존재)
2. `POST /api/v4/hooks/incoming` — **API로도** 생성되는지 (자동화 성립 조건)
3. `POST /hooks/{key}`에 `channel` override — bypass 권한이 실제 동작하는지
4. `POST /api/v4/channels` (P 타입) + `POST /channels/{id}/members` — 채널 자동 생성·초대 왕복
5. `POST /api/v4/commands` — 슬래시 명령어 API 등록 + 콜백 왕복 (outgoing webhook 콜백은 `ssafy.kkh-hub.tech`로 이미 테스트됨)
6. `POST /api/v4/oauth/apps` — OAuth 앱 등록 및 authorization code flow 왕복
7. `GET /api/v4/config/client?format=old` 또는 관리자 문의 — 서버 버전 확인 (`posts/rewrite` 11.2+, `direct/read` 11.3+)
8. `_65-scheduled-post` 재검증 — `create_post` 확보로 예약 발송 가능성 재개 (되면 스케줄링 엔진 부담 경감 옵션)
