# _96-workflow-statuses API 요약

이 리소스 그룹은 Jira 이슈 워크플로우 상태(status)를 조회하는 API로 구성된다. 활성 워크플로우에 연결된 전체 상태 목록을 가져오거나, 특정 상태 하나를 ID/이름으로 조회할 수 있다.

## 제외된 API

- 제외된 API 없음 (두 엔드포인트 모두 "Browse projects" 프로젝트 권한만 요구하며, 사이트 전체 관리자 권한이 필요하지 않음)

### [높은 우선순위] 1. Get all statuses (GET /rest/api/3/status)

## 기본 정보

- **기능:** 활성 워크플로우에 연결된 모든 이슈 상태(status) 목록을 조회한다.
- **Endpoint:** `GET /rest/api/3/status`
- **인증:** 불필요 (익명 접근 가능, `This operation can be accessed anonymously.`)
- **권한:** 해당 프로젝트에 대한 *Browse projects* 프로젝트 권한

## 설명

이 API는 Jira 사이트 내 활성 워크플로우에 포함된 모든 상태의 목록을 반환한다. 각 상태는 이름, 설명, 아이콘 URL, 그리고 상태 카테고리(진행 전/진행 중/완료) 정보를 포함한다. 통합 대시보드에서 이슈 상태 값을 사람이 읽을 수 있는 이름이나 색상(카테고리)으로 매핑해 보여줄 때 기준 데이터로 활용할 수 있다.

## Request

### Path parameters

_없음_

### Query parameters

_없음_

### Body

_없음 (GET 요청)_

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 상태 ID | `"10000"` |
| `name` | string | 상태 이름 | `"In Progress"` |
| `description` | string | 상태 설명 | `"The issue is currently being worked on."` |
| `iconUrl` | string | 상태 아이콘 URL | `"https://your-domain.atlassian.net/images/icons/progress.gif"` |
| `self` | string | 상태 리소스 URL | `"https://your-domain.atlassian.net/rest/api/3/status/10000"` |
| `statusCategory` | object | 상태 카테고리 정보 (색상, 이름, key 등) | 아래 예시 참고 |

```json
[
  {
    "description": "The issue is currently being worked on.",
    "iconUrl": "https://your-domain.atlassian.net/images/icons/progress.gif",
    "id": "10000",
    "name": "In Progress",
    "self": "https://your-domain.atlassian.net/rest/api/3/status/10000",
    "statusCategory": {
      "colorName": "yellow",
      "id": 1,
      "key": "in-flight",
      "name": "In Progress",
      "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/1"
    }
  },
  {
    "description": "The issue is closed.",
    "iconUrl": "https://your-domain.atlassian.net/images/icons/closed.gif",
    "id": "5",
    "name": "Closed",
    "self": "https://your-domain.atlassian.net/rest/api/3/status/5",
    "statusCategory": {
      "colorName": "green",
      "id": 9,
      "key": "completed",
      "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/9"
    }
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 올바르지 않은 경우 | 인증 토큰/자격 증명을 확인 후 재요청 |

## 주의 사항

- 익명 접근이 허용되지만, 실제 결과는 호출자가 *Browse projects* 권한을 가진 프로젝트의 상태만 포함될 수 있다.
- 활성 워크플로우에 연결되지 않은 상태는 목록에 포함되지 않는다.

---

### [중간 우선순위] 2. Get status (GET /rest/api/3/status/{idOrName})

## 기본 정보

- **기능:** ID 또는 이름으로 특정 상태(status) 하나의 상세 정보를 조회한다.
- **Endpoint:** `GET /rest/api/3/status/{idOrName}`
- **인증:** 불필요 (익명 접근 가능, `This operation can be accessed anonymously.`)
- **권한:** 해당 프로젝트에 대한 *Browse projects* 프로젝트 권한

## 설명

지정한 ID 또는 이름에 해당하는 상태 하나를 반환한다. 해당 상태는 활성 워크플로우에 연결되어 있어야 조회된다. 이름이 여러 상태에서 중복 사용되는 경우 가장 먼저 찾은 상태만 반환되므로, 이름보다는 ID로 조회하는 것이 더 정확하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `idOrName` | string | Y | 조회할 상태의 ID 또는 이름 | `"10000"` |

### Query parameters

_없음_

### Body

_없음 (GET 요청)_

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 상태 ID | `"10000"` |
| `name` | string | 상태 이름 | `"In Progress"` |
| `description` | string | 상태 설명 | `"The issue is currently being worked on."` |
| `iconUrl` | string | 상태 아이콘 URL | `"https://your-domain.atlassian.net/images/icons/progress.gif"` |
| `self` | string | 상태 리소스 URL | `"https://your-domain.atlassian.net/rest/api/3/status/10000"` |
| `statusCategory` | object | 상태 카테고리 정보 (색상, 이름, key 등) | 아래 예시 참고 |

```json
{
  "description": "The issue is currently being worked on.",
  "iconUrl": "https://your-domain.atlassian.net/images/icons/progress.gif",
  "id": "10000",
  "name": "In Progress",
  "self": "https://your-domain.atlassian.net/rest/api/3/status/10000",
  "statusCategory": {
    "colorName": "yellow",
    "id": 1,
    "key": "in-flight",
    "name": "In Progress",
    "self": "https://your-domain.atlassian.net/rest/api/3/statuscategory/1"
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 올바르지 않은 경우 | 인증 토큰/자격 증명을 확인 후 재요청 |
| 404 | - | 상태를 찾을 수 없음 / 상태가 워크플로우에 연결되지 않음 / 사용자가 필요한 권한을 가지고 있지 않음 | `idOrName` 값 확인 및 권한 확인 |

## 주의 사항

- 이름으로 조회 시 동일 이름의 상태가 여러 개면 먼저 찾은 것만 반환되므로, 가능하면 ID로 조회하는 것을 권장한다.
- 활성 워크플로우에 연결되지 않은 상태는 404로 처리된다.
