# _72-project-roles API 요약

이 리소스 그룹은 프로젝트에서 사용자가 맡을 수 있는 "역할(Project Role)"을 조회·생성·수정·삭제하는 Jira REST API 엔드포인트 모음이다. 프로젝트 단위로 역할에 소속된 사용자/그룹(액터)을 확인할 수 있어 통합 대시보드에서 담당자·구성원 정보를 보여주는 데 활용할 수 있다.

## 제외된 API

- `04-get-all-project-roles-get.md`: 사이트 전체의 모든 프로젝트 역할과 기본 액터를 조회하며, "Administer Jira" 사이트 전체(글로벌) 관리자 권한만 허용되고 프로젝트 관리자 권한으로는 접근 불가.
- `05-create-project-role-post.md`: 새 프로젝트 역할 생성. "Administer Jira" 글로벌 관리자 권한 필요.
- `06-get-project-role-by-id-get.md`: 역할 ID로 전역 역할 상세(기본 액터 포함) 조회. "Administer Jira" 글로벌 관리자 권한 필요.
- `07-fully-update-project-role-put.md`: 역할 이름/설명 전체 수정. "Administer Jira" 글로벌 관리자 권한 필요.
- `08-partial-update-project-role-post.md`: 역할 이름 또는 설명 부분 수정. "Administer Jira" 글로벌 관리자 권한 필요.
- `09-delete-project-role-delete.md`: 프로젝트 역할 삭제. "Administer Jira" 글로벌 관리자 권한 필요.

---

### [높은 우선순위] 1. 프로젝트의 역할 목록 조회 (GET /rest/api/3/project/{projectIdOrKey}/role)

## 기본 정보

- **기능:** 특정 프로젝트에 존재하는 프로젝트 역할들의 이름과 self URL 목록을 반환
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}/role`
- **인증:** Bearer Token(또는 Basic Auth) 필요 (단, 익명 접근도 허용될 수 있음)
- **권한:** 해당 프로젝트에 대한 *Administer Projects* 프로젝트 권한 또는 사이트 전체 *Administer Jira* 글로벌 권한

## 설명

프로젝트에 정의된 역할(Administrators, Developers, Users 등)의 이름과 상세 조회용 self URL을 반환한다. Jira Cloud에서는 역할 자체가 전체 프로젝트에 공유되므로, 이 API는 특정 프로젝트에서 어떤 역할이 활성화되어 있는지 확인하는 용도로 쓰인다. 역할별 실제 구성원(액터) 목록은 반환하지 않으며, 이는 `02` API에서 개별 조회해야 한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | `string` | Yes | 프로젝트 ID 또는 프로젝트 키 (대소문자 구분) | `MKY` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| (역할 이름) | `string` | 역할명을 키로 하고 값은 해당 역할의 self URL | `"Administrators": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10002"` |

```json
{
  "Administrators": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10002",
  "Developers": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10000",
  "Users": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10001"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 잘못되었거나 없음, 또는 프로젝트에 대한 관리자 권한이 없음 | 인증 토큰 및 권한 확인 |
| 404 | - | 프로젝트를 찾을 수 없거나 사용자가 해당 프로젝트에 대한 관리자 권한이 없음 | 프로젝트 키/ID 재확인 |

## 주의 사항

- 반환되는 것은 역할명과 URL뿐이며, 역할에 속한 실제 사용자/그룹 목록은 포함되지 않는다.
- Jira Cloud에서 프로젝트 역할 자체는 전역 공유 리소스이므로, 이 API는 "이 프로젝트에서 사용 가능한 역할이 무엇인지"를 확인하는 용도다.

---

### [높은 우선순위] 2. 프로젝트의 특정 역할 상세(구성원 포함) 조회 (GET /rest/api/3/project/{projectIdOrKey}/role/{id})

## 기본 정보

- **기능:** 특정 프로젝트의 특정 역할에 대한 상세 정보와 소속 액터(사용자/그룹) 목록을 반환
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}/role/{id}`
- **인증:** Bearer Token(또는 Basic Auth) 필요 (단, 익명 접근도 허용될 수 있음)
- **권한:** 해당 프로젝트에 대한 *Administer Projects* 프로젝트 권한 또는 사이트 전체 *Administer Jira* 글로벌 권한

## 설명

