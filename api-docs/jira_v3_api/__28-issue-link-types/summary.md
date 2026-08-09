# __28-issue-link-types API 요약

이 리소스 그룹은 Jira의 이슈 링크 타입(issue link type) — 예: "Duplicate", "Blocks" 등 이슈 간 연결 관계의 종류 — 을 조회, 생성, 수정, 삭제하는 API를 제공한다. 사용하려면 사이트에 issue linking 기능이 활성화되어 있어야 한다.

## 제외된 API

- `02-create-issue-link-type-post.md`: 이슈 링크 타입 생성. "Administer Jira" 글로벌(사이트 전체) 권한이 필요하여 제외.
- `04-update-issue-link-type-put.md`: 이슈 링크 타입 수정. "Administer Jira" 글로벌(사이트 전체) 권한이 필요하여 제외.
- `05-delete-issue-link-type-delete.md`: 이슈 링크 타입 삭제. "Administer Jira" 글로벌(사이트 전체) 권한이 필요하여 제외.

---

### [중간] 1. Get issue link types (GET /rest/api/3/issueLinkType)

## 기본 정보

- **기능:** 사이트에 정의된 모든 이슈 링크 타입(예: Duplicate, Blocks 등) 목록을 조회
- **Endpoint:** `GET /rest/api/3/issueLinkType`
- **인증:** 익명 접근 가능 (Anonymous access 허용). 단, 일반적으로는 Bearer Token / Basic Auth 사용
- **권한:** *Browse projects* 프로젝트 권한 (사이트 내 최소 한 프로젝트에 대해)

## 설명

사이트에 설정된 전체 이슈 링크 타입 목록을 반환한다. 각 링크 타입은 이름(name)과 정방향(outward)/역방향(inward) 관계 설명을 포함한다. 이슈 상세 정보나 대시보드에서 링크된 이슈의 관계 종류를 사람이 읽을 수 있는 텍스트로 표시할 때 참조용으로 사용할 수 있다. 사이트에 issue linking 기능이 비활성화되어 있으면 호출할 수 없다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| Authorization | N | 인증된 사용자로 호출 시 필요 (Basic/Bearer) | `Basic base64(email:api_token)` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| issueLinkTypes | array | 이슈 링크 타입 객체 배열 | 아래 예시 참고 |
| issueLinkTypes[].id | string | 링크 타입 ID | `"1000"` |
| issueLinkTypes[].name | string | 링크 타입 이름 | `"Duplicate"` |
| issueLinkTypes[].inward | string | 역방향 관계 설명 | `"Duplicated by"` |
| issueLinkTypes[].outward | string | 정방향 관계 설명 | `"Duplicates"` |
| issueLinkTypes[].self | string | 해당 리소스의 URL | `"https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000"` |

```json
{
  "issueLinkTypes": [
    {
      "id": "1000",
      "inward": "Duplicated by",
      "name": "Duplicate",
      "outward": "Duplicates",
      "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000"
    },
    {
      "id": "1010",
      "inward": "Blocked by",
      "name": "Blocks",
      "outward": "Blocks",
      "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1010"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 올바르지 않음 | 인증 정보 확인 후 재요청 |
| 404 | - | 사이트에 issue linking 기능이 비활성화됨 | Jira 설정에서 issue linking 활성화 여부 확인 |

## 주의 사항

- 익명 접근이 허용되지만, 실제로는 사이트/프로젝트 설정에 따라 달라질 수 있다.
- 응답 결과는 사이트 전역 설정이므로 프로젝트마다 다르지 않고 한 번 캐싱해서 재사용 가능하다.

---

### [중간] 2. Get issue link type (GET /rest/api/3/issueLinkType/{issueLinkTypeId})

## 기본 정보

- **기능:** ID로 특정 이슈 링크 타입 하나를 조회
- **Endpoint:** `GET /rest/api/3/issueLinkType/{issueLinkTypeId}`
- **인증:** 익명 접근 가능 (Anonymous access 허용). 단, 일반적으로는 Bearer Token / Basic Auth 사용
- **권한:** *Browse projects* 프로젝트 권한 (사이트 내 최소 한 프로젝트에 대해)

## 설명

특정 이슈 링크 타입의 상세 정보(이름, inward/outward 설명)를 조회한다. 이슈 링크 목록 화면에서 특정 링크 타입 ID에 대한 표시 텍스트를 확인하거나 유효성을 검증할 때 사용할 수 있다. 사이트에 issue linking 기능이 비활성화되어 있으면 호출할 수 없다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| Authorization | N | 인증된 사용자로 호출 시 필요 (Basic/Bearer) | `Basic base64(email:api_token)` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueLinkTypeId | string | Y | 조회할 이슈 링크 타입의 ID | `"1000"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| id | string | 링크 타입 ID | `"1000"` |
| name | string | 링크 타입 이름 | `"Duplicate"` |
| inward | string | 역방향 관계 설명 | `"Duplicated by"` |
| outward | string | 정방향 관계 설명 | `"Duplicates"` |
| self | string | 해당 리소스의 URL | `"https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000"` |

```json
{
  "id": "1000",
  "inward": "Duplicated by",
  "name": "Duplicate",
  "outward": "Duplicates",
  "self": "https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | issueLinkTypeId 값이 유효하지 않음 | ID 형식/값 확인 |
| 401 | - | 인증 정보가 없거나 올바르지 않음 | 인증 정보 확인 후 재요청 |
| 404 | - | issue linking이 비활성화되었거나, 해당 링크 타입이 없거나, 권한이 없음 | 존재 여부 및 issue linking 설정, 권한 확인 |

## 주의 사항

- 존재하지 않는 ID를 조회해도 400이 아닌 404가 반환될 수 있다 (링크 타입 미존재 케이스).
