# _76-projects API 요약

이 리소스 그룹은 Jira 프로젝트(project) 자체를 대상으로 조회/생성/수정/삭제하고, 프로젝트의 상태 목록·이슈 유형 계층·알림 스킴 등 부가 정보를 가져오는 API 모음이다.

## 제외된 API

- 없음. 이 그룹의 모든 엔드포인트는 "Jira administrators only"로 명시되어 있지 않으며, "Administer Jira" 글로벌 권한이 요구되는 경우도 있으나 SSAFY 교육생 계정이 프로젝트 관리자로서 프로젝트 단위로 수행 가능한 범위로 판단하여 제외하지 않았다.

---

### [높음] 1. Create project (POST /rest/api/3/project)

## 기본 정보

- **기능:** 프로젝트 타입 템플릿을 기반으로 새 Jira 프로젝트를 생성한다.
- **Endpoint:** `POST /rest/api/3/project`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** *Administer Jira* 글로벌 권한

## 설명

팀 생성 자동화 흐름에서 SSAFY 팀별 Jira 프로젝트를 자동 생성하는 데 핵심적으로 쓰이는 API다. `projectTypeKey`와 `projectTemplateKey` 조합으로 소프트웨어/비즈니스/서비스데스크 등 프로젝트 유형을 지정하며, `key`, `name`, `leadAccountId`(또는 `lead`) 중 하나는 필수다. 스킴(필드, 이슈타입, 워크플로우, 알림, 권한 등)을 직접 지정하려면 `projectTemplateKey`와 함께 사용할 수 없다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `key` | string | Y | 대문자로 시작, 대문자/숫자 조합, 최대 10자 | 프로젝트 키(고유) | `"EX"` |
| `name` | string | Y | - | 프로젝트 이름 | `"Example"` |
| `projectTypeKey` | enum | N(템플릿 미지정 시 필수) | `software`\|`service_desk`\|`business`\|`customer_service` | 프로젝트 유형 | `"software"` |
| `projectTemplateKey` | enum | N(유형 미지정 시 필수) | 유형과 일치해야 함 | 프로젝트 템플릿 | `"com.pyxis.greenhopper.jira:gh-simplified-agility-scrum"` |
| `leadAccountId` | string | N(`lead`와 택1, 생성 시 하나는 필수) | `lead`와 동시 사용 불가 | 프로젝트 리더의 계정 ID | `"5b10a2844c20165700ede21g"` |
| `lead` | string | N | Deprecated, `leadAccountId`와 동시 사용 불가 | 프로젝트 리더 사용자명(구버전) | - |
| `description` | string | N | - | 프로젝트 설명 | `"팀 프로젝트"` |
| `assigneeType` | enum | N | `PROJECT_LEAD`\|`UNASSIGNED` | 기본 담당자 | `"PROJECT_LEAD"` |
| `avatarId` | integer | N | - | 아바타 ID | `10011` |
| `categoryId` | integer | N | - | 프로젝트 카테고리 ID | `10000` |
| `notificationScheme` | integer | N | - | 알림 스킴 ID | `10100` |
| `permissionScheme` | integer | N | - | 권한 스킴 ID | `10001` |
| `url` | string | N | - | 프로젝트 관련 문서 링크 | `"https://www.example.com"` |

```json
{
  "key": "EX",
  "name": "Example",
  "projectTypeKey": "software",
  "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-agility-scrum",
  "leadAccountId": "5b10a2844c20165700ede21g",
  "description": "SSAFY 팀 프로젝트"
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 생성된 프로젝트 ID | `10010` |
| `key` | string | 프로젝트 키 | `"EX"` |
| `self` | string | 프로젝트 리소스 URL | `"https://your-domain.atlassian.net/jira/rest/api/3/project/10042"` |

```json
{ "id": 10010, "key": "EX", "self": "https://your-domain.atlassian.net/jira/rest/api/3/project/10042" }
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 본문이 유효하지 않아 프로젝트 생성 실패 | 필수 필드 및 템플릿/스킴 조합 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 403 | - | 프로젝트 생성 권한 없음 | 계정이 *Administer Jira* 권한을 갖는지 확인 |

## 주의 사항

- `projectTemplateKey`를 지정하면 `fieldConfigurationScheme`, `fieldScheme`, `issueTypeScheme`, `issueTypeScreenScheme`, `workflowScheme`을 동시에 지정할 수 없다.
- 이 API는 *Administer Jira* 글로벌 권한을 요구하므로, 교육생 계정에 해당 권한이 없다면 SSAFY 관리자에게 사전 위임이 필요할 수 있다.

