# _38-issue-search API 요약

이 리소스 그룹은 JQL(Jira Query Language) 쿼리로 이슈를 검색하거나, 이슈 피커(자동완성)용 후보를 찾거나, 특정 이슈가 JQL 조건에 부합하는지 확인하는 등 "이슈 검색" 관련 기능을 제공한다. 제외된 API는 없다(모두 프로젝트 단위 권한 또는 무권한으로 호출 가능).

## 제외된 API

- 없음 (사이트 전체 관리자 권한이 필요한 API가 이 그룹에는 없음)

---

### [상] 1. 이슈 피커 후보 조회 (GET /rest/api/3/issue/picker)

## 기본 정보

- **기능:** 사용자가 입력한 문자열과 일치하는 이슈 목록을 반환하여 이슈 검색 자동완성(오토컴플리트)에 사용
- **Endpoint:** `GET /rest/api/3/issue/picker`
- **인증:** 익명 접근 가능 (인증 없이도 호출 가능. 단, 비공개 프로젝트 이슈는 인증 필요)
- **권한:** 없음

## 설명

사용자가 이슈를 검색어(단어/문자열)로 찾을 때 자동완성 후보를 제공하기 위한 API다. `History Search`(사용자가 최근에 생성/수정/조회한 이슈 중 `query`와 일치하는 것)와 `Current Search`(`currentJQL` 조건에 맞으면서 `query`와 일치하는 것) 두 목록을 반환한다. 팀 대시보드나 이슈 연결 UI에서 "이슈 검색창"을 구현할 때 핵심적으로 쓰일 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | 아니오 | - | 이슈의 제목, 설명, 코멘트 등 텍스트 필드와 매칭할 문자열 | `"로그인 오류"` |
| `currentJQL` | string | 아니오 | - | 검색어를 찾을 이슈 범위를 정의하는 JQL. `username`/`userkey`는 사용 불가(`accountId` 사용) | `"project = SSAFY"` |
| `currentIssueKey` | string | 아니오 | - | 검색 결과에서 제외할 이슈 키(현재 보고 있는 이슈 등) | `"SSAFY-12"` |
| `currentProjectId` | string | 아니오 | - | 후보 이슈가 속해야 하는 프로젝트 ID | `"10000"` |
| `showSubTasks` | boolean | 아니오 | - | 하위 작업(sub-task)을 후보에 포함할지 여부 | `true` |
| `showSubTaskParent` | boolean | 아니오 | - | `currentIssueKey`가 하위 작업일 때, 상위 이슈를 후보에 포함할지 여부 | `false` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `sections[].id` | string | 자동완성용 이슈 유형의 ID | `"cs"` |
| `sections[].issues[].id` | integer | 이슈 ID | `10001` |
| `sections[].issues[].img` | string | 이슈 타입 아바타 URL | `"https://.../icon.png"` |
| `sections[].issues[].key` | string | 이슈 키 | `"SSAFY-1"` |
| `sections[].issues[].keyHtml` | string | HTML 형식의 이슈 키 | `"<b>SSAFY</b>-1"` |
| `sections[].issues[].summary` | string | 검색어가 강조(bold)된 HTML 형식 요약 | `"로그인 <b>오류</b> 수정"` |
| `sections[].issues[].summaryText` | string | 일반 텍스트 요약 | `"로그인 오류 수정"` |
| `sections[].label` | string | 이슈 유형 섹션의 레이블 | `"현재 검색"` |
| `sections[].msg` | string | 후보가 없을 때 표시할 메시지 | `"일치하는 이슈가 없습니다"` |
| `sections[].sub` | string | 후보가 있을 때 개수 안내 메시지 | `"5개 이슈 찾음"` |

