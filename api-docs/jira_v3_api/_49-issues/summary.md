# _49-issues API 요약

이 리소스 그룹은 Jira 이슈(및 서브태스크)의 생성/조회/수정/삭제, 상태 전환, 담당자 배정, 변경 이력(changelog) 조회, 이메일 알림 발송 등 이슈 라이프사이클 전반을 다루는 API 모음이다.

## 제외된 API

- `02-get-events-get.md` - "Administer Jira" 전역(global) 권한 필요. 사이트 전체 관리자 전용 API로 프로젝트 관리자 권한으로는 호출 불가.
- `04-archive-issue-s-by-issue-id-key-put.md` - "Jira admin or site admin" 전역 권한 필요 + Premium/Enterprise 라이선스 필요.
- `05-archive-issue-s-by-jql-post.md` - "Jira admin or site admin" 전역 권한 필요 + Premium/Enterprise 라이선스 필요.
- `11-get-issue-limit-report-get.md` - "Administer Jira" 전역 권한 필요.
- `12-unarchive-issue-s-by-issue-keys-id-put.md` - "Jira admin or site admin" 전역 권한 필요 + Premium/Enterprise 라이선스 필요.
- `23-export-archived-issue-s-put.md` - "Jira admin or site admin" 전역 권한 필요 + Premium/Enterprise 라이선스 필요.

---

### [높음] 1. Bulk fetch changelogs (POST /rest/api/3/changelog/bulkfetch)

## 기본 정보

- **기능:** 여러 이슈의 변경 이력(changelog)을 한 번에 조회하고 특정 필드로 필터링
- **Endpoint:** `POST /rest/api/3/changelog/bulkfetch`
- **인증:** Bearer Token(또는 Basic/API 토큰) 필요
- **권한:** 대상 이슈가 속한 프로젝트에 대한 *Browse projects* 권한. 이슈 단위 보안이 설정된 경우 해당 보안 권한도 필요

## 설명

최대 1000개 이슈의 changelog를 changelog 날짜와 이슈 ID 기준(오름차순)으로 정렬하여 페이지네이션된 형태로 반환한다. 이슈는 ID 또는 key로 지정하며, 최대 10개의 필드 ID로 changelog를 필터링할 수 있다. 대시보드에서 이슈 상태 변경 이력을 통합 조회할 때 유용하다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| fieldIds | string[] | N | 최대 10개 | changelog를 필터링할 필드 ID 목록 | `["fieldId"]` |
| issueIdsOrKeys | string[] | Y | 최대 1000개 | changelog를 조회할 이슈 ID/key 목록 | `["ED-1","10100"]` |
| maxResults | integer | N | | 페이지당 최대 반환 개수 | `50` |
| nextPageToken | string | N | | 페이지네이션 커서 | `"UxAQBFRF"` |