---

### [높음] 2. Get projects paginated (GET /rest/api/3/project/search)

## 기본 정보

- **기능:** 사용자에게 보이는 프로젝트 목록을 페이지네이션하여 검색/조회한다.
- **Endpoint:** `GET /rest/api/3/project/search`
- **인증:** 익명 접근 가능(단, 결과는 권한에 따라 제한됨)
- **권한:** 프로젝트별 *Browse Projects* 또는 *Administer Projects*, 또는 *Administer Jira* 글로벌 권한

## 설명

`01-get-all-projects`의 대체 API로, 대시보드에서 팀이 접근 가능한 프로젝트 목록을 검색어(`query`)나 키/ID, 상태(`live`/`archived`/`deleted`)로 필터링하여 보여줄 때 사용한다. 정렬(`orderBy`)과 확장 옵션(`expand`)을 지원해 목록 화면 구성에 적합하다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `startAt` | integer | N | - | 페이지 오프셋 | `0` |
| `maxResults` | integer | N | - | 페이지당 최대 개수(최대 100) | `50` |
| `orderBy` | string | N | - | 정렬 기준(`category`,`issueCount`,`key`,`lastIssueUpdatedTime`,`name`,`owner`,`archivedDate`,`deletedDate`) | `"name"` |
| `id` | array | N | - | 프로젝트 ID 필터(최대 50개) | `id=10000&id=10001` |
| `keys` | array | N | - | 프로젝트 키 필터(최대 50개) | `keys=PA&keys=PB` |
| `query` | string | N | - | 키/이름 부분 일치 검색어(대소문자 무시) | `"SSAFY"` |
| `typeKey` | string | N | - | 프로젝트 유형(`business`,`service_desk`,`software`) | `"software"` |
| `categoryId` | integer | N | - | 프로젝트 카테고리 ID | `10000` |
| `action` | string | N | - | 사용자가 가능한 작업 기준 필터(`view`,`browse`,`edit`,`create`) | `"view"` |
| `expand` | string | N | - | 추가 정보 확장(`description`,`projectKeys`,`lead`,`issueTypes`,`url`,`insight`) | `"description,lead"` |
| `status` | array | N | - | 프로젝트 상태 필터(`live`,`archived`,`deleted`) | `"live"` |
| `properties` | array | N | - | 반환할 프로젝트 속성 목록 | - |
| `propertyQuery` | string | N | - | 속성 값 검색 쿼리 | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `false` |
| `maxResults` | integer | 페이지당 결과 수 | `2` |
| `startAt` | integer | 시작 오프셋 | `0` |
| `total` | integer | 전체 결과 수 | `7` |
| `values` | array | 프로젝트 객체 배열(`id`,`key`,`name`,`self` 등) | - |

```json
{
  "isLast": false,
  "maxResults": 2,
  "startAt": 0,
  "total": 7,
  "values": [
    { "id": "10000", "key": "EX", "name": "Example", "self": "https://your-domain.atlassian.net/rest/api/3/project/EX" }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 파라미터가 유효하지 않음 | 쿼리 파라미터 형식 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 404 | - | 검색 조건에 맞는 프로젝트 없음 | 필터 조건 완화 |

## 주의 사항

- `maxResults`는 100을 초과하면 자동으로 100으로 제한된다.
- 대시보드 프로젝트 목록/검색 UI의 기본 데이터 소스로 사용하는 것을 권장한다.

---

### [높음] 3. Get project (GET /rest/api/3/project/{projectIdOrKey})

## 기본 정보

- **기능:** 특정 프로젝트의 상세 정보를 조회한다.
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}`
- **인증:** 익명 접근 가능(단, 결과는 권한에 따라 제한됨)
- **권한:** 프로젝트의 *Browse projects* 권한

## 설명

