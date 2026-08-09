# _71-project-role-actors API 요약

이 리소스 그룹은 특정 프로젝트에 부여된 프로젝트 역할(project role)의 담당자(actor, 사용자/그룹)를 조회·추가·삭제하는 API를 제공한다. 팀 생성 자동화 시 신규 프로젝트에 팀원을 역할별(예: Developers, Administrators)로 배정하는 데 사용할 수 있다.

## 제외된 API

- `04-get-default-actors-for-project-role-get.md`: 프로젝트 역할의 "기본 담당자(default actors)"를 조회하는 API로, `Administer Jira` 전역(글로벌) 권한이 필요하며 프로젝트 관리자 권한으로 대체할 수 있는 경로가 없음. Jira 사이트 전체 관리자만 호출 가능.
- `05-add-default-actors-to-project-role-post.md`: 프로젝트 역할에 "기본 담당자"를 추가하는 API로, `Administer Jira` 전역 권한 필요. 사이트 전체의 역할 템플릿을 변경하는 것으로 SSAFY 교육생(프로젝트 관리자) 계정으로는 호출 불가.
- `06-delete-default-actors-from-project-role-delete.md`: 프로젝트 역할의 "기본 담당자"를 삭제하는 API로, `Administer Jira` 전역 권한 필요. 위와 동일한 사유로 제외.

---

### [높음] 1. Set actors for project role (PUT /rest/api/3/project/{projectIdOrKey}/role/{id})

## 기본 정보

- **기능:** 프로젝트의 특정 프로젝트 역할에 대한 담당자(사용자/그룹) 목록을 전체 교체(덮어쓰기)한다.
- **Endpoint:** `PUT /rest/api/3/project/{projectIdOrKey}/role/{id}`
- **인증:** Bearer Token(또는 Basic/OAuth 등 Jira Cloud 인증) 필요
- **권한:** 해당 프로젝트에 대한 `Administer Projects` 프로젝트 권한 또는 `Administer Jira` 전역 권한

## 설명

해당 프로젝트의 지정된 역할(role id)에 배정된 기존 담당자 전체를 새로운 목록으로 교체한다. 기존 목록을 유지한 채 추가만 하려면 Add actors to project role(POST, 동일 경로) API를 사용해야 한다. 팀 생성 자동화 시 프로젝트를 만든 직후 역할별 담당자를 일괄 세팅하는 용도로 적합하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Yes | 프로젝트 ID 또는 키 (대소문자 구분) | `MKY` |
| `id` | integer | Yes | 프로젝트 역할의 ID. Get all project roles API로 조회 가능 | `10360` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `categorisedActors` | object | - | - | 프로젝트 역할에 추가할 담당자 목록. 그룹은 `atlassian-group-role-actor`(그룹명) 또는 `atlassian-group-role-actor-id`(그룹 ID, 권장) 키로, 사용자는 `atlassian-user-role-actor` 키(계정 ID 목록)로 지정 | `{"atlassian-user-role-actor": ["12345678-9abc-def1-2345-6789abcdef12"]}` |
| `id` | integer | - | - | 프로젝트 역할의 ID | `10360` |

```json
{
  "categorisedActors": {
    "atlassian-group-role-actor-id": ["eef79f81-0b89-4fca-a736-4be531a10869"],
    "atlassian-user-role-actor": ["12345678-9abc-def1-2345-6789abcdef12"]
  },
  "id": 10360
}
```

## Response

### `200 OK`

요청이 성공하면 프로젝트의 전체 담당자 목록이 반환된다.

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `actors` | array | 역할에 배정된 담당자(그룹/사용자) 목록 | 아래 예시 참고 |
| `id` | integer | 프로젝트 역할 ID | `10360` |
| `name` | string | 프로젝트 역할 이름 | `Developers` |
| `description` | string | 역할 설명 | `A project role that represents developers in a project` |
| `scope` | object | 역할이 적용되는 범위(프로젝트) 정보 | `{"project":{"id":"10000","key":"KEY"}}` |
| `self` | string | 리소스 self 링크 | `https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360` |

