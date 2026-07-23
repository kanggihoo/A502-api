# Webhooks & Hooks API 명세서 (관리자 권한 미필요 API)

본 문서는 `_68-hooks` 디렉토리 내의 GitLab Webhooks & Hooks (그룹 웹훅 및 프로젝트 웹훅 등록, 이벤트 설정, 커스텀 헤더, 비밀 URL 변수, 웹훅 테스트 및 재전송) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버(Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 24개)

> **관리자(Admin) 전용 API 제외 목록 (10개)**
> - `17~26번`: GitLab 인스턴스 전역 시스템 훅(System Hooks) CRUD, URL 변수 및 커스텀 헤더 관리 (`/api/v4/hooks...` - Admin 전용)

---

## 01 ~ 05. Group Webhooks Management (GET, POST, GET, PUT, DEL)

### 기본 정보

- **기능:** 그룹 레벨의 웹훅(Group Webhook)을 생성, 조회, 수정 및 삭제한다.
- **Endpoint:** `POST /api/v4/groups/{id}/hooks`
- **인증:** Bearer Token 필요
- **권한:** 그룹 Maintainer / Owner

### 설명

그룹 산하의 모든 프로젝트에서 발생하는 이벤트(push, issue, merge_request, pipeline, job, wiki 등)를 수신할 HTTP Webhook URL을 등록합니다. SSAFY 팀의 Mattermost 전용 채널 자동 연동 및 팀 워크스페이스 구축 시 필수적으로 활용됩니다.

### Request

#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 URL 인코딩 경로 | `s15p11a502` |

#### Body (생성 기준)
| 필드 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `url` | string | Y | - | 웹훅 페이로드를 수신할 HTTP/HTTPS Endpoint URL | `https://mattermost.ssafy.io/hooks/xxx` |
| `push_events` | boolean | N | `true` | 푸시 이벤트 발생 시 웹훅 전송 여부 | `true` |
| `issues_events` | boolean | N | `false` | 이슈 생성/변경 시 웹훅 전송 여부 | `true` |
| `merge_requests_events` | boolean | N | `false` | MR 이벤트 발생 시 웹훅 전송 여부 | `true` |
| `pipeline_events` | boolean | N | `false` | CI 파이프라인 상태 변경 시 웹훅 전송 여부 | `true` |
| `token` | string | N | - | 웹훅 검증용 비밀 토큰 (`X-Gitlab-Token` 헤더 전송) | `my-secret-token` |
| `enable_ssl_verification` | boolean | N | `true` | SSL 인증서 검증 여부 | `true` |

```json
{
  "url": "https://mattermost.ssafy.io/hooks/sample-webhook-token",
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "pipeline_events": true,
  "enable_ssl_verification": true
}
```

### Response

#### `201 Created`
```json
{
  "id": 50,
  "url": "https://mattermost.ssafy.io/hooks/sample-webhook-token",
  "group_id": 105,
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "pipeline_events": true,
  "enable_ssl_verification": true,
  "created_at": "2026-07-23T10:00:00Z"
}
```

---

## 06~10, 13~16. Group Webhook Extended Configuration (Events, Secret Vars, Custom Headers, Test, Resend)

- **Endpoints:**
  - `GET /api/v4/groups/{id}/hooks/{hook_id}/events`: 그룹 웹훅의 최근 전송 이벤트 내역 목록 조회
  - `PUT/DELETE /api/v4/groups/{id}/hooks/{hook_id}/url_variables/{key}`: 웹훅 URL 비밀 변수 등록 및 삭제
  - `PUT/DELETE /api/v4/groups/{id}/hooks/{hook_id}/custom_headers/{key}`: 웹훅 요청 전송 시 포함할 커스텀 HTTP 헤더 추가/삭제
  - `POST /api/v4/groups/{id}/hooks/{hook_id}/test/{trigger}`: 테스트 웹훅 이벤트 강제 발생 (`push_events`, `issues_events`, `merge_requests_events` 등)
  - `POST /api/v4/groups/{id}/hooks/{hook_id}/events/{event_id}/resend`: 과거 실패했거나 누락된 웹훅 이벤트 재전송

---

## 27 ~ 31. Project Webhooks Management (GET, POST, GET, PUT, DEL)

### 기본 정보

- **기능:** 단일 프로젝트 레벨의 웹훅(Project Webhook)을 생성, 조회, 수정 및 삭제한다.
- **Endpoint:** `POST /api/v4/projects/{id}/hooks`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### 설명

특정 프로젝트 저장소에 좁은 범위로 적용되는 웹훅 엔드포인트를 등록하고 이벤트(Push, Issue, MR, Pipeline, Job, Tag Push, Wiki 등) 구독 옵션을 구성합니다.

### Request

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

#### Body
```json
{
  "url": "https://api.ssafy.io/v1/gitlab/webhooks",
  "push_events": true,
  "merge_requests_events": true,
  "job_events": true
}
```

### Response

#### `201 Created`
```json
{
  "id": 101,
  "url": "https://api.ssafy.io/v1/gitlab/webhooks",
  "project_id": 1234,
  "push_events": true,
  "merge_requests_events": true
}
```

---

## 32 ~ 34. Project Webhook Testing & Log (GET Events, POST Test, POST Resend)

- **Endpoints:**
  - `GET /api/v4/projects/{id}/hooks/{hook_id}/events`: 프로젝트 웹훅 전송 이벤트 록 조회
  - `POST /api/v4/projects/{id}/hooks/{hook_id}/test/{trigger}`: 프로젝트 테스트 웹훅 실행
  - `POST /api/v4/projects/{id}/hooks/{hook_id}/events/{event_id}/resend`: 프로젝트 웹훅 이벤트 재전송
