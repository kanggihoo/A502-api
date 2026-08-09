# _48-issue-worklogs API 요약

이 리소스 그룹은 Jira 이슈의 워크로그(작업 시간 기록)를 조회·생성·수정·삭제하고, 변경/삭제된 워클로그 ID 목록을 동기화하는 기능을 제공한다. 제외된 API는 없다(모두 프로젝트 권한 수준에서 사용 가능).

## 제외된 API

- 없음 (모든 엔드포인트가 프로젝트 관리자/일반 권한 범위에서 호출 가능하며, 사이트 전체 시스템 관리자 권한을 요구하지 않음)

---

### [높음] 1. Get issue worklogs (GET /rest/api/3/issue/{issueIdOrKey}/worklog)

## 기본 정보

- **기능:** 특정 이슈에 달린 워클로그 목록을 생성 시각 순으로 조회한다.
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/worklog`
- **인증:** Bearer Token 필요 (단, 익명 접근도 허용됨)
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 권한, 이슈 단위 보안이 설정된 경우 해당 열람 권한, 워클로그에 가시성 제한이 있으면 해당 그룹/역할 소속 여부

## 설명

이슈에 기록된 워클로그들을 페이지네이션으로 조회하며, 특정 시작일 이후/이전의 워클로그만 필터링할 수 있다. Jira에서 시간 추적(Time tracking) 기능이 꺼져 있으면 오류가 반환된다. 통합 대시보드에서 이슈별 작업 시간 현황을 보여줄 때 핵심적으로 쓰인다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `10010` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `startAt` | integer | N | - | 반환할 첫 항목의 페이지 오프셋 | `0` |
| `maxResults` | integer | N | - | 페이지당 최대 반환 개수 | `50` |
| `startedAfter` | integer | N | - | 이 시각(UNIX ms) 이후 시작된 워클로그만 반환 | `1610000000000` |
| `startedBefore` | integer | N | - | 이 시각(UNIX ms) 이전 시작된 워클로그만 반환 | `1620000000000` |
| `expand` | string | N | - | `properties` 지정 시 워클로그 속성 포함 | `properties` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `maxResults` | integer | 페이지당 최대 개수 | `1` |
| `startAt` | integer | 페이지 오프셋 | `0` |
| `total` | integer | 전체 워클로그 수 | `1` |
| `worklogs` | array | 워클로그 객체 목록 | 아래 참조 |

```json
{
  "maxResults": 1,
  "startAt": 0,
  "total": 1,
  "worklogs": [
    {
      "author": {
        "accountId": "5b10a2844c20165700ede21g",
        "active": false,
        "displayName": "Mia Krystof",
        "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
      },
      "comment": {
        "type": "doc",
        "version": 1,
        "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "I did some work here." }] }]
      },
      "id": "100028",
      "issueId": "10002",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000",
      "started": "2021-01-17T12:34:00.000+0000",
      "timeSpent": "3h 20m",
      "timeSpentSeconds": 12000,
      "updateAuthor": {
        "accountId": "5b10a2844c20165700ede21g",
        "active": false,
        "displayName": "Mia Krystof",
        "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
      },
      "updated": "2021-01-18T23:45:00.000+0000",
      "visibility": {
        "identifier": "276f955c-63d7-42c8-9520-92d01dca0625",
        "type": "group",
        "value": "jira-developers"
      }
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 재확인 |
| 404 | - | 이슈를 찾을 수 없음 / 열람 권한 없음 / `startAt`·`maxResults`가 숫자가 아님 / 시간 추적 비활성화 | 이슈 키, 파라미터, 시간 추적 설정 확인 |

## 주의 사항

- 시간 추적(Time tracking)이 비활성화된 사이트에서는 항상 오류가 발생한다.
- 워클로그에 가시성 제한(그룹/역할)이 걸려 있으면 해당 소속이 아닌 사용자에게는 보이지 않는다.

---

### [높음] 2. Add worklog (POST /rest/api/3/issue/{issueIdOrKey}/worklog)

## 기본 정보

- **기능:** 이슈에 새 워클로그(작업 기록)를 추가한다.
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/worklog`
- **인증:** Bearer Token 필요 (단, 익명 접근도 허용됨)
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 및 *Work on issues* 권한, 이슈 단위 보안 열람 권한

## 설명

이슈에 작업 시간과 코멘트를 기록하는 워클로그를 생성한다. `timeSpent` 또는 `timeSpentSeconds` 중 하나가 필수이며 `adjustEstimate` 쿼리 파라미터로 잔여 예상 시간을 함께 조정할 수 있다. 프로젝트 운영 지원(작업 시간 기록 자동화)의 핵심 API다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `10010` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `notifyUsers` | boolean | N | - | 이슈를 watch 중인 사용자에게 이메일 알림 여부 | `true` |
| `adjustEstimate` | string | N | - | 예상 시간 조정 방식: `new`/`leave`/`manual`/`auto` | `auto` |
| `newEstimate` | string | N | - | `adjustEstimate=new`일 때 필수, 새 예상 시간 | `2d` |
| `reduceBy` | string | N | - | `adjustEstimate=manual`일 때 필수, 감소시킬 양 | `2d` |
| `expand` | string | N | - | `properties` 지정 시 워클로그 속성 포함 | `properties` |
| `overrideEditableFlag` | boolean | N | - | 이슈가 편집 불가 상태여도 강제로 워클로그 추가 (Connect/Forge 앱 + *Administer Jira* 권한 필요) | `false` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `started` | string | Y(생성 시) | - | 작업 시작 일시 | `"2021-01-17T12:34:00.000+0000"` |
| `timeSpent` | string | Y(`timeSpentSeconds` 없을 시) | `timeSpentSeconds`와 동시 사용 불가 | 소요 시간 (일/시간/분) | `"3h 20m"` |
| `timeSpentSeconds` | integer | Y(`timeSpent` 없을 시) | `timeSpent`와 동시 사용 불가 | 소요 시간(초) | `12000` |
| `comment` | any | N | ADF 형식 | 작업 내용 코멘트 | 아래 예시 참조 |
| `visibility` | any | N | - | 워클로그 공개 범위 제한 | 아래 예시 참조 |
| `properties` | array | N | - | 워클로그 커스텀 속성 | `[]` |

```json
{
  "comment": {
    "type": "doc",
    "version": 1,
    "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "I did some work here." }] }]
  },
  "started": "2021-01-17T12:34:00.000+0000",
  "timeSpent": "3h 20m",
  "visibility": {
    "identifier": "276f955c-63d7-42c8-9520-92d01dca0625",
    "type": "group",
    "value": "jira-developers"
  }
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 워클로그 ID | `"100028"` |
| `issueId` | string | 워클로그가 속한 이슈 ID | `"10002"` |
| `timeSpent` | string | 소요 시간 문자열 | `"3h 20m"` |
| `timeSpentSeconds` | integer | 소요 시간(초) | `12000` |
| `started` | string | 작업 시작 일시 | `"2021-01-17T12:34:00.000+0000"` |
| `author` | any | 작성자 정보 | 사용자 객체 |

```json
{
  "author": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "comment": {
    "type": "doc",
    "version": 1,
    "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "I did some work here." }] }]
  },
  "id": "100028",
  "issueId": "10002",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000",
  "started": "2021-01-17T12:34:00.000+0000",
  "timeSpent": "3h 20m",
  "timeSpentSeconds": 12000,
  "updateAuthor": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "updated": "2021-01-18T23:45:00.000+0000",
  "visibility": {
    "identifier": "276f955c-63d7-42c8-9520-92d01dca0625",
    "type": "group",
    "value": "jira-developers"
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `adjustEstimate=new`인데 `newEstimate` 누락/오류, `adjustEstimate=manual`인데 `reduceBy` 누락/오류, 권한 없음, JSON 형식 오류 | 요청 파라미터/본문 검증 |
| 401 | - | 인증 정보 오류 | 토큰 재확인 |
| 404 | - | 이슈를 찾을 수 없음 / 열람 권한 없음 | 이슈 키 확인 |
| 413 | - | 이슈당 워클로그/첨부파일 개수 제한 초과 | 워클로그 수 조정 |

## 주의 사항

- `timeSpent`와 `timeSpentSeconds`는 동시에 지정할 수 없다.
- `overrideEditableFlag`는 Connect/Forge 앱 + *Administer Jira* 글로벌 권한 조합에서만 유효하다(개인 계정 API 호출과는 무관).

---

### [높음] 3. Get worklog (GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id})

## 기본 정보

- **기능:** 이슈에 속한 특정 워클로그 1건을 조회한다.
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`
- **인증:** Bearer Token 필요 (단, 익명 접근도 허용됨)
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 권한, 이슈 단위 보안 열람 권한, 워클로그 가시성 제한 시 해당 그룹/역할 소속

## 설명

워클로그 ID로 단건 상세 정보를 조회한다. 알림/대시보드에서 특정 워클로그 원문 링크를 보여주거나 상세 내용을 드릴다운할 때 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `10010` |
| `id` | string | Y | 워클로그 ID | `100028` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | N | - | `properties` 지정 시 워클로그 속성 포함 | `properties` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 워클로그 ID | `"100028"` |
| `issueId` | string | 이슈 ID | `"10002"` |
| `timeSpent` | string | 소요 시간 문자열 | `"3h 20m"` |
| `timeSpentSeconds` | integer | 소요 시간(초) | `12000` |
| `started` | string | 작업 시작 일시 | `"2021-01-17T12:34:00.000+0000"` |

```json
{
  "author": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "comment": {
    "type": "doc",
    "version": 1,
    "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "I did some work here." }] }]
  },
  "id": "100028",
  "issueId": "10002",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000",
  "started": "2021-01-17T12:34:00.000+0000",
  "timeSpent": "3h 20m",
  "timeSpentSeconds": 12000,
  "updateAuthor": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "updated": "2021-01-18T23:45:00.000+0000",
  "visibility": {
    "identifier": "276f955c-63d7-42c8-9520-92d01dca0625",
    "type": "group",
    "value": "jira-developers"
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 오류 | 토큰 재확인 |
| 404 | - | 이슈/워클로그를 찾을 수 없음 또는 열람 권한 없음, 시간 추적 비활성화 | ID·권한·설정 확인 |

## 주의 사항

- 워클로그 가시성 제한이 걸려 있으면 해당 그룹/역할이 아닌 사용자는 404를 받는다.

---

### [높음] 4. Update worklog (PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id})

## 기본 정보

- **기능:** 기존 워클로그의 내용을 수정한다.
- **Endpoint:** `PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`
- **인증:** Bearer Token 필요 (단, 익명 접근도 허용됨)
- **권한:** *Browse projects* 권한, 이슈 단위 보안 열람 권한, *Edit all worklogs*(전체 수정) 또는 *Edit own worklogs*(본인 워클로그 수정)

## 설명

워클로그의 시작 시각, 소요 시간, 코멘트 등을 갱신한다. `adjustEstimate=auto` 사용 시 기존 값과 변경 값의 차이만큼 이슈의 잔여 예상 시간이 자동 조정된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `10010` |
| `id` | string | Y | 워클로그 ID | `100028` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `notifyUsers` | boolean | N | - | watch 사용자 이메일 알림 여부 | `true` |
| `adjustEstimate` | string | N | - | 예상 시간 조정 방식: `new`/`leave`/`auto` | `auto` |
| `newEstimate` | string | N | - | `adjustEstimate=new`일 때 필수 | `2d` |
| `expand` | string | N | - | `properties` 지정 시 워클로그 속성 포함 | `properties` |
| `overrideEditableFlag` | boolean | N | - | 이슈 편집 불가 상태여도 강제 수정 (Connect/Forge + *Administer Jira* 권한 필요) | `false` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `started` | string | N | - | 작업 시작 일시 | `"2021-01-17T12:34:00.000+0000"` |
| `timeSpent` | string | N | `timeSpentSeconds`와 동시 사용 불가 | 소요 시간 | `"3h 20m"` |
| `timeSpentSeconds` | integer | N | `timeSpent`와 동시 사용 불가 | 소요 시간(초) | `12000` |
| `comment` | any | N | ADF 형식 | 작업 내용 코멘트 | 아래 예시 참조 |

```json
{
  "comment": {
    "type": "doc",
    "version": 1,
    "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "I did some work here." }] }]
  },
  "started": "2021-01-17T12:34:00.000+0000",
  "timeSpent": "3h 20m"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 워클로그 ID | `"100028"` |
| `updated` | string | 마지막 수정 시각 | `"2021-01-18T23:45:00.000+0000"` |
| `timeSpent` | string | 소요 시간 | `"3h 20m"` |

```json
{
  "author": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "comment": {
    "type": "doc",
    "version": 1,
    "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "I did some work here." }] }]
  },
  "id": "100028",
  "issueId": "10002",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000",
  "started": "2021-01-17T12:34:00.000+0000",
  "timeSpent": "3h 20m",
  "timeSpentSeconds": 12000,
  "updateAuthor": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "updated": "2021-01-18T23:45:00.000+0000",
  "visibility": {
    "identifier": "276f955c-63d7-42c8-9520-92d01dca0625",
    "type": "group",
    "value": "jira-developers"
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `adjustEstimate=new`인데 `newEstimate` 누락/오류, 권한 없음, JSON 형식 오류 | 요청 검증 |
| 401 | - | 인증 정보 오류 | 토큰 재확인 |
| 404 | - | 이슈/워클로그 없음 또는 열람 권한 없음, 시간 추적 비활성화 | ID·권한·설정 확인 |

## 주의 사항

- 본인이 작성한 워클로그가 아니면 *Edit own worklogs* 권한만으로는 수정할 수 없고 *Edit all worklogs* 권한이 필요하다.

---

### [높음] 5. Delete worklog (DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{id})

## 기본 정보

- **기능:** 이슈에서 워클로그 1건을 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`
- **인증:** Bearer Token 필요 (단, 익명 접근도 허용됨)
- **권한:** *Browse projects* 권한, 이슈 단위 보안 열람 권한, *Delete all worklogs*(전체 삭제) 또는 *Delete own worklogs*(본인 워클로그 삭제)

## 설명

지정한 워클로그를 이슈에서 제거한다. `adjustEstimate` 옵션으로 삭제 시 이슈의 잔여 예상 시간을 함께 조정할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `10010` |
| `id` | string | Y | 워클로그 ID | `100028` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `notifyUsers` | boolean | N | - | watch 사용자 이메일 알림 여부 | `true` |
| `adjustEstimate` | string | N | - | 예상 시간 조정 방식: `new`/`leave`/`manual`/`auto` | `auto` |
| `newEstimate` | string | N | - | `adjustEstimate=new`일 때 필수 | `2d` |
| `increaseBy` | string | N | - | `adjustEstimate=manual`일 때 필수, 증가시킬 양 | `2d` |
| `overrideEditableFlag` | boolean | N | - | 이슈 편집 불가 상태여도 강제 삭제 (admin 권한 필요) | `false` |

## Response

### `204 No Content`

삭제 성공 시 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `adjustEstimate=new`인데 `newEstimate` 누락/오류, `adjustEstimate=manual`인데 `reduceBy` 누락/오류, 권한 없음 | 요청 검증 |
| 401 | - | 인증 정보 오류 | 토큰 재확인 |
| 404 | - | 이슈/워클로그 없음 또는 열람 권한 없음, 시간 추적 비활성화 | ID·권한·설정 확인 |

## 주의 사항

- 삭제는 되돌릴 수 없다. UI/자동화에서 삭제 전 확인 절차를 두는 것이 권장된다.

---

### [중간] 6. Bulk delete worklogs (DELETE /rest/api/3/issue/{issueIdOrKey}/worklog)

## 기본 정보

- **기능:** 하나의 이슈에서 여러 워클로그를 한 번에 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/issue/{issueIdOrKey}/worklog`
- **인증:** Bearer Token 필요
- **권한:** *Browse projects* 권한, 이슈 단위 보안 열람 권한, *Delete all worklogs* 권한(전체 삭제 대상), 가시성 제한 시 해당 소속

## 설명

실험적(experimental) API로 한 번에 최대 5000개까지 워클로그를 삭제할 수 있다. 삭제된 워클로그에 대한 알림은 발송되지 않는다. 대량 정리 작업에 유용하지만 팀 생성/알림/일상 CRUD 핵심 흐름은 아니다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `10010` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `adjustEstimate` | string | N | - | 예상 시간 조정 방식: `leave`/`auto` | `auto` |
| `overrideEditableFlag` | boolean | N | - | 이슈 편집 불가 상태여도 강제 삭제 (admin 권한 필요) | `false` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ids` | array\<integer\> | Y | 최대 5000개 | 삭제할 워클로그 ID 목록 | `[100028, 100029]` |

```json
{
  "ids": [100028, 100029]
}
```

## Response

### `204 No Content`

전체 성공 시 본문 없이 204 반환. 부분 성공 시 200과 함께 메시지가 반환된다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 200 | - | 부분 성공 (일부만 삭제됨) | 응답 메시지로 실패 항목 확인 |
| 400 | - | `request` 누락/유효하지 않음, 권한 없음, 삭제 개수 제한 초과 | 요청 검증 |
| 401 | - | 인증 정보 오류 | 토큰 재확인 |
| 404 | - | 이슈 없음/열람 권한 없음, 워클로그가 해당 이슈 소속 아님, 시간 추적 비활성화 | ID·매핑 확인 |

## 주의 사항

- 한 번에 5000개를 초과해서 삭제할 수 없다.
- 삭제 시 알림이 전혀 발송되지 않는다.

---

### [중간] 7. Bulk move worklogs (POST /rest/api/3/issue/{issueIdOrKey}/worklog/move)

## 기본 정보

- **기능:** 워클로그 목록을 한 이슈에서 다른 이슈로 이동시킨다.
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/worklog/move`
- **인증:** Bearer Token 필요
- **권한:** 원본/대상 이슈가 속한 프로젝트에 대한 *Browse projects* 권한, 이슈 단위 보안 열람 권한, *Delete all worklogs* 권한, *Work on issues* 권한(시간 추적 전제조건), 가시성 제한 시 해당 소속

## 설명

실험적(experimental) API로 최대 5000개까지 워클로그를 이동할 수 있다. 첨부파일이 포함되거나 프로젝트 역할로 제한된 워클로그는 이동할 수 없으며, 알림/webhook/이슈 히스토리가 기록되지 않는다. 이슈 재구성 시 보조적으로 쓰인다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 원본(소스) 이슈의 ID 또는 키 | `10010` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `adjustEstimate` | string | N | - | 예상 시간 조정 방식: `leave`/`auto` | `auto` |
| `overrideEditableFlag` | boolean | N | - | 이슈 편집 불가 상태여도 강제 이동 (admin 권한 필요) | `false` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ids` | array\<integer\> | N | 최대 5000개 | 이동할 워클로그 ID 목록 | `[100028, 100029]` |
| `issueIdOrKey` | string | N | - | 이동 대상(목적지) 이슈의 ID 또는 키 | `"10011"` |

```json
{
  "ids": [100028, 100029],
  "issueIdOrKey": "10011"
}
```

## Response

### `204 No Content`

전체 성공 시 본문 없이 204 반환. 부분 성공 시 200 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 200 | - | 부분 성공 | 응답 메시지 확인 |
| 400 | - | `request` 누락/유효하지 않음, 권한 없음, 이동 개수/크기 제한 초과, 첨부파일 포함 | 요청 검증 |
| 401 | - | 인증 정보 오류 | 토큰 재확인 |
| 404 | - | 원본/대상 이슈 없음 또는 열람 권한 없음, 워클로그가 원본 이슈 소속 아님, 시간 추적 비활성화 | ID·매핑 확인 |

## 주의 사항

- 첨부파일이 포함된 워클로그나 프로젝트 역할로 제한된 워클로그는 이동 불가.
- 이동 시 알림, webhook, 이슈 히스토리가 전혀 남지 않는다.

---

### [중간] 8. Get IDs of deleted worklogs (GET /rest/api/3/worklog/deleted)

## 기본 정보

- **기능:** 특정 시각 이후 삭제된 워클로그들의 ID와 삭제 시각 목록을 반환한다.
- **Endpoint:** `GET /rest/api/3/worklog/deleted`
- **인증:** Bearer Token 필요
- **권한:** Jira 접근 권한

## 설명

사이트 전체에서 삭제된 워클로그를 폴링 방식으로 동기화할 때 사용한다. 페이지당 최대 1000개이며 `nextPage`로 다음 페이지를 가져오고 `lastPage`가 true면 마지막 페이지다. 요청 직전 1분 이내 삭제된 항목은 반환되지 않는다. 외부 시스템과의 워클로그 동기화/캐시 무효화에 보조적으로 쓰인다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `since` | integer | N | - | 이 시각(UNIX ms) 이후 삭제된 워클로그만 반환 | `1438013671562` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `lastPage` | boolean | 마지막 페이지 여부 | `true` |
| `nextPage` | string | 다음 페이지 URL | `"https://your-domain.atlassian.net/api/~ver~/worklog/deleted?since=1438013693136"` |
| `since` | integer | 조회 시작 시각 | `1438013671562` |
| `until` | integer | 페이지 내 최신 항목 시각 | `1438013693136` |
| `values` | array | 삭제된 워클로그 목록 (`worklogId`, `updatedTime`, `properties`) | 아래 참조 |

```json
{
  "lastPage": true,
  "nextPage": "https://your-domain.atlassian.net/api/~ver~/worklog/deleted?since=1438013693136",
  "self": "https://your-domain.atlassian.net/api/~ver~/worklog/deleted?since=1438013671562",
  "since": 1438013671562,
  "until": 1438013693136,
  "values": [
    { "properties": [], "updatedTime": 1438013671562, "worklogId": 103 },
    { "properties": [], "updatedTime": 1438013672165, "worklogId": 104 },
    { "properties": [], "updatedTime": 1438013693136, "worklogId": 105 }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 재확인 |

## 주의 사항

- 요청 직전 1분 이내 삭제된 항목은 이 API에 아직 반영되지 않을 수 있으므로 폴링 주기 설계 시 고려해야 한다.

---

### [중간] 9. Get worklogs (POST /rest/api/3/worklog/list)

## 기본 정보

- **기능:** 워클로그 ID 목록으로 여러 워클로그의 상세 정보를 한 번에 조회한다.
- **Endpoint:** `POST /rest/api/3/worklog/list`
- **인증:** Bearer Token 필요
- **권한:** Jira 접근 권한 (단, *Viewable by All Users*로 설정되었거나 열람 권한이 있는 프로젝트 역할/그룹 소속인 워클로그만 반환)

## 설명

여러 워클로그를 개별 조회 없이 ID 배열로 일괄 조회할 수 있다. 최대 1000개까지 반환되며, `08-Get IDs of deleted/updated worklogs`로 얻은 ID 목록의 상세 정보를 가져올 때 함께 사용하면 유용하다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | N | - | `properties` 지정 시 각 워클로그의 속성 포함 | `properties` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ids` | array\<integer\> | Y | 최대 1000개 | 조회할 워클로그 ID 목록 | `[100028]` |

```json
{
  "ids": [100028]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| (array) | array | 워클로그 객체 배열 | 아래 참조 |

```json
[
  {
    "author": {
      "accountId": "5b10a2844c20165700ede21g",
      "active": false,
      "displayName": "Mia Krystof",
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
    },
    "comment": {
      "type": "doc",
      "version": 1,
      "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "I did some work here." }] }]
    },
    "id": "100028",
    "issueId": "10002",
    "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000",
    "started": "2021-01-17T12:34:00.000+0000",
    "timeSpent": "3h 20m",
    "timeSpentSeconds": 12000,
    "updateAuthor": {
      "accountId": "5b10a2844c20165700ede21g",
      "active": false,
      "displayName": "Mia Krystof",
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
    },
    "updated": "2021-01-18T23:45:00.000+0000",
    "visibility": {
      "identifier": "276f955c-63d7-42c8-9520-92d01dca0625",
      "type": "group",
      "value": "jira-developers"
    }
  }
]
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청에 워클로그 ID가 1000개 초과 또는 비어 있음 | ID 목록 개수 조정 |
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 재확인 |

## 주의 사항

- 가시성 제한이 걸린 워클로그는 요청자가 해당 그룹/역할 소속이 아니면 결과에서 제외된다.

---

### [중간] 10. Get IDs of updated worklogs (GET /rest/api/3/worklog/updated)

## 기본 정보

- **기능:** 특정 시각 이후 업데이트된 워클로그들의 ID와 갱신 시각 목록을 반환한다.
- **Endpoint:** `GET /rest/api/3/worklog/updated`
- **인증:** Bearer Token 필요
- **권한:** Jira 접근 권한 (단, *Viewable by All Users*로 설정되었거나 열람 권한이 있는 프로젝트 역할/그룹 소속인 워클로그만 반환)

## 설명

사이트 전체에서 변경된 워클로그를 폴링 방식으로 동기화할 때 사용한다. 페이지당 최대 1000개이며 `nextPage`/`lastPage`로 페이지네이션을 처리한다. 요청 직전 1분 이내 업데이트된 항목은 반환되지 않는다. 변경분을 `09-Get worklogs`와 조합해 상세를 가져오는 흐름으로 자주 쓰인다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `since` | integer | N | - | 이 시각(UNIX ms) 이후 업데이트된 워클로그만 반환 | `1438013671562` |
| `expand` | string | N | - | `properties` 지정 시 각 워클로그의 속성 포함 | `properties` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `lastPage` | boolean | 마지막 페이지 여부 | `true` |
| `nextPage` | string | 다음 페이지 URL | `"https://your-domain.atlassian.net/api/~ver~/worklog/updated?since=1438013693136"` |
| `since` | integer | 조회 시작 시각 | `1438013671562` |
| `until` | integer | 페이지 내 최신 항목 시각 | `1438013693136` |
| `values` | array | 업데이트된 워클로그 목록 (`worklogId`, `updatedTime`, `properties`) | 아래 참조 |

```json
{
  "lastPage": true,
  "nextPage": "https://your-domain.atlassian.net/api/~ver~/worklog/updated?since=1438013693136",
  "self": "https://your-domain.atlassian.net/api/~ver~/worklog/updated?since=1438013671562",
  "since": 1438013671562,
  "until": 1438013693136,
  "values": [
    { "properties": [], "updatedTime": 1438013671562, "worklogId": 103 },
    { "properties": [], "updatedTime": 1438013672165, "worklogId": 104 },
    { "properties": [], "updatedTime": 1438013693136, "worklogId": 105 }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 없거나 잘못됨 | 토큰 재확인 |

## 주의 사항

- 요청 직전 1분 이내 업데이트된 항목은 이 API에 아직 반영되지 않을 수 있으므로 폴링 주기 설계 시 고려해야 한다.