```json
{
  "actors": [
    {
      "actorGroup": {
        "displayName": "jira-developers",
        "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2",
        "name": "jira-developers"
      },
      "displayName": "jira-developers",
      "id": 10240,
      "name": "jira-developers",
      "type": "atlassian-group-role-actor",
      "user": "jira-developers"
    },
    {
      "actorUser": { "accountId": "5b10a2844c20165700ede21g" },
      "displayName": "Mia Krystof",
      "id": 10241,
      "type": "atlassian-user-role-actor"
    }
  ],
  "description": "A project role that represents developers in a project",
  "id": 10360,
  "name": "Developers",
  "scope": {
    "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" },
    "type": "PROJECT"
  },
  "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 본문의 `categorisedActors`, `id` 형식을 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 호출자가 프로젝트 관리 권한이 없음 | 인증 토큰 및 계정 권한 확인 |
| 404 | - | 프로젝트를 찾을 수 없음 / 사용자나 그룹을 찾을 수 없음 / 그룹·사용자가 비활성 상태임 | `projectIdOrKey`, 사용자·그룹 ID, 활성 상태를 확인 |

## 주의 사항

- 기존 담당자 목록을 전부 덮어쓰므로, 일부만 추가하려면 Add actors to project role(POST) API를 사용해야 한다.
- 그룹명은 변경될 수 있으므로 `atlassian-group-role-actor`보다 `atlassian-group-role-actor-id` 사용을 권장한다.

---

### [높음] 2. Add actors to project role (POST /rest/api/3/project/{projectIdOrKey}/role/{id})

## 기본 정보

- **기능:** 프로젝트의 특정 프로젝트 역할에 담당자(사용자/그룹)를 기존 목록에 추가한다.
- **Endpoint:** `POST /rest/api/3/project/{projectIdOrKey}/role/{id}`
- **인증:** Bearer Token 필요 (익명 접근도 허용되나 실제로는 권한 검증이 필요함)
- **권한:** 해당 프로젝트에 대한 `Administer Projects` 프로젝트 권한 또는 `Administer Jira` 전역 권한

## 설명

프로젝트의 지정된 역할에 사용자 또는 그룹을 추가한다. 기존 담당자 목록은 유지되고 새로운 담당자만 추가된다. 전체 목록을 교체하려면 Set actors for project role(PUT) API를 사용해야 한다. 팀원 초대/합류 시 특정 역할에 개별 사용자를 추가하는 흐름에 적합하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Yes | 프로젝트 ID 또는 키 (대소문자 구분) | `MKY` |
| `id` | integer | Yes | 프로젝트 역할의 ID | `10360` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `group` | string[] | No | `groupId`와 동시 사용 불가 | 추가할 그룹 이름 목록 | `["jira-developers"]` |
| `groupId` | string[] | No | `group`과 동시 사용 불가 | 추가할 그룹 ID 목록 (권장) | `["77f6ab39-e755-4570-a6ae-2d7a8df0bcb8"]` |
| `user` | string[] | No | - | 추가할 사용자 계정 ID 목록 | `["5b10a2844c20165700ede21g"]` |

```json
{
  "group": ["jira-developers"],
  "user": ["5b10a2844c20165700ede21g"]
}
```

## Response

### `200 OK`

요청이 성공하면 프로젝트의 전체 담당자 목록이 반환된다.

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `actors` | array | 역할에 배정된 담당자 목록 | 아래 예시 참고 |
| `id` | integer | 프로젝트 역할 ID | `10360` |
| `name` | string | 프로젝트 역할 이름 | `Developers` |

```json
{
  "actors": [
    {
      "actorGroup": {
        "displayName": "jira-developers",
        "groupId": "952d12c3-5b5b-4d04-bb32-44d383afc4b2",
        "name": "jira-developers"
      },
      "displayName": "jira-developers",
      "id": 10240,
      "name": "jira-developers",
      "type": "atlassian-group-role-actor",
      "user": "jira-developers"
    },
    {
      "actorUser": { "accountId": "5b10a2844c20165700ede21g" },
      "displayName": "Mia Krystof",
      "id": 10241,
      "type": "atlassian-user-role-actor"
    }
  ],
  "description": "A project role that represents developers in a project",
  "id": 10360,
  "name": "Developers",
  "scope": {
    "project": { "id": "10000", "key": "KEY", "name": "Next Gen Project" },
    "type": "PROJECT"
  },
  "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 본문의 `group`/`groupId`/`user` 형식 확인 |
| 401 | - | 인증 정보가 없거나 잘못됨, 또는 호출자가 프로젝트 관리 권한이 없음 | 인증 토큰 및 계정 권한 확인 |
| 404 | - | 프로젝트를 찾을 수 없음 / 사용자나 그룹을 찾을 수 없음 / 그룹·사용자가 비활성 상태임 | `projectIdOrKey`, 사용자·그룹 ID, 활성 상태를 확인 |

## 주의 사항

- `group`과 `groupId`는 동시에 사용할 수 없으며, 그룹명 변경 가능성 때문에 `groupId` 사용이 권장된다.

---

### [높음] 3. Delete actors from project role (DELETE /rest/api/3/project/{projectIdOrKey}/role/{id})

## 기본 정보

- **기능:** 프로젝트의 특정 프로젝트 역할에서 담당자(사용자/그룹)를 제거한다.
- **Endpoint:** `DELETE /rest/api/3/project/{projectIdOrKey}/role/{id}`
- **인증:** Bearer Token 필요 (익명 접근도 허용되나 실제로는 권한 검증이 필요함)
- **권한:** 해당 프로젝트에 대한 `Administer Projects` 프로젝트 권한 또는 `Administer Jira` 전역 권한

## 설명

프로젝트의 지정된 역할에서 사용자 또는 그룹 하나를 제거한다. 쿼리 파라미터로 제거 대상을 지정하며, 프로젝트 역할의 "기본 담당자"를 제거하려면 별도의 Delete default actors from project role API를 사용해야 한다(단, 해당 API는 사이트 전체 관리자 권한이 필요하여 이 요약에서는 제외됨). 팀원 퇴출/역할 변경 시 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Yes | 프로젝트 ID 또는 키 (대소문자 구분) | `MKY` |
| `id` | integer | Yes | 프로젝트 역할의 ID | `10360` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `user` | string | No | - | 제거할 사용자의 계정 ID | `5b10a2844c20165700ede21g` |
| `group` | string | No | - | 제거할 그룹 이름 (`groupId`와 동시 사용 불가) | `jira-developers` |
| `groupId` | string | No | - | 제거할 그룹 ID (`group`과 동시 사용 불가, 권장) | `952d12c3-5b5b-4d04-bb32-44d383afc4b2` |

## Response

### `204 No Content`

요청이 성공하면 별도의 응답 본문 없이 204가 반환된다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 쿼리 파라미터 조합(예: `group`과 `groupId` 동시 사용) 확인 |
| 404 | - | 프로젝트 또는 프로젝트 역할을 찾을 수 없음 / 호출자가 관리자 권한이 없음 | `projectIdOrKey`, `id` 값과 계정 권한 확인 |

## 주의 사항

- `group`과 `groupId`는 동시에 사용할 수 없다.
- 이 API는 프로젝트 범위의 담당자만 제거하며, 역할의 기본(default) 담당자 설정에는 영향을 주지 않는다.