프로젝트 역할 하나에 대해 설명, 범위(scope), 그리고 실제로 배정된 액터(사용자 또는 그룹) 목록을 표시 이름 순으로 정렬하여 반환한다. 사용자가 그룹 멤버십을 통해 특정 역할에 속하는지 확인하려면 `Get user` API의 `groups` expand와 결과를 비교해야 한다. 팀 채널의 담당자/구성원 정보를 대시보드에 표시하거나 알림 수신 대상을 판단하는 데 유용하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | `string` | Yes | 프로젝트 ID 또는 프로젝트 키 (대소문자 구분) | `MKY` |
| `id` | `integer` | Yes | 프로젝트 역할의 ID | `10360` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `excludeInactiveUsers` | `boolean` | No | - | 비활성 사용자를 결과에서 제외할지 여부 | `true` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | `integer` | 역할 ID | `10360` |
| `name` | `string` | 역할 이름 | `"Developers"` |
| `description` | `string` | 역할 설명 | `"A project role that represents developers in a project"` |
| `actors` | `array` | 역할에 소속된 사용자/그룹 액터 목록 | 아래 예시 참고 |
| `scope` | `object` | 역할이 적용되는 프로젝트 범위 정보 | `{"project": {...}, "type": "PROJECT"}` |
| `self` | `string` | 역할 상세 조회 URL | `"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360"` |

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
| 400 | - | 요청이 유효하지 않음 | 요청 파라미터 확인 |
| 401 | - | 인증 정보가 잘못되었거나 없음 | 인증 토큰 확인 |
| 404 | - | 프로젝트 또는 역할을 찾을 수 없거나, 관리자 권한 없음 | 프로젝트/역할 ID 재확인, 권한 확인 |

## 주의 사항

- 그룹 기반 액터(`atlassian-group-role-actor`)와 사용자 기반 액터(`atlassian-user-role-actor`)가 혼재할 수 있으므로 파싱 시 타입을 구분해야 한다.
- `excludeInactiveUsers=true`로 조회하면 결과에서 비활성 사용자를 제외할 수 있어, 알림 대상 필터링에 활용 가능하다.

---

### [중간 우선순위] 3. 프로젝트의 전체 역할 상세 목록 조회 (GET /rest/api/3/project/{projectIdOrKey}/roledetails)

## 기본 정보

- **기능:** 프로젝트에 존재하는 모든 프로젝트 역할과 각 역할의 상세 정보(설명, 기본 여부, 관리자 여부 등)를 한 번에 반환
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}/roledetails`
- **인증:** Bearer Token(또는 Basic Auth) 필요 (단, 익명 접근도 허용될 수 있음)
- **권한:** 사이트 전체 *Administer Jira* 글로벌 권한 또는 해당 프로젝트에 대한 *Administer projects* 프로젝트 권한

## 설명

`01` API와 달리 역할별 액터 목록은 포함하지 않지만, 각 역할의 설명(description), 관리자 역할 여부(admin), 기본 역할 여부(default), 역할 설정 가능 여부(roleConfigurable), 타입(type) 등 메타데이터를 한 번의 호출로 모두 가져올 수 있다. `currentMember` 쿼리 파라미터로 현재 사용자가 속한 역할만 필터링할 수도 있어, 로그인한 사용자 기준 개인화된 뷰 구성에 유용하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | `string` | Yes | 프로젝트 ID 또는 프로젝트 키 (대소문자 구분) | `MKY` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `currentMember` | `boolean` | No | - | 현재 사용자가 속한 역할만 필터링할지 여부 | `true` |
| `excludeConnectAddons` | `boolean` | No | - | (설명 없음) | `true` |
| `excludeOtherServiceRoles` | `boolean` | No | - | CSM/JSM 관련 기본 역할을 결과에서 제외할지 여부 | `true` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `self` | `string` | 역할 상세 조회 URL | `"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360"` |
| `name` | `string` | 역할 이름 | `"Developers"` |
| `id` | `integer` | 역할 ID | `10360` |
| `description` | `string` | 역할 설명 | `"A project role that represents developers in a project"` |
| `admin` | `boolean` | 관리자 역할 여부 | `false` |
| `default` | `boolean` | 기본 역할 여부 | `true` |
| `roleConfigurable` | `boolean` | 역할 설정 가능 여부 | `true` |
| `translatedName` | `string` | 번역된 역할 이름 | `"Developers"` |
| `type` | `string` | 역할 타입 | `"DEFAULT"` |

```json
[
  {
    "self": "https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360",
    "name": "Developers",
    "id": 10360,
    "description": "A project role that represents developers in a project",
    "admin": false,
    "default": true,
    "roleConfigurable": true,
    "translatedName": "Developers",
    "type": "DEFAULT"
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 잘못되었거나 없음 | 인증 토큰 확인 |
| 404 | - | 프로젝트를 찾을 수 없거나 필요한 권한이 없음 | 프로젝트 키/ID 및 권한 확인 |

## 주의 사항

- 역할별 실제 구성원(액터) 목록은 포함되지 않으므로, 구성원까지 필요하면 `02` API를 함께 사용해야 한다.
- 프로젝트 역할 목록 자체는 모든 프로젝트에 공통이지만, 이 API는 프로젝트 컨텍스트에서 각 역할의 메타데이터(관리자/기본 여부 등)를 확인하는 데 특화되어 있다.
