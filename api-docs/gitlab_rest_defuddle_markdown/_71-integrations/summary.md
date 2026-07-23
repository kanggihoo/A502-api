# Integrations API 명세서 (관리자 권한 미필요 API)

본 문서는 `_71-integrations` 디렉토리 내의 GitLab Integrations (외부 서드파티 서비스: Jira, Mattermost, Jenkins, Slack, Discord, Datadog, GitHub 등 프로젝트 연동 설정 및 관리) 관련 API 중 일반 사용자 및 프로젝트 멤버(Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 168개)

---

## 04. List all active integrations [GET]

### 기본 정보

- **기능:** 프로젝트에 활성화되어 설정된 서드파티 연동(Integration) 서비스 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/integrations`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Maintainer / Owner)

### 설명

프로젝트에서 활성화된 서드파티 통합 서비스(예: `jira`, `mattermost`, `jenkins`, `slack`, `datadog` 등) 목록과 각각의 연동 상태 정보를 조회합니다.

### Request

#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

#### Query parameters
없음

#### Body
없음

### Response

#### `200 OK`
```json
[
  {
    "id": 1,
    "title": "Jira",
    "slug": "jira",
    "created_at": "2026-07-23T10:00:00Z",
    "updated_at": "2026-07-23T10:00:00Z",
    "active": true,
    "commit_events": true,
    "merge_requests_events": true
  },
  {
    "id": 2,
    "title": "Mattermost notifications",
    "slug": "mattermost",
    "active": true
  }
]
```

---

## 26. Create/Edit Jira integration [PUT]

### 기본 정보

- **기능:** 프로젝트의 Atlassian Jira 이슈 트래커 연동 설정을 등록하거나 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/integrations/jira`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### 설명

SSAFY 워크스페이스와 `https://ssafy.atlassian.net/` Jira 간 커밋/MR 키워드 자동 전환 및 이슈 트래킹 연동 설정을 구성합니다.

### Request

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `url` | string | Y | Jira 인스턴스 URL | `https://ssafy.atlassian.net` |
| `username` | string | Y | Jira 계정 이메일 | `user@ssafy.com` |
| `password` | string | Y | Jira API 토큰 | `jira-api-token-xxx` |
| `project_key` | string | N | Jira 프로젝트 키 전용 필터 | `S15P11A502` |

```json
{
  "url": "https://ssafy.atlassian.net",
  "username": "user@ssafy.com",
  "password": "jira-api-token-xxx",
  "project_key": "S15P11A502"
}
```

### Response

#### `200 OK`
```json
{
  "id": 1,
  "title": "Jira",
  "slug": "jira",
  "active": true
}
```

---

## 25. Create/Edit Jenkins integration [PUT]

### 기본 정보

- **기능:** 프로젝트와 Jenkins CI/CD 서버 간 통합 연동 설정을 등록/수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/integrations/jenkins`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### Request

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `jenkins_url` | string | Y | Jenkins 서버 URL (AWS EC2) | `https://jenkins.ssafy.com` |
| `project_name` | string | Y | Jenkins 잡(Job) 이름 | `A502-CI-Job` |
| `username` | string | N | Jenkins 유저명 | `ssafy` |

---

## 43. Create/Edit Mattermost integration [PUT]

### 기본 정보

- **기능:** 프로젝트의 Mattermost 실시간 알림 채널 연동 설정을 구한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/integrations/mattermost`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### Request

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `webhook` | string | Y | Mattermost 수신 Webhook URL | `https://mattermost.ssafy.io/hooks/xxx` |
| `username` | string | N | 메시지 봇 닉네임 | `GitLab Bot` |
| `push_events` | boolean | N | 푸시 이벤트 알림 전송 | `true` |
| `issues_events` | boolean | N | 이슈 이벤트 알림 전송 | `true` |
| `merge_requests_events` | boolean | N | MR 이벤트 알림 전송 | `true` |

---

## 112. Get an integration settings [GET]

### 기본 정보

- **기능:** 프로젝트에 등록된 특정 서드파티 연동 서비스의 상세 구성 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/integrations/{slug}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

---

## 111. Disable an integration [DEL]

### 기본 정보

- **기능:** 프로젝트의 특정 서드파티 연동 서비스를 비활성화 및 설정 해제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/integrations/{slug}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner
