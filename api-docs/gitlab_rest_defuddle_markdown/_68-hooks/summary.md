# Webhooks & Hooks API 명세서 (관리자 권한 미필요 API)

본 문서는 `_68-hooks` 디렉토리 내의 GitLab Webhooks & Hooks (그룹 웹훅 및 프로젝트 웹훅 등록, 이벤트 설정, 커스텀 헤더, 비밀 URL 변수, 웹훅 테스트 및 재전송) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버(Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 24개)



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