```json
{
  "fieldIds": ["fieldId"],
  "issueIdsOrKeys": ["10100"],
  "maxResults": 50,
  "nextPageToken": "UxAQBFRF"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| issueChangeLogs | array | 이슈별 changelog 목록 | - |
| issueChangeLogs[].issueId | string | 이슈 ID | `"10100"` |
| issueChangeLogs[].changeHistories | array | 변경 이력 배열 | - |
| nextPageToken | string | 다음 페이지 커서 | `"UxAQBFRF"` |

```json
{
  "issueChangeLogs": [
    {
      "issueId": "10100",
      "changeHistories": [
        {
          "id": "10001",
          "author": {
            "accountId": "5b10a2844c20165700ede21g",
            "displayName": "Mia Krystof"
          },
          "created": 1492070429,
          "items": [
            {"field": "fields", "fieldId": "fieldId", "fieldtype": "jira", "fromString": "old summary", "toString": "new summary"}
          ]
        }
      ]
    }
  ],
  "nextPageToken": "UxAQBFRF"
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | issue ID/key 미포함 또는 1000개 초과 요청 | 요청 개수를 1000개 이하로 조정 |

## 주의 사항

- 한 번에 조회 가능한 이슈는 최대 1000개, 필드 ID는 최대 10개로 제한된다.

---

### [높음] 2. Create issue (POST /rest/api/3/issue)

## 기본 정보

- **기능:** 이슈 또는 서브태스크 생성
- **Endpoint:** `POST /rest/api/3/issue`
- **인증:** Bearer Token 필요
- **권한:** 대상 프로젝트에 대한 *Browse projects*, *Create issues* 프로젝트 권한

## 설명

이슈나 서브태스크를 생성하며, 생성 시 기본 시작 상태가 아닌 다른 워크플로 단계로 전환(transition)하거나 이슈 속성을 함께 설정할 수 있다. `description`, `environment`, textarea 타입 커스텀 필드는 Atlassian Document Format(ADF)을 사용해야 한다. 서브태스크 생성 시 `issueType`을 서브태스크 타입으로, `parent`에 부모 이슈 ID/key를 지정해야 한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| updateHistory | boolean | N | - | 이슈 생성 프로젝트를 사용자의 "최근 조회" 목록에 추가할지 여부 | `true` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| fields | object | N | update와 필드 중복 불가 | 설정할 이슈 화면 필드 목록 | `{"project":{"key":"ED"},"summary":"..."}` |
| historyMetadata | any | N | | 추가 이슈 이력 정보 | - |
| properties | array | N | | 추가/수정할 이슈 속성 목록 (key, value) | `[{"key":"myprop","value":"val"}]` |
| transition | any | N | | 수행할 transition 정보 | - |
| update | object | N | fields와 필드 중복 불가 | 필드별 수행할 오퍼레이션 맵 | - |

```json
{
  "fields": {
    "project": {"key": "ED"},
    "summary": "Main order flow broken",
    "issuetype": {"name": "Bug"}
  }
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| id | string | 생성된 이슈 ID | `"10000"` |
| key | string | 생성된 이슈 key | `"ED-24"` |
| self | string | 이슈 리소스 URL | `"https://your-domain.atlassian.net/rest/api/3/issue/10000"` |

```json
{
  "id": "10000",
  "key": "ED-24",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10000",
  "transition": {"status": 200, "errorCollection": {"errorMessages": [], "errors": {}}}
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 필수 필드 누락/잘못된 값/생성 불가한 필드 포함 등 | 요청 body의 fields 값을 createmeta 기준으로 검증 |
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |
| 403 | - | 권한 없음 | Create issues 권한 확인 |
| 422 | - | 설정 문제로 생성 불가 | Jira 프로젝트/워크플로 설정 확인 |

```json
{"errorMessages": ["Field 'priority' is required"], "errors": {}}
```

## 주의 사항

- 팀 생성 자동화 및 프로젝트 운영 지원(이슈 CRUD)의 핵심 API.

---

### [높음] 3. Bulk create issue (POST /rest/api/3/issue/bulk)

## 기본 정보

- **기능:** 최대 50개의 이슈/서브태스크를 한 번에 생성
- **Endpoint:** `POST /rest/api/3/issue/bulk`
- **인증:** Bearer Token 필요
- **권한:** 각 이슈가 생성되는 프로젝트에 대한 *Browse projects*, *Create issues* 프로젝트 권한

## 설명

여러 이슈를 한 번의 요청으로 생성하며, 각 이슈에 대해 개별적으로 transition 적용과 속성 설정이 가능하다. 단일 생성 API(Create issue)와 동일한 `fields`/`update` 규칙을 따른다. 일부 이슈 생성이 실패해도 나머지는 성공할 수 있다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| issueUpdates | array | N | 최대 50개 | 생성할 이슈 정보 목록 (각 항목은 Create issue와 동일한 구조: fields, historyMetadata, properties, transition, update) | - |

```json
{
  "issueUpdates": [
    {"fields": {"project": {"key": "ED"}, "summary": "issue 1", "issuetype": {"name": "Bug"}}},
    {"fields": {"project": {"key": "ED"}, "summary": "issue 2", "issuetype": {"name": "Task"}}}
  ]
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| issues | array | 생성 성공한 이슈 목록 | `[{"id":"10000","key":"ED-24"}]` |
| errors | array | 생성 실패한 항목의 오류 정보 | `[]` |

```json
{
  "issues": [
    {"id": "10000", "key": "ED-24", "self": "https://your-domain.atlassian.net/rest/api/3/issue/10000"},
    {"id": "10001", "key": "ED-25", "self": "https://your-domain.atlassian.net/rest/api/3/issue/10001"}
  ],
  "errors": []
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 모든 요청이 유효하지 않음 | 각 issueUpdates 항목 필드값 검증 |
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |

```json
{
  "issues": [],
  "errors": [
    {"elementErrors": {"errorMessages": [], "errors": {"issuetype": "The issue type selected is invalid."}}, "failedElementNumber": 0, "status": 400}
  ]
}
```

## 주의 사항

- 팀 생성 자동화 시 초기 백로그/이슈 세트를 일괄 생성하는 데 활용 가능하다.
- 한 번에 최대 50개까지만 생성 가능하다.

---

### [높음] 4. Bulk fetch issues (POST /rest/api/3/issue/bulkfetch)

## 기본 정보

- **기능:** 여러 이슈의 상세 정보를 한 번에 조회
- **Endpoint:** `POST /rest/api/3/issue/bulkfetch`
- **인증:** 익명 접근 가능(단, 결과는 권한에 따라 필터링됨). 일반적으로 Bearer Token 사용 권장
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 권한. 이슈 단위 보안 설정 시 해당 권한도 필요

## 설명

최대 100개의 이슈를 ID 또는 key로 조회한다. 식별자가 일치하지 않으면 대소문자 무시 검색 및 이동된 이슈 확인을 수행한다. 결과는 `id` 오름차순으로 반환되며, 조회 실패한 이슈는 `issueErrors`에 별도로 담긴다. 통합 대시보드에서 여러 이슈 상태를 한 번에 가져올 때 유용하다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| expand | string[] | N | | 추가 정보 확장 옵션 (`renderedFields`, `names`, `schema`, `transitions`, `operations`, `editmeta`, `changelog`, `versionedRepresentations`) | `["names"]` |
| fields | string[] | N | | 반환할 필드 목록, 기본값은 `*navigable` | `["summary","comment"]` |
| fieldsByKeys | boolean | N | false | 필드를 key로 참조할지 여부 | `false` |
| issueIdsOrKeys | string[] | Y | 최대 100개 | 조회할 이슈 ID/key 배열 | `["EX-1","EX-2"]` |
| properties | string[] | N | 최대 5개 | 포함할 이슈 속성 키 목록 | `["prop1"]` |

```json
{
  "issueIdsOrKeys": ["EX-1", "EX-2"],
  "fields": ["summary", "assignee"]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| expand | string | 확장 정보 | `"schema,names"` |
| issues | array | 조회된 이슈 목록 | - |
| issueErrors | array | 조회 실패한 이슈 오류 목록 | `[]` |

```json
{
  "expand": "schema,names",
  "issueErrors": [],
  "issues": [
    {
      "id": "10002",
      "key": "EX-1",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002",
      "fields": {"summary": "My first example issue"}
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 이슈 ID/key 미포함 또는 100개 초과 요청 | 요청 개수 조정 |
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |

## 주의 사항

- 통합 대시보드에서 다건 이슈 상태 조회에 적합하다. 최대 100개 제한에 유의.

---

### [높음] 5. Get issue (GET /rest/api/3/issue/{issueIdOrKey})

## 기본 정보

- **기능:** 단일 이슈의 상세 정보 조회
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 권한. 이슈 단위 보안 설정 시 해당 권한도 필요

## 설명

이슈 ID 또는 key로 상세 정보를 조회한다. 식별자가 일치하지 않으면 대소문자 무시 검색과 이동된 이슈 확인을 수행하며, 매칭되면 302 리다이렉트 없이 바로 상세 정보를 반환한다. 통합 알림/대시보드에서 이슈 상태, 코멘트, 워처, 첨부파일 등을 조회하는 핵심 API다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 이슈의 ID 또는 key | `"EX-1"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| fields | array | N | 전체 필드 | 반환할 필드 목록(콤마 구분) | `"summary,comment"` |
| fieldsByKeys | boolean | N | false | 필드를 key로 참조할지 여부 | `false` |
| expand | string | N | - | 추가 정보 확장(renderedFields, names, schema, transitions, editmeta, changelog, versionedRepresentations) | `"changelog"` |
| properties | array | N | - | 반환할 이슈 속성 목록 | `"*all"` |
| updateHistory | boolean | N | - | 최근 조회 프로젝트 목록에 추가할지 여부 | `true` |
| failFast | boolean | N | false | 필드 로드 실패 시 즉시 실패할지 여부 | `false` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| id | string | 이슈 ID | `"10002"` |
| key | string | 이슈 key | `"ED-1"` |
| self | string | 이슈 리소스 URL | `"https://your-domain.atlassian.net/rest/api/3/issue/10002"` |
| fields | object | 이슈 필드 값(watcher, attachment, comment, issuelinks, worklog 등) | - |

```json
{
  "id": "10002",
  "key": "ED-1",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10002",
  "fields": {
    "watcher": {"isWatching": false, "watchCount": 1},
    "description": {"type": "doc", "version": 1, "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Main order flow broken"}]}]},
    "comment": [
      {"id": "10000", "author": {"displayName": "Mia Krystof"}, "created": "2021-01-17T12:34:00.000+0000"}
    ]
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |
| 404 | - | 이슈를 찾을 수 없거나 조회 권한 없음 | 이슈 ID/key 및 권한 확인 |

## 주의 사항

- 통합 알림/대시보드의 "원문 링크 제공" 기능에서 이슈 상세를 가져오는 데 핵심적으로 사용된다.

---

### [높음] 6. Edit issue (PUT /rest/api/3/issue/{issueIdOrKey})

## 기본 정보

- **기능:** 이슈 필드 수정
- **Endpoint:** `PUT /rest/api/3/issue/{issueIdOrKey}`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 대상 프로젝트에 대한 *Browse projects*, *Edit issues* 프로젝트 권한

## 설명

이슈 필드와 속성을 수정한다. 이슈 상태 전환(transition)은 이 API에서 지원하지 않으며 무시되므로 Transition issue API를 별도로 사용해야 한다. `description`, `environment`, textarea 타입 커스텀 필드는 ADF 콘텐츠를 사용해야 한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 이슈의 ID 또는 key | `"EX-1"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| notifyUsers | boolean | N | - | 워처에게 수정 알림 이메일 발송 여부 | `true` |
| overrideScreenSecurity | boolean | N | - | 화면 보안 설정을 무시하고 숨겨진 필드 수정 허용(Connect/Forge 앱 전용) | `false` |
| overrideEditableFlag | boolean | N | - | 편집 불가 필드 수정 허용(Connect/Forge 앱 전용) | `false` |
| returnIssue | boolean | N | - | 응답에 수정된 이슈 반환 여부 | `true` |
| expand | string | N | - | returnIssue가 true일 때 사용할 expand 옵션 | `"names"` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| fields | object | N | update와 중복 불가 | 수정할 필드 목록 | `{"summary": "새 요약"}` |
| historyMetadata | any | N | | 추가 이력 정보 | - |
| properties | array | N | | 추가/수정할 이슈 속성 | `[{"key":"myprop","value":"val"}]` |
| transition | any | N | 이 API에서는 무시됨 | transition 정보 | - |
| update | object | N | fields와 중복 불가 | 필드별 오퍼레이션 맵 | - |

```json
{ "fields": { "summary": "새 이슈 요약" } }
```

## Response

### `200 OK` (returnIssue=true인 경우)

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| - | any | Get issue API와 동일한 형식의 이슈 객체 | - |

### `204 No Content`

수정 성공 시 본문 없이 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청 body 누락, 권한 부족, 존재하지 않는 필드 포함, 잘못된 transition 포함 | 요청 필드를 editmeta 기준으로 검증 |
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |
| 403 | - | override 파라미터 사용 권한 없음 | 관리자 권한 필요 여부 확인 |
| 404 | - | 이슈 없음/조회 권한 없음 | 이슈 ID/key 확인 |
| 409 | - | 충돌하는 업데이트 | 재시도 |
| 422 | - | 설정 문제로 수정 불가 | 프로젝트/워크플로 설정 확인 |

## 주의 사항

- 이슈 상태 전환은 별도의 Transition issue API를 사용해야 한다.

---

### [높음] 7. Delete issue (DELETE /rest/api/3/issue/{issueIdOrKey})

## 기본 정보

- **기능:** 이슈 삭제
- **Endpoint:** `DELETE /rest/api/3/issue/{issueIdOrKey}`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 대상 프로젝트에 대한 *Browse projects*, *Delete issues* 프로젝트 권한

## 설명

이슈를 삭제한다. 서브태스크가 있는 이슈는 `deleteSubtasks`를 설정하지 않으면 삭제할 수 없다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 이슈의 ID 또는 key | `"EX-1"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| deleteSubtasks | string | N | - | 삭제 시 서브태스크도 함께 삭제할지 여부 | `"true"` |

## Response

### `204 No Content`

삭제 성공 시 본문 없이 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 서브태스크가 있는데 deleteSubtasks가 true가 아님 | deleteSubtasks=true로 재요청 |
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |
| 403 | - | 삭제 권한 없음 | Delete issues 권한 확인 |
| 404 | - | 이슈 없음/조회 권한 없음 | 이슈 ID/key 확인 |

## 주의 사항

- 서브태스크가 있는 이슈는 `deleteSubtasks=true`를 명시하지 않으면 삭제가 실패한다.

---

### [높음] 8. Assign issue (PUT /rest/api/3/issue/{issueIdOrKey}/assignee)

## 기본 정보

- **기능:** 이슈에 담당자 배정
- **Endpoint:** `PUT /rest/api/3/issue/{issueIdOrKey}/assignee`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 대상 프로젝트에 대한 *Browse Projects*, *Assign Issues* 프로젝트 권한

## 설명

*Edit Issues* 권한이 없어도 *Assign issue* 권한만 있으면 담당자를 배정할 수 있다. `accountId`가 `"-1"`이면 프로젝트 기본 담당자로, `null`이면 담당자 없음으로 설정된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 배정할 이슈의 ID 또는 key | `"EX-1"` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| accountId | string | Y(요청상) | | 담당자로 지정할 사용자의 계정 ID. `"-1"`은 기본 담당자, `null`은 담당자 해제 | `"5b10ac8d82e05b22cc7d4ef5"` |
| accountType | enum | N | atlassian/app/customer/unknown | 사용자 계정 유형 | `"atlassian"` |
| active | boolean | N | | 사용자 활성 여부 | `true` |
| displayName | string | N | | 사용자 표시 이름 | `"Mia Krystof"` |
| emailAddress | string | N | | 사용자 이메일 | `"mia@example.com"` |

```json
{ "accountId": "5b10ac8d82e05b22cc7d4ef5" }
```

## Response

### `204 No Content`

배정 성공 시 본문 없이 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 사용자를 찾을 수 없음, accountId 누락, name/key/accountId 중복 제공 | accountId만 단독으로 전달 |
| 403 | - | 권한 없음 | Assign Issues 권한 확인 |
| 404 | - | 이슈 없음 | 이슈 ID/key 확인 |

## 주의 사항

- 팀 생성 자동화 후 이슈 자동 배정, 워크플로 자동화에 활용 가능하다.

---

### [높음] 9. Get changelogs (GET /rest/api/3/issue/{issueIdOrKey}/changelog)

## 기본 정보

- **기능:** 단일 이슈의 변경 이력(changelog) 페이지네이션 조회
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/changelog`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 권한. 이슈 단위 보안 설정 시 해당 권한도 필요

## 설명

특정 이슈의 changelog를 날짜순(오래된 순)으로 페이지네이션하여 반환한다. 통합 알림/대시보드에서 개별 이슈의 변경 이력을 조회하는 데 사용된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 이슈의 ID 또는 key | `"TT-1"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| startAt | integer | N | 0 | 페이지 시작 인덱스 | `2` |
| maxResults | integer | N | - | 페이지당 최대 반환 개수 | `2` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| isLast | boolean | 마지막 페이지 여부 | `false` |
| maxResults | integer | 페이지당 최대 개수 | `2` |
| startAt | integer | 페이지 시작 인덱스 | `2` |
| total | integer | 전체 changelog 개수 | `5` |
| values | array | changelog 항목 목록 | - |

```json
{
  "isLast": false,
  "maxResults": 2,
  "startAt": 2,
  "total": 5,
  "values": [
    {
      "id": "10001",
      "author": {"accountId": "5b10a2844c20165700ede21g", "displayName": "Mia Krystof"},
      "created": "1970-01-18T06:27:50.429+0000",
      "items": [{"field": "fields", "fieldtype": "jira", "fieldId": "fieldId", "fromString": "", "toString": "label-1"}]
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 404 | - | 이슈 없음/조회 권한 없음 | 이슈 ID/key 확인 |

## 주의 사항

- 단일 이슈용이며, 다건 조회는 Bulk fetch changelogs API를 사용한다.

---

### [높음] 10. Get changelogs by IDs (POST /rest/api/3/issue/{issueIdOrKey}/changelog/list)

## 기본 정보

- **기능:** changelog ID 목록으로 특정 changelog들만 조회
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/changelog/list`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 권한. 이슈 단위 보안 설정 시 해당 권한도 필요

## 설명

특정 changelog ID 목록으로 이슈의 변경 이력을 조회한다. 전체 changelog 중 일부만 필요한 경우 유용하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 이슈의 ID 또는 key | `"TT-1"` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| changelogIds | integer[] | Y | | 조회할 changelog ID 목록 | `[10001, 10002]` |

```json
{ "changelogIds": [10001, 10002] }
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| histories | array | changelog 항목 목록 | - |
| maxResults | integer | 반환된 최대 개수 | `2` |
| startAt | integer | 시작 인덱스 | `0` |
| total | integer | 전체 개수 | `2` |

```json
{
  "histories": [
    {"id": "10001", "author": {"displayName": "Mia Krystof"}, "created": "1970-01-18T06:27:50.429+0000", "items": [{"field": "fields", "fromString": "", "toString": "label-1"}]}
  ],
  "maxResults": 2,
  "startAt": 0,
  "total": 2
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | changelogIds 값 확인 |
| 404 | - | 이슈 없음/권한 없음 | 이슈 ID/key 확인 |

## 주의 사항

- 없음.

---

### [높음] 11. Send notification for issue (POST /rest/api/3/issue/{issueIdOrKey}/notify)

## 기본 정보

- **기능:** 이슈에 대한 이메일 알림 생성 및 발송 큐 등록
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/notify`
- **인증:** Bearer Token 필요
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse Projects* 프로젝트 권한. 이슈 단위 보안 설정 시 해당 권한도 필요

## 설명

특정 이슈에 대해 이메일 알림을 생성해 메일 큐에 등록한다. 수신자, 제목, 본문(HTML/텍스트)을 지정할 수 있으며 특정 권한을 가진 사용자로 수신을 제한할 수 있다. 통합 알림 기능에서 Mattermost 외 이메일 채널로도 알림을 보낼 때 활용 가능하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 알림을 보낼 이슈의 ID 또는 key | `"EX-1"` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| htmlBody | string | N | | 이메일 HTML 본문 | `"<p>이슈가 업데이트 되었습니다</p>"` |
| restrict | any | N | | 특정 권한을 가진 사용자로 수신 제한 | - |
| subject | string | N | 미지정 시 이슈 key+요약 | 이메일 제목 | `"이슈 업데이트 안내"` |
| textBody | string | N | | 이메일 텍스트 본문 | `"이슈가 업데이트 되었습니다"` |
| to | any | N | | 수신자 정보 | - |

```json
{
  "subject": "이슈 업데이트 안내",
  "textBody": "이슈가 업데이트 되었습니다.",
  "to": { "reporter": true, "assignee": true }
}
```

## Response

### `204 No Content`

이메일 큐 등록 성공 시 본문 없이 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 수신자가 호출자 본인, 수신자 정보 잘못됨, 이슈 ID 잘못됨, 필수 필드 누락 | 수신자/필드 값 확인 |
| 403 | - | 외부 이메일 발송 비활성화, SMTP 서버 미설정 | Jira 이메일 설정 확인 |
| 404 | - | 이슈 없음 | 이슈 ID/key 확인 |

## 주의 사항

- 없음.

---

### [높음] 12. Get transitions (GET /rest/api/3/issue/{issueIdOrKey}/transitions)

## 기본 정보

- **기능:** 이슈에서 수행 가능한 상태 전환(transition) 목록 조회
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/transitions`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 권한. *Transition issues* 권한이 없으면 빈 목록 반환

## 설명

이슈의 현재 상태 기준으로 전체 또는 특정 transition 정보를 반환한다. 상태 전환 UI를 만들거나 자동화 워크플로에서 다음 가능한 상태를 파악할 때 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 이슈의 ID 또는 key | `"EX-1"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| expand | string | N | - | `transitions.fields` 지정 시 전환 화면 필드 정보 포함 | `"transitions.fields"` |
| transitionId | string | N | - | 특정 transition ID | `"711"` |
| skipRemoteOnlyCondition | boolean | N | - | Hide From User Condition이 걸린 transition 포함 여부(Connect/Forge 전용) | `false` |
| includeUnavailableTransitions | boolean | N | - | 조건 실패한 transition도 포함할지 여부 | `false` |
| sortByOpsBarAndStatus | boolean | N | - | ops-bar 순서/상태 카테고리 기준 정렬 여부 | `false` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| transitions | array | 가능한 transition 목록 | - |
| transitions[].id | string | transition ID | `"2"` |
| transitions[].name | string | transition 이름 | `"Close Issue"` |
| transitions[].to | object | 전환될 상태 정보 | `{"id":"10000","name":"In Progress"}` |

```json
{
  "transitions": [
    {
      "id": "2",
      "name": "Close Issue",
      "hasScreen": false,
      "isAvailable": true,
      "to": {"id": "10000", "name": "In Progress"}
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |
| 404 | - | 이슈 없음/권한 없음 | 이슈 ID/key 확인 |

## 주의 사항

- *Transition issues* 권한이 없으면 빈 목록이 반환되므로 오류로 오인하지 않도록 주의.

---

### [높음] 13. Transition issue (POST /rest/api/3/issue/{issueIdOrKey}/transitions)

## 기본 정보

- **기능:** 이슈 상태 전환 수행
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/transitions`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 대상 프로젝트에 대한 *Browse projects*, *Transition issues* 프로젝트 권한

## 설명

이슈의 상태를 전환하며, 전환 화면(screen)이 있는 경우 `fields`나 `update`로 해당 화면의 필드도 함께 갱신한다. 전환 가능한 필드 정보는 Get transitions API의 `transitions.fields` expand로 확인한다. 프로젝트 운영 지원(상태 전환 자동화)의 핵심 API다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 이슈의 ID 또는 key | `"EX-1"` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| fields | object | N | update와 중복 불가 | 전환 화면의 필드 값 | `{"resolution": {"name": "Fixed"}}` |
| historyMetadata | any | N | | 추가 이력 정보 | - |
| properties | array | N | | 추가/수정할 이슈 속성 | - |
| transition | any | Y | | 수행할 transition 정보(id 등) | `{"id": "2"}` |
| update | object | N | fields와 중복 불가 | 필드별 오퍼레이션 맵 | - |

```json
{
  "transition": { "id": "2" },
  "fields": { "resolution": { "name": "Fixed" } }
}
```

## Response

### `204 No Content`

전환 성공 시 본문 없이 반환.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | transition 미지정, 권한 없음, 화면에 없는 필드 지정, fields/update 중복 지정 | 요청 body 검증 |
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |
| 404 | - | 이슈 없음/권한 없음 | 이슈 ID/key 확인 |
| 409 | - | 충돌하는 업데이트 | 재시도 |
| 413 | - | 코멘트/워크로그/첨부파일/이슈링크 등 이슈별 한도 초과 | 한도 확인 후 재요청 |
| 422 | - | 설정 문제로 생성 불가 | 프로젝트/워크플로 설정 확인 |

## 주의 사항

- 프로젝트 운영 지원의 상태 전환 자동화 흐름에서 핵심적으로 사용된다.

---

### [중간] 14. Get create issue metadata (GET /rest/api/3/issue/createmeta)

## 기본 정보

- **기능:** 이슈 생성에 필요한 프로젝트/이슈타입/필드 메타데이터 조회 (Deprecated)
- **Endpoint:** `GET /rest/api/3/issue/createmeta`
- **인증:** 익명 접근 가능
- **권한:** 요청 대상 프로젝트에 대한 *Create issues* 프로젝트 권한

## 설명

Create issue/Bulk create issue 요청을 구성하는 데 필요한 프로젝트, 이슈 타입, 생성 화면 필드 정보를 반환한다. Atlassian 공식 문서에 따르면 Deprecated 상태이며, 향후 프로젝트별/이슈타입별 개별 엔드포인트(09, 10번) 사용이 권장된다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| projectIds | array | N | - | 프로젝트 ID 목록(콤마 구분) | `"10000,10001"` |
| projectKeys | array | N | - | 프로젝트 key 목록(콤마 구분) | `"proj1,proj2"` |
| issuetypeIds | array | N | - | 이슈 타입 ID 목록 | `"10000,10001"` |
| issuetypeNames | array | N | - | 이슈 타입 이름 목록 | `"name1,name2"` |
| expand | string | N | - | `projects.issuetypes.fields` 지정 시 생성 화면 필드 정보 포함 | `"projects.issuetypes.fields"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| projects | array | 프로젝트별 이슈 타입/필드 메타데이터 | - |

```json
{
  "projects": [
    {
      "id": "10000",
      "key": "ED",
      "name": "Edison Project",
      "issuetypes": [
        {"id": "1", "name": "Bug", "description": "An error in the code", "subtask": false}
      ]
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |

## 주의 사항

- Deprecated API. 신규 구현 시 09/10번 엔드포인트 사용을 우선 검토할 것.

---

### [중간] 15. Get create metadata issue types for a project (GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes)

## 기본 정보

- **기능:** 특정 프로젝트의 이슈 타입 메타데이터 페이지 조회
- **Endpoint:** `GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes`
- **인증:** 익명 접근 가능
- **권한:** 요청 대상 프로젝트에 대한 *Create issues* 프로젝트 권한

## 설명

Create issue/Bulk create issue 요청 구성을 위해 특정 프로젝트에서 사용 가능한 이슈 타입 목록을 페이지네이션으로 반환한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| projectIdOrKey | string | Y | 프로젝트 ID 또는 key | `"ED"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| startAt | integer | N | 0 | 페이지 시작 인덱스 | `0` |
| maxResults | integer | N | - | 페이지당 최대 반환 개수(최대 200) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| issueTypes | array | 이슈 타입 목록 | - |
| maxResults | integer | 페이지당 최대 개수 | `1` |
| startAt | integer | 시작 인덱스 | `0` |
| total | integer | 전체 개수 | `1` |

```json
{
  "issueTypes": [
    {"id": "1", "name": "Bug", "description": "An error in the code", "subtask": false}
  ],
  "maxResults": 1,
  "startAt": 0,
  "total": 1
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | maxResults가 한도(200) 초과 등 잘못된 요청 | 파라미터 값 조정 |
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |

## 주의 사항

- 없음.

---

### [중간] 16. Get create field metadata for a project and issue type id (GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId})

## 기본 정보

- **기능:** 특정 프로젝트/이슈타입의 생성 화면 필드 메타데이터 조회
- **Endpoint:** `GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}`
- **인증:** 익명 접근 가능
- **권한:** 요청 대상 프로젝트에 대한 *Create issues* 프로젝트 권한

## 설명

특정 프로젝트와 이슈 타입 조합에서 이슈 생성 화면에 노출되는 필드 메타데이터를 페이지네이션으로 반환한다. Create issue 요청의 `fields`/`update` 값을 구성하는 데 사용한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| projectIdOrKey | string | Y | 프로젝트 ID 또는 key | `"ED"` |
| issueTypeId | string | Y | 이슈 타입 ID | `"1"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| startAt | integer | N | 0 | 페이지 시작 인덱스 | `0` |
| maxResults | integer | N | - | 페이지당 최대 반환 개수(최대 200) | `50` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| fields | array | 필드 메타데이터 목록 | - |
| maxResults | integer | 페이지당 최대 개수 | `1` |
| startAt | integer | 시작 인덱스 | `0` |
| total | integer | 전체 개수 | `1` |

```json
{
  "fields": [
    {"fieldId": "assignee", "name": "Assignee", "required": true, "hasDefaultValue": false, "operations": ["set"]}
  ],
  "maxResults": 1,
  "startAt": 0,
  "total": 1
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | maxResults가 한도(200) 초과 등 잘못된 요청 | 파라미터 값 조정 |
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |

## 주의 사항

- 없음.

---

### [중간] 17. Get edit issue metadata (GET /rest/api/3/issue/{issueIdOrKey}/editmeta)

## 기본 정보

- **기능:** 이슈 편집 화면에서 사용자가 보고 수정할 수 있는 필드 메타데이터 조회
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/editmeta`
- **인증:** 익명 접근 가능(비공개 프로젝트는 인증 필요)
- **권한:** 이슈가 속한 프로젝트에 대한 *Browse projects* 권한(필드를 실제로 수정하려면 *Edit issues* 권한 필요)

## 설명

Edit issue API 요청을 구성하기 위해 현재 사용자가 편집 가능한 필드 목록과 각 필드의 제약 조건(허용 값, 필수 여부 등)을 반환한다. 화면/필드 구성/워크플로 조건 등 여러 단계를 검사해 최종 편집 가능 필드를 결정한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| issueIdOrKey | string | Y | 이슈의 ID 또는 key | `"EX-1"` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| overrideScreenSecurity | boolean | N | - | 숨겨진 필드도 반환할지 여부(Connect/Forge 전용) | `false` |
| overrideEditableFlag | boolean | N | - | 편집 불가 필드도 반환할지 여부(Connect/Forge 전용) | `false` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| fields | object | 필드별 편집 메타데이터(허용 값, 기본값, 필수 여부, 오퍼레이션 등) | - |

```json
{
  "fields": {
    "summary": {
      "required": false,
      "name": "My Multi Select",
      "key": "field_key",
      "operations": ["set", "add"],
      "allowedValues": ["red", "blue"]
    }
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보 없음/오류 | 인증 토큰 확인 |
| 403 | - | override 파라미터 사용 권한 없음 | 관리자 권한 필요 여부 확인 |
| 404 | - | 이슈 없음/권한 없음 | 이슈 ID/key 확인 |

## 주의 사항

- 실제로 필드를 수정하려면 *Edit issues* 프로젝트 권한이 별도로 필요하다.
