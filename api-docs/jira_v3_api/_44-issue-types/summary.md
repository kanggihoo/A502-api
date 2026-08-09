# _44-issue-types API 요약

이 리소스 그룹은 Jira의 이슈 타입(issue type)을 조회/생성/수정/삭제하고, 대체 가능한 이슈 타입을 확인하며 아바타를 설정하는 API를 제공한다. 여기서는 프로젝트 관리자 수준 권한으로 호출 가능한 조회형 API만 채택했다.

## 제외된 API

- `02-create-issue-type-post.md`: 이슈 타입 생성은 *Administer Jira* 전역(글로벌) 권한이 필요한 사이트 전체 관리자 전용 기능이라 제외.
- `05-update-issue-type-put.md`: 이슈 타입 수정은 *Administer Jira* 전역 권한이 필요한 사이트 전체 관리자 전용 기능이라 제외.
- `06-delete-issue-type-delete.md`: 이슈 타입 삭제는 *Administer Jira* 전역 권한이 필요한 사이트 전체 관리자 전용 기능이라 제외.
- `08-load-issue-type-avatar-post.md`: 이슈 타입 아바타 업로드는 *Administer Jira* 전역 권한이 필요한 사이트 전체 관리자 전용 기능이라 제외.

---

### [높음] 1. 사용자의 모든 이슈 타입 조회 (GET /rest/api/3/issuetype)

## 기본 정보

- **기능:** 현재 인증된 사용자(또는 익명 사용자)가 접근 가능한 모든 이슈 타입 목록을 반환한다.
- **Endpoint:** `GET /rest/api/3/issuetype`
- **인증:** 불필요 (익명 접근 가능, 단 결과 범위가 달라짐)
- **권한:** 없음 / *Administer Jira* 전역 권한이 있으면 전체 이슈 타입, 없으면 *Browse projects* 권한이 있는 프로젝트에 연결된 이슈 타입만 반환

## 설명

이 API는 사용자가 볼 수 있는 이슈 타입 전체 목록을 조회한다. *Administer Jira* 전역 권한을 가진 사용자는 인스턴스의 모든 이슈 타입을 받고, 그렇지 않은 사용자는 자신이 *Browse projects* 권한을 가진 프로젝트들에 연결된 이슈 타입만 받는다. 익명 사용자는 익명 접근이 허용된 프로젝트 기준으로 결과가 제한되며, 인증 정보가 잘못된 경우 익명 사용자로 취급된다. 대시보드에서 이슈 타입 아이콘/이름을 표시하거나 필터링 옵션을 구성할 때 사용할 수 있다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| Authorization | 아니오 | Basic 인증(이메일:API 토큰). 생략 시 익명 사용자로 처리 | `Basic base64(email:api_token)` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| avatarId | integer | 이슈 타입 아바타의 ID | `1` |
| description | string | 이슈 타입 설명 | `"A task that needs to be done."` |
| entityId | string | 넥스트젠(팀 관리) 프로젝트용 고유 ID | `"9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2"` |
| hierarchyLevel | integer | 이슈 타입 계층 레벨 | `0` |
| iconUrl | string | 이슈 타입 아바타 URL | `"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype"` |
| id | string | 이슈 타입 ID | `"3"` |
| name | string | 이슈 타입 이름 | `"Task"` |
| scope | object | 넥스트젠 프로젝트 관련 이슈 타입 범위 정보 | `{"project":{"id":"10000"},"type":"PROJECT"}` |
| self | string | 이슈 타입 상세 조회 URL | `"https://your-domain.atlassian.net/rest/api/3/issueType/3"` |
| subtask | boolean | 서브태스크 생성용 이슈 타입 여부 | `false` |

