# Events API 명세서 (관리자 권한 미필요 API)

본 문서는 `_52-events` 디렉토리 내의 GitLab Events (프로젝트, 사용자 및 전체 접근 가능 이벤트 활동 이력 조회) 관련 API 중 일반 사용자 및 프로젝트 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 3개)

---

## 01. List all visible events for a project [GET]

### 기본 정보

- **기능:** 특정 프로젝트에서 발생한 전체 이벤트(커밋, 이슈, MR 생성/상태변경 등) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/events`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

지정한 프로젝트 내부에서 발생한 각종 활동 이벤트(푸시, 이슈 생성/닫기, 머지 리퀘스트 생성/머지, 댓글 등) 이력을 가져옵니다. `action` 파라미터를 사용하여 `created`, `updated`, `closed`, `reopened`, `pushed`, `commented`, `merged` 등의 특정 활동 유형만 필터링할 수 있으며, `target_type`으로 `issue`, `milestone`, `merge_request`, `note`, `project`, `snippet`, `user` 별로 구분하여 조회할 수 있습니다.

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

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `action` | string | N | - | 이벤트 액션 종류 (`created` \| `updated` \| `closed` \| `reopened` \| `pushed` \| `commented` \| `merged` \| `joined` \| `left` \| `destroyed` \| `expired`) | `pushed` |
| `target_type` | string | N | - | 이벤트 대상 유형 (`issue` \| `milestone` \| `merge_request` \| `note` \| `project` \| `snippet` \| `user`) | `issue` |
| `before` | string | N | - | 이 시각 이전 이벤트만 조회 (YYYY-MM-DD) | `2026-07-01` |
| `after` | string | N | - | 이 시각 이후 이벤트만 조회 (YYYY-MM-DD) | `2026-07-23` |
| `sort` | string | N | `desc` | 정렬 방식 (`asc` \| `desc`) | `desc` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 이벤트 ID | `1001` |
| `title` | string | 이벤트 관련 제목 | null 또는 커밋 제목 |
| `project_id` | integer | 프로젝트 ID | `1234` |
| `action_name` | string | 실행된 액션 이름 | `pushed to` |
| `target_type` | string | 대상 유형 | null 또는 `Issue` |
| `author_username` | string | 이벤트 발생 유저 아이디 | `kkh_ssafy` |
| `push_data` | object | 푸시 이벤트 시 상세 커밋 수, 브랜치명 객체 | `{ "commit_count": 1, "ref": "main" }` |

```json
[
  {
    "id": 1001,
    "project_id": 1234,
    "action_name": "pushed to",
    "target_id": null,
    "target_type": null,
    "author_id": 12,
    "target_title": null,
    "created_at": "2026-07-23T10:00:00Z",
    "author": {
      "id": 12,
      "username": "kkh_ssafy",
      "name": "강기후"
    },
    "push_data": {
      "commit_count": 1,
      "action": "pushed",
      "ref_type": "branch",
      "commit_from": "a1b2c3...",
      "commit_to": "d4e5f6...",
      "ref": "main"
    },
    "author_username": "kkh_ssafy"
  }
]
```

---

## 02. List all events [GET]

### 기본 정보

- **기능:** 인증된 사용자가 접근 가능한 모든 프로젝트의 통합 이벤트 목록을 조회한다.
- **Endpoint:** `GET /api/v4/events`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자

### 설명

현재 로그인한 사용자가 접근 권한을 가지고 있는 인스턴스 내 전체 프로젝트에서 발생하는 타임라인 이벤트를 통합 조회합니다. SSAFY 워크스페이스 대시보드 실시간 타임라인 피드 구현 시 주로 사용됩니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

없음

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `action` | string | N | - | 이벤트 액션 종류 | `commented` |
| `target_type` | string | N | - | 이벤트 대상 유형 | `merge_request` |
| `before` | string | N | - | 이전 날짜 필터 (YYYY-MM-DD) | `2026-07-23` |
| `after` | string | N | - | 이후 날짜 필터 (YYYY-MM-DD) | `2026-07-01` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

```json
[
  {
    "id": 1002,
    "project_id": 1234,
    "action_name": "commented on",
    "target_type": "Note",
    "author_username": "kkh_ssafy",
    "created_at": "2026-07-23T10:05:00Z"
  }
]
```

---

## 03. Retrieve contribution events for a user [GET]

### 기본 정보

- **기능:** 특정 사용자가 수행한 기여(Contribution) 이벤트 이력을 조회한다.
- **Endpoint:** `GET /api/v4/users/{id}/events`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자

### 설명

지정한 사용자의 프로필 타임라인 잔디 그래프 및 기여 활동 내역(커밋 푸시, 이슈 생성, MR 오픈 및 머지 등)을 가져옵니다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | integer | Y | 대상 사용자 ID | `12` |

#### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `action` | string | N | 액션 필터 | `pushed` |
| `target_type` | string | N | 대상 유형 필터 | `issue` |

### Response

#### `200 OK`

```json
[
  {
    "id": 1003,
    "action_name": "closed",
    "target_type": "Issue",
    "author_username": "kkh_ssafy",
    "created_at": "2026-07-23T10:10:00Z"
  }
]
```