```json
{
  "sections": [
    {
      "id": "cs",
      "label": "현재 검색",
      "sub": "5개 이슈 찾음",
      "issues": [
        {
          "id": 10001,
          "key": "SSAFY-1",
          "keyHtml": "SSAFY-1",
          "img": "https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10300",
          "summary": "로그인 <b>오류</b> 수정",
          "summaryText": "로그인 오류 수정"
        }
      ]
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 토큰/세션 확인 후 재시도 |

## 주의 사항

- `username`, `userkey`는 개인정보 보호를 위해 `currentJQL`의 검색어로 사용할 수 없다. 대신 `accountId`를 사용해야 한다.
- 익명 접근이 허용되지만, 결과는 실제 조회 권한이 있는 이슈로 제한된다.

---

### [상] 2. JQL을 이용한 이슈 검색 - 향상된 검색 GET (GET /rest/api/3/search/jql)

## 기본 정보

- **기능:** JQL 쿼리로 이슈를 검색하는 최신(권장) 검색 API
- **Endpoint:** `GET /rest/api/3/search/jql`
- **인증:** 익명 접근 가능(단, 결과는 조회 권한 있는 이슈로 제한됨)
- **권한:** 프로젝트별 `Browse projects` 권한, 이슈 단위 보안이 설정된 경우 해당 열람 권한

## 설명

기존 `/rest/api/3/search`(제거 예정)를 대체하는 새로운 검색 엔드포인트로, `nextPageToken` 기반 페이지네이션을 사용한다. 통합 대시보드에서 이슈 목록/상태를 조회하거나 특정 조건(예: 담당자, 상태, 스프린트)에 맞는 이슈를 가져올 때 핵심적으로 사용된다. 최근 변경 사항이 검색 결과에 즉시 반영되지 않을 수 있으며, 강한 일관성이 필요하면 `reconcileIssues` 파라미터를 사용한다. JQL은 반드시 bounded(검색 범위 제한이 있는) 쿼리여야 한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `jql` | string | 아니오 | - | JQL 표현식(bounded 쿼리 필요). `orderBy`는 최대 7개 필드까지 | `"assignee = currentUser() order by key"` |
| `nextPageToken` | string | 아니오 | `null` | 다음 페이지를 가져오기 위한 토큰. 첫 페이지는 `null` | `"CAEaAggD"` |
| `maxResults` | integer | 아니오 | - | 페이지당 최대 항목 수(최대 5000건) | `50` |
| `fields` | array | 아니오 | `id` | 반환할 필드 목록(콤마 구분). `*all`, `*navigable`, `id`, `-필드명`(제외) 등 사용 가능 | `"summary,comment"` |
| `expand` | string | 아니오 | - | 이슈에 대한 추가 정보 포함 옵션(콤마 구분 문자열) | `"names,changelog"` |
| `properties` | array | 아니오 | - | 결과에 포함할 이슈 속성 키(최대 5개) | `"prop1,prop2"` |
| `fieldsByKeys` | boolean | 아니오 | `false` | 필드를 ID 대신 키로 참조할지 여부 | `true` |
| `failFast` | boolean | 아니오 | - | 필드 조회 실패 시 요청을 조기에 실패시킬지 여부 | `false` |
| `reconcileIssues` | array | 아니오 | - | 결과와 강한 일관성으로 대조할 이슈 ID(최대 50개) | `[10001, 10002]` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `true` |
| `issues[].id` | string | 이슈 ID | `"10002"` |
| `issues[].key` | string | 이슈 키 | `"ED-1"` |
| `issues[].fields` | object | 요청한 필드 값들 | `{...}` |

```json
{
  "isLast": true,
  "issues": [
    {
      "id": "10002",
      "key": "ED-1",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002",
      "fields": {
        "description": "Main order flow broken",
        "project": {
          "id": "10000",
          "key": "EX",
          "name": "Example"
        }
      }
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 검색 요청(JQL 등)이 유효하지 않음 | JQL 문법 및 bounded 조건 확인 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 토큰/세션 확인 후 재시도 |

## 주의 사항

- JQL은 반드시 bounded 쿼리여야 하며(예: `order by key desc`는 unbounded라 거부될 수 있음), 검색 조건(`assignee = currentUser()` 등)이 필요하다.
- 기본적으로 `fields`를 지정하지 않으면 `id`만 반환되므로, 실제 이슈 데이터를 쓰려면 `fields` 파라미터를 명시해야 한다.
- 기존 `GET /rest/api/3/search`는 제거 예정이므로 신규 통합 작업은 이 엔드포인트를 사용해야 한다.

---

### [상] 3. JQL을 이용한 이슈 검색 - 향상된 검색 POST (POST /rest/api/3/search/jql)

## 기본 정보

- **기능:** JQL 쿼리로 이슈를 검색하는 최신(권장) 검색 API의 POST 버전(긴 JQL 표현식용)
- **Endpoint:** `POST /rest/api/3/search/jql`
- **인증:** 익명 접근 가능(단, 결과는 조회 권한 있는 이슈로 제한됨)
- **권한:** 프로젝트별 `Browse projects` 권한, 이슈 단위 보안이 설정된 경우 해당 열람 권한

## 설명

GET 버전과 동일한 기능을 제공하되, JQL 쿼리 표현식이 URL 쿼리 파라미터로 인코딩하기에 너무 길 때 사용한다. 요청 본문에 검색 조건을 담아 전달하므로 복잡한 JQL이나 다수의 `properties`/`fields`를 다룰 때 유리하다. 통합 대시보드·리포트 자동화에서 정기적으로 이슈를 조회할 때 GET 버전과 함께 핵심적으로 사용된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `jql` | string | 아니오 | bounded 쿼리 필요, `orderBy` 최대 7개 필드 | JQL 표현식 | `"assignee = currentUser() order by key"` |
| `nextPageToken` | string | 아니오 | - | 다음 페이지 토큰 | `"CAEaAggD"` |
| `maxResults` | integer | 아니오 | 최대 5000건 반환 | 페이지당 최대 항목 수 | `50` |
| `fields` | array&lt;string&gt; | 아니오 | - | 반환할 필드 목록. 기본값 `id` | `["summary", "comment"]` |
| `fieldsByKeys` | boolean | 아니오 | 기본값 `false` | 필드를 키로 참조할지 여부 | `false` |
| `expand` | string | 아니오 | - | 콤마 구분 확장 옵션 문자열 | `"names,changelog"` |
| `properties` | array&lt;string&gt; | 아니오 | 최대 5개 | 결과에 포함할 이슈 속성 | `["prop1", "prop2"]` |
| `reconcileIssues` | array&lt;integer&gt; | 아니오 | 최대 50개 | 강한 일관성 대조용 이슈 ID | `[10001, 10002]` |

```json
{
  "jql": "assignee = currentUser() order by key",
  "maxResults": 50,
  "fields": ["summary", "status", "assignee"],
  "fieldsByKeys": false
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `true` |
| `issues[].id` | string | 이슈 ID | `"10002"` |
| `issues[].key` | string | 이슈 키 | `"ED-1"` |
| `issues[].fields` | object | 요청한 필드 값들 | `{...}` |

```json
{
  "isLast": true,
  "issues": [
    {
      "id": "10002",
      "key": "ED-1",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002",
      "fields": {
        "description": "Main order flow broken"
      }
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 검색 요청(JQL 등)이 유효하지 않음 | JQL 문법 및 bounded 조건 확인 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 토큰/세션 확인 후 재시도 |

## 주의 사항

- GET 버전과 동일하게 JQL은 bounded 쿼리여야 한다.
- 긴 JQL이나 많은 필드/속성을 요청할 때는 GET 대신 이 POST 버전을 사용하는 것이 권장된다.

---

### [상] 4. JQL을 이용한 이슈 개수(카운트) 조회 (POST /rest/api/3/search/approximate-count)

## 기본 정보

- **기능:** JQL 조건에 맞는 이슈의 대략적인(추정) 개수를 반환
- **Endpoint:** `POST /rest/api/3/search/approximate-count`
- **인증:** 익명 접근 가능(단, 결과는 조회 권한 있는 이슈로 제한됨)
- **권한:** 프로젝트별 `Browse projects` 권한, 이슈 단위 보안이 설정된 경우 해당 열람 권한

## 설명

대시보드에서 "열린 이슈 N건", "이번 스프린트 남은 작업 M건"과 같은 통계성 카운트를 표시할 때 이슈 전체를 가져오지 않고 개수만 빠르게 얻을 수 있는 API다. 최근 변경 사항이 즉시 반영되지 않을 수 있으며, 성능상의 이유로 JQL은 반드시 bounded 쿼리여야 한다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `jql` | string | 아니오 | bounded 쿼리 필요 | 개수를 셀 대상 이슈를 정의하는 JQL 표현식 | `"project = SSAFY AND status = \"In Progress\""` |

```json
{
  "jql": "project = SSAFY AND status = \"In Progress\""
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `count` | integer | JQL 조건에 맞는 이슈의 추정 개수 | `153` |

```json
{
  "count": 153
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | JQL 쿼리를 파싱할 수 없음 | JQL 문법 확인 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 토큰/세션 확인 후 재시도 |

## 주의 사항

- 반환되는 개수는 "추정치"이며 최근 업데이트가 즉시 반영되지 않을 수 있다. 정확한 실시간 카운트가 필요한 용도에는 부적합하다.
- JQL은 반드시 검색 범위를 제한하는 bounded 쿼리여야 한다.

---

### [중] 5. 여러 이슈의 JQL 매칭 여부 확인 (POST /rest/api/3/jql/match)

## 기본 정보

- **기능:** 하나 이상의 이슈가 하나 이상의 JQL 쿼리에 매칭되는지 일괄 확인
- **Endpoint:** `POST /rest/api/3/jql/match`
- **인증:** Bearer Token 필요(또는 세션 인증)
- **권한:** 없음(단, 이슈는 사용자가 해당 프로젝트에 대해 `Browse projects` 권한이 있고, 이슈 단위 보안이 설정된 경우 열람 권한이 있는 것에 한해서만 매칭됨)

## 설명

이슈 ID 목록과 JQL 쿼리 목록을 받아, 각 JQL에 대해 어떤 이슈가 매칭되는지를 배치로 반환한다. 예를 들어 webhook 이벤트로 들어온 이슈가 특정 알림 규칙(JQL로 정의된 조건)에 해당하는지 판별하는 보조 로직에 활용할 수 있다. 핵심 검색 흐름은 아니지만 알림 필터링 등에 유용하다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `issueIds` | array&lt;integer&gt; | 예 | - | 확인할 이슈 ID 목록 | `[10001, 10004]` |
| `jqls` | array&lt;string&gt; | 예 | - | 매칭 여부를 확인할 JQL 쿼리 목록 | `["project = SSAFY", "assignee = currentUser()"]` |

```json
{
  "issueIds": [10001, 10004],
  "jqls": ["project = SSAFY", "assignee = currentUser()"]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `matches[].matchedIssues` | array&lt;integer&gt; | 해당 JQL에 매칭된 이슈 ID 목록 | `[10000, 10004]` |
| `matches[].errors` | array&lt;string&gt; | 해당 JQL 처리 중 발생한 오류 메시지 | `["Invalid JQL: broken = value"]` |

```json
{
  "matches": [
    { "matchedIssues": [10000, 10004], "errors": [] },
    { "matchedIssues": [], "errors": ["Invalid JQL: broken = value"] }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `jqls` 또는 `issueIds`가 최대 허용 개수를 초과함 | 요청을 배치로 나눠서 재시도 |

## 주의 사항

- `jqls`와 `issueIds` 각각 최대 개수 제한이 있다(초과 시 400 오류).
- 특정 JQL이 잘못되었더라도 다른 JQL의 매칭 결과는 정상 반환되며, 오류는 해당 JQL의 `errors` 배열에 담긴다.

---

### [중] 6. JQL을 이용한 이슈 검색 - 구버전 GET (제거 예정) (GET /rest/api/3/search)

## 기본 정보

- **기능:** JQL로 이슈를 검색하는 구버전 API (GET)
- **Endpoint:** `GET /rest/api/3/search`
- **인증:** 익명 접근 가능(단, 결과는 조회 권한 있는 이슈로 제한됨)
- **권한:** 프로젝트별 `Browse projects` 권한, 이슈 단위 보안이 설정된 경우 해당 열람 권한

## 설명

Atlassian이 제거 예정으로 공지한 구버전 검색 API로, `startAt`/`total` 기반의 오프셋 페이지네이션을 사용한다. 신규 통합에는 `/rest/api/3/search/jql`(향상된 검색) 사용이 권장되며, 이 API는 향후 제거될 수 있어 장기적으로 의존하기에는 리스크가 있다. 기존 코드 호환이나 참고용으로만 중간 우선순위로 채택한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `jql` | string | 아니오 | - | JQL 표현식. 없으면 모든 이슈 반환 | `"project = SSAFY"` |
| `startAt` | integer | 아니오 | - | 페이지 오프셋(첫 항목 인덱스) | `0` |
| `maxResults` | integer | 아니오 | - | 페이지당 최대 항목 수 | `50` |
| `validateQuery` | string | 아니오 | - | JQL 검증 방식(`strict`/`warn`/`none`/`true`(deprecated)/`false`(deprecated)) | `"strict"` |
| `fields` | array | 아니오 | 모든 navigable 필드 | 반환할 필드 목록 | `"summary,comment"` |
| `expand` | string | 아니오 | - | 추가 정보 포함 옵션 | `"changelog"` |
| `properties` | array | 아니오 | - | 포함할 이슈 속성(최대 5개) | `"prop1,prop2"` |
| `fieldsByKeys` | boolean | 아니오 | - | 필드를 키로 참조할지 여부 | `false` |
| `failFast` | boolean | 아니오 | - | 필드 로딩 오류 시 즉시 실패할지 여부 | `false` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `startAt` | integer | 페이지 오프셋 | `0` |
| `maxResults` | integer | 페이지당 최대 항목 수 | `50` |
| `total` | integer | 전체 이슈 수 | `1` |
| `issues[].key` | string | 이슈 키 | `"ED-1"` |

```json
{
  "expand": "names,schema",
  "startAt": 0,
  "maxResults": 50,
  "total": 1,
  "issues": [
    {
      "id": "10002",
      "key": "ED-1",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002",
      "fields": {
        "description": {
          "type": "doc",
          "version": 1,
          "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Main order flow broken" }] }]
        }
      }
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | JQL 쿼리가 유효하지 않음 | JQL 문법 확인 |
| 401 | - | 인증 자격 증명이 잘못됨 | 토큰/세션 확인 후 재시도 |

## 주의 사항

- Atlassian 공지에 따라 이 엔드포인트는 제거(removal) 예정이다. 신규 개발에는 `/rest/api/3/search/jql`을 사용해야 한다.
- JQL이 URL 쿼리 파라미터로 인코딩하기에 너무 길면 POST 버전을 사용해야 한다.

---

### [중] 7. JQL을 이용한 이슈 검색 - 구버전 POST (제거 예정) (POST /rest/api/3/search)

## 기본 정보

- **기능:** JQL로 이슈를 검색하는 구버전 API (POST, 긴 JQL 표현식용)
- **Endpoint:** `POST /rest/api/3/search`
- **인증:** 익명 접근 가능(단, 결과는 조회 권한 있는 이슈로 제한됨)
- **권한:** 프로젝트별 `Browse projects` 권한, 이슈 단위 보안이 설정된 경우 해당 열람 권한

## 설명

구버전 GET 검색과 동일한 기능을 POST 방식으로 제공하며, JQL 쿼리 표현식이 길어 URL 쿼리 파라미터로 인코딩하기 어려운 경우 사용한다. GET 버전과 마찬가지로 Atlassian이 제거 예정으로 공지했으므로, 신규 통합에는 `/rest/api/3/search/jql`(POST) 사용이 권장된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `jql` | string | 아니오 | - | JQL 표현식 | `"project = SSAFY"` |
| `startAt` | integer | 아니오 | 기본값 `0` | 페이지 오프셋 | `0` |
| `maxResults` | integer | 아니오 | - | 페이지당 최대 항목 수 | `50` |
| `validateQuery` | enum | 아니오 | 기본값 `strict` | `strict`/`warn`/`none`/`true`(deprecated)/`false`(deprecated) | `"strict"` |
| `fields` | array&lt;string&gt; | 아니오 | 기본값 `*navigable` | 반환할 필드 목록 | `["summary", "comment"]` |
| `fieldsByKeys` | boolean | 아니오 | 기본값 `false` | 필드를 키로 참조할지 여부 | `false` |
| `properties` | array&lt;string&gt; | 아니오 | 최대 5개 | 포함할 이슈 속성 | `["prop1", "prop2"]` |
| `expand` | array&lt;string&gt; | 아니오 | - | 추가 정보 포함 옵션 목록 | `["changelog"]` |

```json
{
  "jql": "project = SSAFY",
  "startAt": 0,
  "maxResults": 50,
  "validateQuery": "strict",
  "fields": ["summary", "status"]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `startAt` | integer | 페이지 오프셋 | `0` |
| `maxResults` | integer | 페이지당 최대 항목 수 | `50` |
| `total` | integer | 전체 이슈 수 | `1` |
| `issues[].key` | string | 이슈 키 | `"ED-1"` |

```json
{
  "expand": "names,schema",
  "startAt": 0,
  "maxResults": 50,
  "total": 1,
  "issues": [
    {
      "id": "10002",
      "key": "ED-1",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | JQL 쿼리가 유효하지 않음 | JQL 문법 확인 |
| 401 | - | 인증 자격 증명이 잘못됨 | 토큰/세션 확인 후 재시도 |

## 주의 사항

- Atlassian 공지에 따라 이 엔드포인트는 제거(removal) 예정이다. 신규 개발에는 `/rest/api/3/search/jql`(POST)을 사용해야 한다.
- GET 버전이 있으나, JQL이 길 때는 이 POST 버전을 사용한다.