```json
[
  {
    "avatarId": 1,
    "description": "A task that needs to be done.",
    "hierarchyLevel": 0,
    "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype",
    "id": "3",
    "name": "Task",
    "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3",
    "subtask": false
  },
  {
    "avatarId": 10002,
    "description": "A problem with the software.",
    "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2",
    "hierarchyLevel": 0,
    "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype",
    "id": "1",
    "name": "Bug",
    "scope": { "project": { "id": "10000" }, "type": "PROJECT" },
    "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1",
    "subtask": false
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 200 | - | 요청 성공 (결과 범위는 권한에 따라 달라짐) | 응답 배열이 비어있을 수 있으므로 빈 배열 처리 필요 |

## 주의 사항

- 인증 실패 시 오류 없이 익명 사용자로 폴백되므로, 토큰 만료 여부를 별도로 검증해야 한다.
- 반환되는 이슈 타입 범위가 호출자의 권한에 따라 달라지므로, 대시보드에서 "전체 이슈 타입"을 기대하면 안 된다.

---

### [높음] 2. 프로젝트의 이슈 타입 조회 (GET /rest/api/3/issuetype/project)

## 기본 정보

- **기능:** 특정 프로젝트에 연결된 이슈 타입 목록을 반환한다.
- **Endpoint:** `GET /rest/api/3/issuetype/project`
- **인증:** 불필요 (익명 접근 가능)
- **권한:** 해당 프로젝트에 대한 *Browse projects* 권한 또는 *Administer Jira* 전역 권한

## 설명

프로젝트 ID를 기준으로 해당 프로젝트에서 사용 가능한 이슈 타입을 조회한다. `level` 파라미터로 서브태스크(-1), 기본(0), 에픽(1) 등 계층 레벨별 필터링이 가능하다. 팀 생성 자동화 시 프로젝트에 어떤 이슈 타입이 구성되어 있는지 확인하거나, 이슈 생성 폼의 이슈 타입 선택지를 구성할 때 사용한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| projectId | integer | 예 | - | 프로젝트 ID | `10000` |
| level | integer | 아니오 | - | 필터링할 이슈 타입 계층 레벨 (`-1`: 서브태스크, `0`: 기본, `1`: 에픽) | `0` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| avatarId | integer | 이슈 타입 아바타 ID | `10002` |
| description | string | 이슈 타입 설명 | `"A problem with the software."` |
| entityId | string | 넥스트젠 프로젝트용 고유 ID | `"9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2"` |
| hierarchyLevel | integer | 이슈 타입 계층 레벨 | `0` |
| iconUrl | string | 이슈 타입 아바타 URL | `"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype"` |
| id | string | 이슈 타입 ID | `"1"` |
| name | string | 이슈 타입 이름 | `"Bug"` |
| scope | object | 이슈 타입이 속한 프로젝트 범위 | `{"project":{"id":"10000"},"type":"PROJECT"}` |
| self | string | 이슈 타입 상세 조회 URL | `"https://your-domain.atlassian.net/rest/api/3/issueType/1"` |
| subtask | boolean | 서브태스크 이슈 타입 여부 | `false` |

```json
[
  {
    "avatarId": 10002,
    "description": "A problem with the software.",
    "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2",
    "hierarchyLevel": 0,
    "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype",
    "id": "1",
    "name": "Bug",
    "scope": { "project": { "id": "10000" }, "type": "PROJECT" },
    "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1",
    "subtask": false
  },
  {
    "avatarId": 1,
    "description": "A task that needs to be done.",
    "hierarchyLevel": 0,
    "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype",
    "id": "3",
    "name": "Task",
    "scope": { "project": { "id": "10000" }, "type": "PROJECT" },
    "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3",
    "subtask": false
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | `projectId` 값 형식과 존재 여부 확인 |
| 404 | - | 프로젝트를 찾을 수 없거나, 사용자가 필요한 권한이 없음 | `projectId` 확인 및 프로젝트에 대한 Browse 권한 확인 |

## 주의 사항

- `projectId`는 프로젝트 키가 아닌 숫자 ID를 사용해야 한다.
- 프로젝트가 존재해도 권한이 없으면 404로 응답되어 존재 여부를 구분할 수 없다.

---

### [높음] 3. 이슈 타입 단건 조회 (GET /rest/api/3/issuetype/{id})

## 기본 정보

- **기능:** 지정한 ID의 이슈 타입 상세 정보를 반환한다.
- **Endpoint:** `GET /rest/api/3/issuetype/{id}`
- **인증:** 불필요 (익명 접근 가능)
- **권한:** 이슈 타입이 연결된 프로젝트에 대한 *Browse projects* 권한 또는 *Administer Jira* 전역 권한

## 설명

이슈 타입 ID로 이름, 설명, 아바타, 서브태스크 여부 등 상세 정보를 조회한다. 이슈 상세 화면이나 알림/대시보드에서 이슈 타입 ID만 알고 있을 때 이름·아이콘을 함께 표시하기 위해 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| id | string | 예 | 이슈 타입 ID | `"3"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| avatarId | integer | 이슈 타입 아바타 ID | `1` |
| description | string | 이슈 타입 설명 | `"A task that needs to be done."` |
| hierarchyLevel | integer | 이슈 타입 계층 레벨 | `0` |
| iconUrl | string | 이슈 타입 아바타 URL | `"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype"` |
| id | string | 이슈 타입 ID | `"3"` |
| name | string | 이슈 타입 이름 | `"Task"` |
| self | string | 이슈 타입 상세 조회 URL | `"https://your-domain.atlassian.net/rest/api/3/issueType/3"` |
| subtask | boolean | 서브태스크 이슈 타입 여부 | `false` |

```json
{
  "avatarId": 1,
  "description": "A task that needs to be done.",
  "hierarchyLevel": 0,
  "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype",
  "id": "3",
  "name": "Task",
  "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3",
  "subtask": false
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 이슈 타입 ID가 유효하지 않음 | ID 형식 확인 |
| 404 | - | 이슈 타입을 찾을 수 없거나 필요한 권한이 없음 | ID 존재 여부와 권한 확인 |

## 주의 사항

- ID가 존재하지 않는 경우와 권한이 없는 경우 모두 404로 응답되어 클라이언트에서 원인 구분이 어렵다.

---

### [중간] 4. 대체 가능한 이슈 타입 조회 (GET /rest/api/3/issuetype/{id}/alternatives)

## 기본 정보

- **기능:** 지정한 이슈 타입을 대체할 수 있는 다른 이슈 타입 목록을 반환한다.
- **Endpoint:** `GET /rest/api/3/issuetype/{id}/alternatives`
- **인증:** 불필요 (익명 접근 가능)
- **권한:** 없음

## 설명

같은 워크플로우 스킴, 필드 구성 스킴, 화면 스킴에 배정된 대체 가능 이슈 타입 목록을 조회한다. 이슈 타입 삭제 시 대체 이슈 타입을 선택해야 하는 흐름에서 후보 목록을 보여주기 위해 사용할 수 있으나, 이슈 타입 삭제 자체는 관리자 전용이라 이 API는 보조적인 조회 용도로만 활용된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| id | string | 예 | 이슈 타입 ID | `"3"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| avatarId | integer | 이슈 타입 아바타 ID | `1` |
| description | string | 이슈 타입 설명 | `"A task that needs to be done."` |
| hierarchyLevel | integer | 이슈 타입 계층 레벨 | `0` |
| iconUrl | string | 이슈 타입 아바타 URL | `"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype"` |
| id | string | 이슈 타입 ID | `"3"` |
| name | string | 이슈 타입 이름 | `"Task"` |
| self | string | 이슈 타입 상세 조회 URL | `"https://your-domain.atlassian.net/rest/api/3/issueType/3"` |
| subtask | boolean | 서브태스크 이슈 타입 여부 | `false` |

```json
[
  {
    "avatarId": 1,
    "description": "A task that needs to be done.",
    "hierarchyLevel": 0,
    "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype",
    "id": "3",
    "name": "Task",
    "self": "https://your-domain.atlassian.net/rest/api/3/issueType/3",
    "subtask": false
  },
  {
    "avatarId": 10002,
    "description": "A problem with the software.",
    "entityId": "9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2",
    "hierarchyLevel": 0,
    "iconUrl": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype",
    "id": "1",
    "name": "Bug",
    "scope": { "project": { "id": "10000" }, "type": "PROJECT" },
    "self": "https://your-domain.atlassian.net/rest/api/3/issueType/1",
    "subtask": false
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 404 | - | 이슈 타입을 찾을 수 없거나 필요한 권한이 없음 | ID 확인 |

## 주의 사항

- 권한 요구사항이 없어(anonymous 포함) 누구나 호출 가능하지만, 실제 활용도는 이슈 타입 삭제(관리자 전용) 흐름에 종속적이라 보조 기능으로 분류했다.
