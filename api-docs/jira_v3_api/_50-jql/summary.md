# _50-jql API 요약

이 리소스 그룹(JQL)은 JQL 검색을 위한 필드 참조 데이터/자동완성 제안 조회, JQL 쿼리 파싱·검증, 사용자 식별자 변환 등 JQL 쿼리를 프로그래밍 방식으로 생성·검증하는 기능을 제공한다.

## 제외된 API

- `06-sanitize-jql-queries-post.md`: "Administer Jira" 글로벌 권한(Jira 사이트 전체 시스템 관리자 권한)이 필요한 API. SSAFY 교육생 계정(프로젝트 관리자 수준)으로는 호출이 불가능할 가능성이 높아 제외.

---

### [높음] 1. Parse JQL query (POST /rest/api/3/jql/parse)

## 기본 정보

- **기능:** JQL 쿼리 목록을 파싱하고 검증한다.
- **Endpoint:** `POST /rest/api/3/jql/parse`
- **인증:** 익명 접근 가능 (Bearer Token/Basic Auth 불필요)
- **권한:** 없음 (검증은 현재 사용자 컨텍스트에서 수행됨)

## 설명

JQL 쿼리 문자열들을 서버 측에서 파싱하여 문법 오류, 필드/연산자 사용 오류, 존재하지 않는 값 등을 검증하고, 검증에 성공하면 쿼리의 구조(structure)를 반환한다. 통합 알림/대시보드에서 사용자가 입력한 검색 조건이나 자동 생성된 JQL을 실제 검색에 사용하기 전에 유효성을 검증하는 용도로 활용할 수 있다. 검증 결과 처리 방식(`strict`/`warn`/`none`)에 따라 오류 발생 시 구조 반환 여부가 달라진다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `validation` | string | 예 | - | JQL 쿼리 검증 방식과 결과 처리 방법. `strict`: 오류 전체 반환, 실패 시 쿼리 구조 미반환. `warn`: 오류 전체 반환, 쿼리 형식이 올바르면 구조도 반환. `none`: 검증 없이 형식이 올바르면 구조 반환. | `strict` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `queries` | string[] | 예 | - | 파싱할 쿼리 목록 | `["summary ~ test AND (labels in (urgent, blocker) OR lastCommentedBy = currentUser()) AND status CHANGED AFTER -5d ORDER BY updated DESC"]` |