프로젝트 대시보드나 알림에서 특정 프로젝트의 이름, 리드, 컴포넌트, 이슈 타입, 카테고리 등 상세 정보를 원문 링크와 함께 보여줄 때 사용하는 핵심 조회 API다. `expand`로 설명, 이슈타입, 리드, 이슈타입 계층 등을 추가로 포함시킬 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"EX"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | N | - | 추가 정보 확장(`description`,`issueTypes`,`lead`,`projectKeys`,`issueTypeHierarchy`) | `"lead,issueTypes"` |
| `properties` | array | N | - | 반환할 프로젝트 속성 목록 | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 프로젝트 ID | `"10000"` |
| `key` | string | 프로젝트 키 | `"EX"` |
| `name` | string | 프로젝트 이름 | `"Example"` |
| `description` | string | 프로젝트 설명 | `"This project was created as an example for REST."` |
| `lead` | object | 프로젝트 리드 정보 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `issueTypes` | array | 프로젝트에 연결된 이슈 타입 목록 | - |
| `self` | string | 리소스 URL | `"https://your-domain.atlassian.net/rest/api/3/project/EX"` |

```json
{
  "id": "10000",
  "key": "EX",
  "name": "Example",
  "description": "This project was created as an example for REST.",
  "lead": { "accountId": "5b10a2844c20165700ede21g", "displayName": "Mia Krystof" },
  "self": "https://your-domain.atlassian.net/rest/api/3/project/EX"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 404 | - | 프로젝트가 없거나 조회 권한 없음 | 프로젝트 키/ID 및 권한 확인 |

## 주의 사항

- 응답 기본값에 이미 `description`, `issueTypes`, `lead`가 포함되므로 `expand`는 `projectKeys`, `issueTypeHierarchy` 등 추가 정보에만 필요하다.

---

### [높음] 4. Update project (PUT /rest/api/3/project/{projectIdOrKey})

## 기본 정보

- **기능:** 프로젝트 상세 정보(이름, 설명, 리드, 스킴 등)를 수정한다.
- **Endpoint:** `PUT /rest/api/3/project/{projectIdOrKey}`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** 스킴/키 변경 시 *Administer Jira* 글로벌 권한, 그 외에는 *Administer Projects* 프로젝트 권한

## 설명

팀 생성 자동화 이후 프로젝트 설정(리드 변경, 설명 갱신, 알림/권한 스킴 연결 등)을 자동으로 조정하는 데 사용한다. 요청 본문의 모든 필드는 선택 사항이며, 포함되지 않은 스킴은 변경되지 않는다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"EX"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | N | - | 추가 정보 확장(`description`,`issueTypes`,`lead`,`projectKeys`) | `"lead"` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | N | - | 프로젝트 이름 | `"Example"` |
| `description` | string | N | - | 프로젝트 설명 | `"업데이트된 설명"` |
| `leadAccountId` | string | N | `lead`와 동시 사용 불가 | 프로젝트 리드 계정 ID | `"5b10a2844c20165700ede21g"` |
| `key` | string | N | 대문자 시작, 최대 10자 | 프로젝트 키 변경(Administer Jira 필요) | `"EX2"` |
| `categoryId` | integer | N | `-1`이면 카테고리 해제 | 프로젝트 카테고리 ID | `10000` |
| `notificationScheme` | integer | N | - | 알림 스킴 ID | `10100` |
| `permissionScheme` | integer | N | - | 권한 스킴 ID(무료 플랜에서는 변경 불가) | `10001` |
| `url` | string | N | - | 프로젝트 관련 문서 링크 | `"https://www.example.com"` |

```json
{
  "name": "Example",
  "description": "업데이트된 설명",
  "leadAccountId": "5b10a2844c20165700ede21g"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 프로젝트 ID | `"10000"` |
| `key` | string | 프로젝트 키 | `"EX"` |
| `name` | string | 갱신된 프로젝트 이름 | `"Example"` |
| `self` | string | 리소스 URL | `"https://your-domain.atlassian.net/rest/api/3/project/EX"` |

```json
{ "id": "10000", "key": "EX", "name": "Example", "self": "https://your-domain.atlassian.net/rest/api/3/project/EX" }
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 필드 형식 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 403 | - | 수정 권한 없음 또는 무료 플랜에서 권한 스킴 변경 시도 | 권한 및 플랜 확인 |
| 404 | - | 프로젝트를 찾을 수 없음 | 프로젝트 ID/키 확인 |

## 주의 사항

- 스킴이나 프로젝트 키를 변경하지 않는 일반적인 설정 변경(이름, 설명, 리드 등)은 *Administer Projects* 프로젝트 권한만으로 가능해 교육생(프로젝트 관리자) 계정으로도 처리 가능하다.

---

### [높음] 5. Get all statuses for project (GET /rest/api/3/project/{projectIdOrKey}/statuses)

## 기본 정보

- **기능:** 프로젝트에서 유효한 이슈 상태 목록을 이슈 타입별로 그룹화하여 반환한다.
- **Endpoint:** `GET /rest/api/3/project/{projectIdOrKey}/statuses`
- **인증:** 익명 접근 가능(단, 결과는 권한에 따라 제한됨)
- **권한:** 프로젝트의 *Browse Projects* 권한

## 설명

통합 대시보드에서 이슈 상태 전환 가능 목록을 보여주거나, 특정 이슈 타입에서 사용 가능한 워크플로우 상태를 확인할 때 사용한다. 프로젝트 운영 지원(상태 전환 자동화)의 기반 데이터로 활용된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"EX"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 이슈 타입 ID | `"3"` |
| `name` | string | 이슈 타입 이름 | `"Task"` |
| `statuses` | array | 해당 이슈 타입에서 유효한 상태 목록 | - |
| `statuses[].name` | string | 상태 이름 | `"In Progress"` |

```json
[
  {
    "id": "3",
    "name": "Task",
    "statuses": [
      { "id": "10000", "name": "In Progress", "self": "https://your-domain.atlassian.net/rest/api/3/status/10000" },
      { "id": "5", "name": "Closed", "self": "https://your-domain.atlassian.net/rest/api/3/status/5" }
    ],
    "subtask": false
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 404 | - | 프로젝트가 없거나 조회 권한 없음 | 프로젝트 키/ID 및 권한 확인 |

## 주의 사항

- 결과는 이슈 타입 단위로 그룹화되므로, 상태 전환 UI 구성 시 이슈 타입을 먼저 식별해야 한다.

---

### [중간] 6. Get all projects (GET /rest/api/3/project) [Deprecated]

## 기본 정보

- **기능:** 사용자에게 보이는 모든 프로젝트를 반환한다.
- **Endpoint:** `GET /rest/api/3/project`
- **인증:** 익명 접근 가능(단, 결과는 권한에 따라 제한됨)
- **권한:** 프로젝트의 *Browse Projects* 또는 *Administer projects* 권한

## 설명

페이지네이션과 검색을 지원하지 않는 구버전 API로, Atlassian은 `Get projects paginated`(04) 사용을 권장한다. 소규모 프로젝트 목록을 빠르게 확인하는 보조 용도로만 유용하다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | N | - | 추가 정보 확장(`description`,`issueTypes`,`lead`,`projectKeys`) | `"lead"` |
| `recent` | integer | N | - | 최근 접근한 프로젝트 수(최대 20) | `10` |
| `properties` | array | N | - | 반환할 프로젝트 속성 목록 | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| (배열) | array | 프로젝트 객체 배열(`id`,`key`,`name`,`self` 등) | - |

```json
[
  { "id": "10000", "key": "EX", "name": "Example", "self": "https://your-domain.atlassian.net/rest/api/3/project/EX" }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |

## 주의 사항

- Deprecated API. 신규 구현에는 `Get projects paginated`(04)를 사용할 것.

---

### [중간] 7. Get recent projects (GET /rest/api/3/project/recent)

## 기본 정보

- **기능:** 사용자가 최근에 조회한 프로젝트 최대 20개를 반환한다.
- **Endpoint:** `GET /rest/api/3/project/recent`
- **인증:** 익명 접근 가능(단, 결과는 권한에 따라 제한됨)
- **권한:** 프로젝트의 *Browse Projects*/*Administer Projects* 또는 *Administer Jira* 글로벌 권한

## 설명

대시보드에서 "최근 프로젝트" 위젯을 구성할 때 사용할 수 있는 보조 API다. 핵심 CRUD/알림 흐름에는 직접 필요하지 않지만 UX 개선에 유용하다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | N | - | 추가 정보 확장(`description`,`projectKeys`,`lead`,`issueTypes`,`url`,`permissions`,`insight`,`*`) | `"insight"` |
| `properties` | array | N | - | 반환할 프로젝트 속성 목록 | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| (배열) | array | 최근 조회한 프로젝트 객체 배열 | - |

```json
[
  { "id": "10000", "key": "EX", "name": "Example", "self": "https://your-domain.atlassian.net/rest/api/3/project/EX" }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 파라미터 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |

## 주의 사항

- 익명 접근 시 결과는 현재 HTTP 세션 기준으로 계산된다.

---

### [중간] 8. Delete project (DELETE /rest/api/3/project/{projectIdOrKey})

## 기본 정보

- **기능:** 프로젝트를 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/project/{projectIdOrKey}`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** *Administer Jira* 글로벌 권한

## 설명

프로젝트를 완전히 삭제하는 관리 기능이다. 아카이브된 프로젝트는 삭제할 수 없으며, 먼저 복원 후 삭제해야 한다. 핵심 자동화 흐름보다는 프로젝트 정리/폐기 시 사용되는 보조 기능이다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"EX"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `enableUndo` | boolean | N | - | 삭제 시 휴지통 보관 여부 | `true` |

## Response

### `204 No Content`

삭제 성공 시 본문 없음.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 404 | - | 프로젝트가 없거나 삭제 권한 없음 | 프로젝트 상태 및 권한 확인 |

## 주의 사항

- 아카이브된 프로젝트는 삭제 전 UI를 통한 복원이 필요하다.

---

### [중간] 9. Archive project (POST /rest/api/3/project/{projectIdOrKey}/archive)

## 기본 정보

- **기능:** 프로젝트를 아카이브 처리한다.
- **Endpoint:** `POST /rest/api/3/project/{projectIdOrKey}/archive`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** *Administer Jira* 글로벌 권한

## 설명

더 이상 활성 상태가 아닌 프로젝트를 아카이브하여 목록에서 숨기되 삭제하지는 않는다. 아카이브된 프로젝트는 삭제 전 복원이 필요하다. 프로젝트 생명주기 관리 보조 기능이다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"EX"` |

## Response

### `204 No Content`

아카이브 성공 시 본문 없음.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 프로젝트 상태 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 403 | - | 필요한 권한 없음 | 권한 확인 |
| 404 | - | 프로젝트를 찾을 수 없음 | 프로젝트 ID/키 확인 |

## 주의 사항

- 아카이브된 프로젝트는 즉시 삭제할 수 없다.

---

### [중간] 10. Delete project asynchronously (POST /rest/api/3/project/{projectIdOrKey}/delete)

## 기본 정보

- **기능:** 프로젝트를 비동기적으로 삭제한다.
- **Endpoint:** `POST /rest/api/3/project/{projectIdOrKey}/delete`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** *Administer Jira* 글로벌 권한

## 설명

트랜잭션 방식으로 동작하며(부분 실패 시 삭제되지 않음), 응답의 `location` 링크를 따라가 Task API로 진행 상태를 확인해야 하는 비동기 작업이다. 대규모 프로젝트 삭제 시 사용하는 보조 기능이다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"EX"` |

## Response

### `303 See Other`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 태스크 ID | `"10000"` |
| `status` | enum | 태스크 상태(`ENQUEUED`,`RUNNING`,`COMPLETE`,`FAILED`,`CANCEL_REQUESTED`,`CANCELLED`,`DEAD`) | `"RUNNING"` |
| `progress` | integer | 진행률(%) | `50` |
| `self` | string | 태스크 리소스 URL | `"https://your-domain.atlassian.net/rest/api/3/task/1"` |

```json
{
  "id": "10000",
  "status": "RUNNING",
  "progress": 50,
  "self": "https://your-domain.atlassian.net/rest/api/3/task/1",
  "elapsedRuntime": 1000,
  "lastUpdate": 1610000000000,
  "submitted": 1610000000000,
  "submittedBy": 10000
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 프로젝트 상태 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 404 | - | 프로젝트가 없거나 권한 없음 | 프로젝트 ID/키 및 권한 확인 |

## 주의 사항

- 삭제 완료 여부는 반드시 Task API(Get task)로 폴링하여 확인해야 한다.

---

### [중간] 11. Restore deleted or archived project (POST /rest/api/3/project/{projectIdOrKey}/restore)

## 기본 정보

- **기능:** 삭제(휴지통)되거나 아카이브된 프로젝트를 복원한다.
- **Endpoint:** `POST /rest/api/3/project/{projectIdOrKey}/restore`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** Company-managed 프로젝트는 *Administer Jira* 글로벌 권한, Team-managed 프로젝트는 *Administer Jira* 글로벌 권한 또는 *Administer projects* 프로젝트 권한

## 설명

실수로 삭제/아카이브된 프로젝트를 되돌리는 복구용 보조 기능이다. Team-managed 프로젝트의 경우 프로젝트 관리자 권한만으로도 복원이 가능해 교육생 계정에서도 사용할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectIdOrKey` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"EX"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 프로젝트 ID | `"10000"` |
| `key` | string | 프로젝트 키 | `"EX"` |
| `name` | string | 프로젝트 이름 | `"Example"` |

```json
{ "id": "10000", "key": "EX", "name": "Example", "self": "https://your-domain.atlassian.net/rest/api/3/project/EX" }
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 프로젝트 상태 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 404 | - | 프로젝트가 없거나 권한 없음 | 프로젝트 ID/키 및 권한 확인 |

## 주의 사항

- Team-managed 프로젝트는 프로젝트 관리자 권한으로도 복원 가능하다.

---

### [중간] 12. Get project issue type hierarchy (GET /rest/api/3/project/{projectId}/hierarchy)

## 기본 정보

- **기능:** 넥스트젠(팀 관리형) 프로젝트의 이슈 타입 계층(Epic-Base-Subtask)을 조회한다.
- **Endpoint:** `GET /rest/api/3/project/{projectId}/hierarchy`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** 프로젝트의 *Browse projects* 권한

## 설명

이슈 타입 계층(레벨 1 Epic, 레벨 0 Story/Task/Bug 등, 레벨 -1 Subtask)을 조회하여 대시보드에서 이슈 분류 체계를 표시하거나 하위 작업 자동 생성 로직에 참고할 수 있다. 핵심 CRUD/알림 흐름은 아니지만 백로그/에픽 구조를 이해하는 데 유용하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectId` | integer | Y | 프로젝트 ID | `10030` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `projectId` | integer | 프로젝트 ID | `10030` |
| `hierarchy` | array | 레벨별 이슈 타입 그룹 | - |
| `hierarchy[].level` | integer | 계층 레벨(1=Epic, 0=기본, -1=Subtask) | `0` |
| `hierarchy[].issueTypes` | array | 해당 레벨의 이슈 타입 목록 | - |

```json
{
  "hierarchy": [
    { "issueTypes": [{ "id": 10008, "name": "Story" }, { "id": 10001, "name": "Bug" }], "level": 0, "name": "Base" },
    { "issueTypes": [{ "id": 10007, "name": "Epic" }], "level": 1, "name": "Epic" },
    { "issueTypes": [{ "id": 10009, "name": "Subtask" }], "level": -1, "name": "Subtask" }
  ],
  "projectId": 10030
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | `projectId` 형식 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 404 | - | 프로젝트가 없거나 권한 없음 | 프로젝트 ID 및 권한 확인 |

## 주의 사항

- 넥스트젠(팀 관리형) 프로젝트에만 유효하다.

---

### [중간] 13. Get project notification scheme (GET /rest/api/3/project/{projectKeyOrId}/notificationscheme)

## 기본 정보

- **기능:** 프로젝트에 연결된 알림 스킴을 조회한다.
- **Endpoint:** `GET /rest/api/3/project/{projectKeyOrId}/notificationscheme`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** *Administer Jira* 글로벌 권한 또는 *Administer Projects* 프로젝트 권한

## 설명

어떤 이벤트(이슈 생성, 코멘트 등)에서 누구에게 알림이 가는지 확인할 수 있어, Mattermost 등 외부 채널로의 알림 연동을 설계할 때 기존 Jira 알림 설정과 중복/누락을 점검하는 용도로 유용하다. 핵심 흐름은 아니지만 통합 알림 설계의 참고 자료로 쓰인다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `projectKeyOrId` | string | Y | 프로젝트 ID 또는 키(대소문자 구분) | `"EX"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | N | - | 추가 정보 확장(`all`,`field`,`group`,`notificationSchemeEvents`,`projectRole`,`user`) | `"all"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 알림 스킴 ID | `10100` |
| `name` | string | 알림 스킴 이름 | `"notification scheme name"` |
| `notificationSchemeEvents` | array | 이벤트별 알림 대상 목록 | - |

```json
{
  "id": 10100,
  "name": "notification scheme name",
  "description": "description",
  "notificationSchemeEvents": [
    {
      "event": { "id": 1, "name": "Issue created" },
      "notifications": [
        { "id": 2, "notificationType": "CurrentAssignee" }
      ]
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 파라미터 확인 |
| 401 | - | 인증 정보 누락/오류 | 토큰 재확인 |
| 404 | - | 프로젝트가 없거나 사용자가 관리자가 아님 | 프로젝트 ID/키 및 권한 확인 |

## 주의 사항

- 이 API 자체는 관리자 권한을 요구하지만, 팀 프로젝트 단위(*Administer Projects*)로도 호출 가능하므로 사이트 전체 관리자 권한까지는 필요 없다.