```json
{
  "queries": [
    "summary ~ test AND (labels in (urgent, blocker) OR lastCommentedBy = currentUser()) AND status CHANGED AFTER -5d ORDER BY updated DESC"
  ]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `queries` | array | 각 쿼리의 파싱 결과(구조, 오류, 경고 등)를 순서대로 포함 | 아래 예시 참고 |

```json
{
  "queries": [
    {
      "query": "summary ~ test AND (labels in (urgent, blocker) OR lastCommentedBy = currentUser()) AND status CHANGED AFTER -5d ORDER BY updated DESC",
      "structure": {
        "orderBy": {
          "fields": [
            { "direction": "desc", "field": { "encodedName": "updated", "name": "updated" } }
          ]
        },
        "where": {
          "clauses": [
            {
              "field": { "encodedName": "summary", "name": "summary" },
              "operand": { "encodedValue": "test", "value": "test" },
              "operator": "~"
            }
          ],
          "operator": "and"
        }
      }
    },
    {
      "errors": ["Error in the JQL Query: Expecting operator but got 'query'. The valid operators are '=', '!=', '<', '>', '<=', '>=', '~', '!~', 'IN', 'NOT IN', 'IS' and 'IS NOT'. (line 1, character 9)"],
      "query": "invalid query"
    },
    {
      "query": "project = INVALID",
      "warnings": ["The value 'INVALID' does not exist for the field 'project'."]
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 (예: `queries` 누락) | 요청 본문/파라미터 확인 후 재요청 |
| 401 | - | 인증 자격 증명이 올바르지 않음 | 인증 토큰 확인 |

```json
{
  "errorMessages": ["input parameter 'key' must be provided"],
  "errors": {
    "projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  },
  "status": 400
}
```

## 주의 사항

- 개별 쿼리 단위로 오류/경고가 반환되므로, 응답의 `queries` 배열 순서가 요청 순서와 동일함을 이용해 결과를 매핑해야 한다.
- `strict` 검증에서 오류가 있으면 해당 쿼리의 `structure`는 반환되지 않는다.

---

### [중간] 2. Get field reference data (GET) (GET /rest/api/3/jql/autocompletedata)

## 기본 정보

- **기능:** JQL 검색에 사용할 필드/함수/예약어 등 참조 데이터를 반환한다.
- **Endpoint:** `GET /rest/api/3/jql/autocompletedata`
- **인증:** 익명 접근 가능
- **권한:** 없음

## 설명

JQL 쿼리를 프로그래밍 방식으로 생성하거나 커스텀 쿼리 빌더에서 입력을 검증할 때 참고할 수 있도록, 검색 가능한 필드 목록, 함수 목록, JQL 예약어 목록을 다운로드 형태로 제공한다. 프로젝트별 필터링이나 동일 이름 필드의 축약이 필요하면 POST 버전(`Get field reference data (POST)`)을 사용해야 한다.

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `jqlReservedWords` | string[] | JQL 예약어 목록 | `["empty","and","or","in","distinct"]` |
| `visibleFieldNames` | array | 검색 가능한 필드 목록(연산자, 타입 등 포함) | 아래 예시 참고 |
| `visibleFunctionNames` | array | 사용 가능한 함수 목록 | 아래 예시 참고 |

```json
{
  "jqlReservedWords": ["empty", "and", "or", "in", "distinct"],
  "visibleFieldNames": [
    {
      "displayName": "summary",
      "operators": ["~", "!~", "is", "is not"],
      "orderable": "true",
      "searchable": "true",
      "types": ["java.lang.String"],
      "value": "summary"
    },
    {
      "auto": "true",
      "cfid": "cf[10880]",
      "displayName": "Sprint - cf[10880]",
      "operators": ["=", "!=", "in", "not in", "is", "is not"],
      "orderable": "true",
      "searchable": "true",
      "types": ["com.atlassian.greenhopper.service.sprint.Sprint"],
      "value": "Sprint"
    }
  ],
  "visibleFunctionNames": [
    {
      "displayName": "standardIssueTypes()",
      "isList": "true",
      "types": ["com.atlassian.jira.issue.issuetype.IssueType"],
      "value": "standardIssueTypes()"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 자격 증명이 올바르지 않음 | 인증 토큰 확인 |

## 주의 사항

- 프로젝트별 필드 필터링이나 필드 축약(collapse)이 필요하면 POST 버전을 사용한다.

---

### [중간] 3. Get field reference data (POST) (POST /rest/api/3/jql/autocompletedata)

## 기본 정보

- **기능:** JQL 검색에 사용할 필드/함수/예약어 참조 데이터를 프로젝트 필터링 및 필드 축약 옵션과 함께 반환한다.
- **Endpoint:** `POST /rest/api/3/jql/autocompletedata`
- **인증:** Bearer Token 필요
- **권한:** 없음

## 설명

GET 버전과 동일한 참조 데이터를 반환하되, `projectIds`로 특정 프로젝트에 보이는 커스텀 필드만 필터링하거나, `includeCollapsedFields`로 이름이 같은 커스텀 필드를 하나의 축약된 필드로 묶어 반환할 수 있다. 시스템 필드는 필터링과 무관하게 항상 반환된다. 유효하지 않은 프로젝트 ID는 무시된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `includeCollapsedFields` | boolean | 아니오 | - | 이름이 겹치는 필드에 대한 축약 필드 포함 여부 | `true` |
| `projectIds` | integer[] | 아니오 | - | 반환할 필드 상세 정보를 필터링할 프로젝트 ID 목록 | `[10000]` |

```json
{
  "includeCollapsedFields": true,
  "projectIds": [10000]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `jqlReservedWords` | string[] | JQL 예약어 목록 | `["empty","and","or","in","distinct"]` |
| `visibleFieldNames` | array | 검색 가능한 필드 목록 (축약 필드 포함 가능) | 아래 예시 참고 |
| `visibleFunctionNames` | array | 사용 가능한 함수 목록 | 아래 예시 참고 |

```json
{
  "jqlReservedWords": ["empty", "and", "or", "in", "distinct"],
  "visibleFieldNames": [
    {
      "displayName": "summary",
      "operators": ["~", "!~", "is", "is not"],
      "orderable": "true",
      "searchable": "true",
      "types": ["java.lang.String"],
      "value": "summary"
    },
    {
      "auto": "true",
      "cfid": "cf[10061]",
      "displayName": "Component - cf[10061]",
      "operators": ["=", "!=", "in", "not in", "is", "is not"],
      "orderable": "true",
      "types": ["com.atlassian.jira.issue.customfields.option.Option"],
      "value": "cf[10061]"
    },
    {
      "auto": "true",
      "displayName": "Component - Component[Dropdown]",
      "operators": ["=", "!=", "in", "not in", "is", "is not"],
      "searchable": "true",
      "types": ["com.atlassian.jira.issue.customfields.option.Option"],
      "value": "\"Component[Dropdown]\""
    }
  ],
  "visibleFunctionNames": [
    {
      "displayName": "standardIssueTypes()",
      "isList": "true",
      "types": ["com.atlassian.jira.issue.issuetype.IssueType"],
      "value": "standardIssueTypes()"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 본문 확인 후 재요청 |
| 401 | - | 인증 자격 증명이 올바르지 않음 | 인증 토큰 확인 |

## 주의 사항

- `projectIds`에 잘못된 프로젝트 ID를 넣어도 오류 없이 무시된다.
- `includeCollapsedFields`로 이름이 같은 커스텀 필드를 하나의 필드로 동시에 검색할 수 있다.

---

### [중간] 4. Get field auto complete suggestions (GET /rest/api/3/jql/autocompletedata/suggestions)

## 기본 정보

- **기능:** 특정 필드에 대한 JQL 자동완성 제안 값을 반환한다.
- **Endpoint:** `GET /rest/api/3/jql/autocompletedata/suggestions`
- **인증:** 익명 접근 가능
- **권한:** 없음

## 설명

`fieldName`만 전달하면 해당 필드의 전체 값 목록을, `fieldValue`를 함께 전달하면 입력 중인 텍스트를 포함하는 값 목록을 반환한다. `predicateName`/`predicateValue`를 사용하면 CHANGED 연산자의 프레디케이트(by/from/to)에 대한 제안도 받을 수 있다. 커스텀 쿼리 빌더나 검색 UI에서 사용자가 입력하는 동안 실시간 자동완성을 제공하는 데 사용된다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `fieldName` | string | 아니오 | - | 필드 이름 | `component` |
| `fieldValue` | string | 아니오 | - | 사용자가 입력 중인 부분 필드 값 | `Ac` |
| `predicateName` | string | 아니오 | - | CHANGED 연산자 프레디케이트 이름 (`by`, `from`, `to`) | `by` |
| `predicateValue` | string | 아니오 | - | 사용자가 입력 중인 부분 프레디케이트 값 | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `results` | array | 제안 값 목록(표시명/실제값) | 아래 예시 참고 |

```json
{
  "results": [
    { "displayName": "<b>Ac</b>tiveObjects (AO)", "value": "ActiveObjects" },
    { "displayName": "Atlassian Connect (<b>AC</b>)", "value": "Atlassian Connect" },
    { "displayName": "Atlassian Connect in Jira (<b>AC</b>JIRA)", "value": "Atlassian Connect in Jira" }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 파라미터 조합이 유효하지 않음 | 파라미터 조합(fieldName/predicateName 등) 확인 |
| 401 | - | 인증 자격 증명이 올바르지 않음 | 인증 토큰 확인 |

## 주의 사항

- `fieldValue`, `predicateValue`는 부분 문자열 매칭에 사용되며 대소문자 강조(`<b>` 태그)가 포함된 표시명을 함께 반환한다.

---

### [중간] 5. Convert user identifiers to account IDs in JQL queries (POST /rest/api/3/jql/pdcleaner)

## 기본 정보

- **기능:** JQL 쿼리에 포함된 사용자 식별자(username 또는 user key)를 계정 ID(accountId) 기반으로 변환한다.
- **Endpoint:** `POST /rest/api/3/jql/pdcleaner`
- **인증:** Bearer Token 필요
- **권한:** Jira 접근 권한 (Permission to access Jira)

## 설명

저장된 JQL 쿼리를 GDPR 준수 형태로 마이그레이션하고자 할 때 사용한다. 쿼리 내 사용자명/사용자 키를 동등한 accountId 기반 쿼리로 변환하며, 최대 100개의 쿼리를 한 번에 처리할 수 있다. 변환할 수 없는 사용자(알 수 없는 사용자)는 별도로 결과에 표시된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `queryStrings` | string[] | 아니오 | 최대 100개 | 사용자 식별자를 포함한 쿼리 목록 | `["issuetype = Bug AND assignee = mia order by lastViewed DESC"]` |

```json
{
  "queryStrings": [
    "issuetype = Bug AND assignee = mia order by lastViewed DESC"
  ]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `queryStrings` | string[] | 변환된 쿼리 목록(요청 순서 유지) | `["issuetype = Bug AND assignee in (abcde-12345) AND reporter in (abc551-c4e99) order by lastViewed DESC"]` |
| `queriesWithUnknownUsers` | array | 알 수 없는 사용자가 포함되어 변환된 쿼리 목록 | 아래 예시 참고 |

```json
{
  "queriesWithUnknownUsers": [
    { "convertedQuery": "assignee = unknown", "originalQuery": "assignee = mia" }
  ],
  "queryStrings": [
    "issuetype = Bug AND assignee in (abcde-12345) AND reporter in (abc551-c4e99) order by lastViewed DESC"
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 하나 이상의 쿼리를 변환할 수 없음 (잘못된 연산자/키워드, 사용자를 찾을 수 없음 등) | 쿼리 문법 및 사용자 식별자 확인 |
| 401 | - | 인증 자격 증명이 올바르지 않거나 없음 | 인증 토큰 확인 |

## 주의 사항

- 응답의 쿼리 순서는 요청한 순서와 동일하게 유지된다.
- 최대 100개 쿼리로 제한되므로 대량 마이그레이션 시 배치 처리가 필요하다.
