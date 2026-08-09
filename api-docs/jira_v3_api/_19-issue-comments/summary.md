# _19-issue-comments API 요약

이 리소스 그룹은 Jira 이슈의 코멘트(comment)를 조회·생성·수정·삭제하는 API 모음이다. 이슈 하나의 코멘트 전체 조회, 코멘트 ID 목록으로 일괄 조회, 단일 코멘트 CRUD를 제공한다.

## 제외된 API

없음 (모든 엔드포인트가 프로젝트 권한(Browse projects, Add/Edit/Delete comments 등) 수준으로 호출 가능하며, 사이트 전체 관리자 권한이 필수인 API는 없음).

---

### [높음] 1. 이슈의 코멘트 전체 조회 (GET /rest/api/3/issue/{issueIdOrKey}/comment)

## 기본 정보

- **기능:** 특정 이슈에 달린 모든 코멘트를 페이지 단위로 조회한다.
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/comment`
- **인증:** Bearer Token 필요 (익명 접근도 가능하나 프로젝트 공개 설정에 따라 제한됨)
- **권한:** 프로젝트의 *Browse projects* 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한. 코멘트에 가시성 제한이 있는 경우 해당 그룹/역할 소속 필요.

## 설명

통합 대시보드에서 이슈 상세를 보여줄 때 코멘트 목록을 가져오는 데 핵심적으로 쓰인다. `orderBy`로 생성일 기준 정렬이 가능하고, `startAt`/`maxResults`로 페이지네이션을 지원한다. `expand=renderedBody`를 사용하면 HTML로 렌더링된 코멘트 본문도 함께 받을 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Yes | 이슈의 ID 또는 키 | `10010` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `startAt` | integer | No | - | 페이지 결과의 시작 인덱스(오프셋) | `0` |
| `maxResults` | integer | No | - | 페이지당 최대 반환 개수 | `50` |
| `orderBy` | string | No | - | 정렬 기준 필드. `created`만 허용 | `created` |
| `expand` | string | No | - | 추가 정보 포함. `renderedBody`(HTML 렌더링 본문) 지원 | `renderedBody` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `comments` | array | 코멘트 객체 배열 | - |
| `comments[].author` | object | 작성자 정보 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `comments[].body` | object | Atlassian Document Format 본문 | `{"type":"doc","version":1,"content":[...]}` |
| `comments[].created` | string | 생성 일시 | `2021-01-17T12:34:00.000+0000` |
| `comments[].id` | string | 코멘트 ID | `10000` |
| `comments[].self` | string | 코멘트 URL | `https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000` |
| `comments[].updateAuthor` | object | 최종 수정자 정보 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `comments[].updated` | string | 최종 수정 일시 | `2021-01-18T23:45:00.000+0000` |
| `comments[].visibility` | object | 코멘트 가시성 제한 | `{"identifier":"Administrators","type":"role","value":"Administrators"}` |
| `maxResults` | integer | 페이지당 최대 개수 | `1` |
| `startAt` | integer | 시작 오프셋 | `0` |
| `total` | integer | 전체 코멘트 수 | `1` |

```json
{
  "comments": [
    {
      "author": {
        "accountId": "5b10a2844c20165700ede21g",
        "active": false,
        "displayName": "Mia Krystof",
        "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
      },
      "body": {
        "type": "doc",
        "version": 1,
        "content": [
          {
            "type": "paragraph",
            "content": [
              { "type": "text", "text": "Lorem ipsum dolor sit amet..." }
            ]
          }
        ]
      },
      "created": "2021-01-17T12:34:00.000+0000",
      "id": "10000",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000",
      "updateAuthor": {
        "accountId": "5b10a2844c20165700ede21g",
        "active": false,
        "displayName": "Mia Krystof",
        "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
      },
      "updated": "2021-01-18T23:45:00.000+0000",
      "visibility": {
        "identifier": "Administrators",
        "type": "role",
        "value": "Administrators"
      }
    }
  ],
  "maxResults": 1,
  "startAt": 0,
  "total": 1
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `orderBy`가 `created` 외의 값으로 설정됨 | `orderBy` 값을 `created` 또는 생략으로 수정 |
| 401 | - | 인증 정보가 잘못되었거나 없음 | 토큰 재발급/재인증 |
| 404 | - | 이슈를 찾을 수 없거나 조회 권한 없음 | 이슈 키/ID 및 권한 확인 |

## 주의 사항

- 익명 접근이 가능하지만 프로젝트/이슈 보안 설정에 따라 결과가 제한될 수 있다.
- 코멘트에 가시성 제한(role/group)이 걸려 있으면 해당 권한이 없는 사용자에게는 응답에서 제외된다.

---

### [높음] 2. 이슈에 코멘트 추가 (POST /rest/api/3/issue/{issueIdOrKey}/comment)

## 기본 정보

- **기능:** 지정한 이슈에 새 코멘트를 추가한다.
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/comment`
- **인증:** Bearer Token 필요 (익명 접근 가능하나 일반적으로 인증 필요)
- **권한:** 프로젝트의 *Browse projects* 및 *Add comments* 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한.

## 설명

프로젝트 운영 지원 자동화(예: 상태 전환 시 자동 코멘트 남기기, 다른 도구의 이벤트를 Jira 코멘트로 동기화)에 핵심적으로 사용된다. 본문은 Atlassian Document Format(ADF)으로 작성해야 하며, `visibility`로 특정 그룹/역할에만 보이도록 제한할 수 있다. 이슈당 코멘트/첨부파일 개수 제한을 초과하면 413 에러가 발생한다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Yes | 이슈의 ID 또는 키 | `10010` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | No | - | 추가 정보 포함. `renderedBody`(HTML 렌더링 본문) 지원 | `renderedBody` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `body` | any (ADF) | No | Atlassian Document Format | 코멘트 본문 텍스트 | `{"type":"doc","version":1,"content":[...]}` |
| `visibility` | any | No | - | 코멘트를 볼 수 있는 그룹/역할 제한 (생성 시 선택) | `{"type":"role","value":"Administrators"}` |
| `jsdPublic` | boolean | No | 기본값 true | Jira Service Desk에서 코멘트 공개 여부 | `true` |
| `properties` | array | No | - | 코멘트 속성 목록 | `[{"key":"a","value":"b"}]` |

```json
{
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          { "type": "text", "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit." }
        ]
      }
    ]
  },
  "visibility": {
    "identifier": "Administrators",
    "type": "role",
    "value": "Administrators"
  }
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `author` | object | 작성자 정보 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `body` | object | 등록된 코멘트 본문(ADF) | `{"type":"doc","version":1,...}` |
| `created` | string | 생성 일시 | `2021-01-17T12:34:00.000+0000` |
| `id` | string | 코멘트 ID | `10000` |
| `self` | string | 코멘트 URL | `https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000` |
| `updateAuthor` | object | 최종 수정자 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `updated` | string | 최종 수정 일시 | `2021-01-18T23:45:00.000+0000` |
| `visibility` | object | 가시성 제한 | `{"identifier":"Administrators","type":"role","value":"Administrators"}` |

```json
{
  "author": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          { "type": "text", "text": "Lorem ipsum dolor sit amet..." }
        ]
      }
    ]
  },
  "created": "2021-01-17T12:34:00.000+0000",
  "id": "10000",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000",
  "updateAuthor": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "updated": "2021-01-18T23:45:00.000+0000",
  "visibility": {
    "identifier": "Administrators",
    "type": "role",
    "value": "Administrators"
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 잘못됨 | 요청 본문(ADF 형식 등) 검증 |
| 401 | - | 인증 정보가 잘못됨 | 토큰 재발급/재인증 |
| 404 | - | 이슈를 찾을 수 없거나 조회 권한 없음 | 이슈 키/ID 및 권한 확인 |
| 413 | - | 이슈당 코멘트 또는 첨부파일 개수 제한 초과 | 코멘트/첨부파일 정리 후 재시도 |

## 주의 사항

- 본문은 반드시 Atlassian Document Format(ADF)으로 작성해야 한다.
- Jira Service Desk 프로젝트가 아니면 `jsdPublic` 관련 설정은 의미가 없다.

---

### [높음] 3. 단일 코멘트 조회 (GET /rest/api/3/issue/{issueIdOrKey}/comment/{id})

## 기본 정보

- **기능:** 이슈에 달린 특정 코멘트 하나를 조회한다.
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/comment/{id}`
- **인증:** Bearer Token 필요 (익명 접근 가능)
- **권한:** 프로젝트의 *Browse projects* 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한. 코멘트 가시성 제한이 있는 경우 해당 그룹/역할 소속 필요.

## 설명

webhook 이벤트(예: comment_created)로 코멘트 ID만 전달받았을 때, 해당 코멘트의 상세 내용을 조회해 알림/대시보드에 표시하는 데 사용된다. 단일 코멘트 조회이므로 페이지네이션이 없다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Yes | 이슈의 ID 또는 키 | `10010` |
| `id` | string | Yes | 코멘트 ID | `10000` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | No | - | 추가 정보 포함. `renderedBody`(HTML 렌더링 본문) 지원 | `renderedBody` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `author` | object | 작성자 정보 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `body` | object | 코멘트 본문(ADF) | `{"type":"doc","version":1,...}` |
| `created` | string | 생성 일시 | `2021-01-17T12:34:00.000+0000` |
| `id` | string | 코멘트 ID | `10000` |
| `self` | string | 코멘트 URL | `https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000` |
| `updateAuthor` | object | 최종 수정자 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `updated` | string | 최종 수정 일시 | `2021-01-18T23:45:00.000+0000` |
| `visibility` | object | 가시성 제한 | `{"identifier":"Administrators","type":"role","value":"Administrators"}` |

```json
{
  "author": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          { "type": "text", "text": "Lorem ipsum dolor sit amet..." }
        ]
      }
    ]
  },
  "created": "2021-01-17T12:34:00.000+0000",
  "id": "10000",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000",
  "updateAuthor": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "updated": "2021-01-18T23:45:00.000+0000",
  "visibility": {
    "identifier": "Administrators",
    "type": "role",
    "value": "Administrators"
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 잘못되었거나 없음 | 토큰 재발급/재인증 |
| 404 | - | 이슈 또는 코멘트를 찾을 수 없거나 조회 권한 없음 | 이슈/코멘트 ID 및 권한 확인 |

## 주의 사항

- 코멘트 가시성 제한이 걸린 경우 조회 권한이 없으면 404가 반환된다.

---

### [높음] 4. 코멘트 수정 (PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id})

## 기본 정보

- **기능:** 이슈에 달린 기존 코멘트의 내용을 수정한다.
- **Endpoint:** `PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}`
- **인증:** Bearer Token 필요 (익명 접근 가능)
- **권한:** 프로젝트의 *Browse projects* 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한. *Edit all comments* 권한(모든 코멘트 수정) 또는 *Edit own comments* 권한(본인 작성 코멘트만 수정).

## 설명

기존 코멘트를 정정하거나 자동화 도구가 남긴 상태 코멘트를 갱신할 때 사용한다. 자식 코멘트(child comment)는 부모 코멘트의 가시성을 상속받으므로, 자식 코멘트의 `visibility`를 변경하려 하면 400 에러가 발생한다. `overrideEditableFlag`는 *Administer Jira* 전역 권한을 가진 Connect/Forge 앱에서만 의미가 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Yes | 이슈의 ID 또는 키 | `10010` |
| `id` | string | Yes | 코멘트 ID | `10000` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `notifyUsers` | boolean | No | - | 코멘트 수정 시 사용자에게 알림 발송 여부 | `true` |
| `overrideEditableFlag` | boolean | No | - | 편집 불가 필드를 강제로 편집하도록 화면 보안을 무시 (Administer Jira 권한 필요) | `false` |
| `expand` | string | No | - | 추가 정보 포함. `renderedBody`(HTML 렌더링 본문) 지원 | `renderedBody` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `body` | any (ADF) | No | Atlassian Document Format | 수정할 코멘트 본문 | `{"type":"doc","version":1,"content":[...]}` |
| `visibility` | any | No | 자식 코멘트는 변경 불가(400) | 코멘트 가시성 제한 | `{"type":"role","value":"Administrators"}` |
| `properties` | array | No | - | 코멘트 속성 목록 | `[{"key":"a","value":"b"}]` |

```json
{
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          { "type": "text", "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit." }
        ]
      }
    ]
  },
  "visibility": {
    "identifier": "Administrators",
    "type": "role",
    "value": "Administrators"
  }
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `author` | object | 작성자 정보 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `body` | object | 수정된 코멘트 본문(ADF) | `{"type":"doc","version":1,...}` |
| `id` | string | 코멘트 ID | `10000` |
| `self` | string | 코멘트 URL | `https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000` |
| `updateAuthor` | object | 최종 수정자 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `updated` | string | 최종 수정 일시 | `2021-01-18T23:45:00.000+0000` |
| `visibility` | object | 가시성 제한 | `{"identifier":"Administrators","type":"role","value":"Administrators"}` |

```json
{
  "author": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          { "type": "text", "text": "Lorem ipsum dolor sit amet..." }
        ]
      }
    ]
  },
  "created": "2021-01-17T12:34:00.000+0000",
  "id": "10000",
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000",
  "updateAuthor": {
    "accountId": "5b10a2844c20165700ede21g",
    "active": false,
    "displayName": "Mia Krystof",
    "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
  },
  "updated": "2021-01-18T23:45:00.000+0000",
  "visibility": {
    "identifier": "Administrators",
    "type": "role",
    "value": "Administrators"
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 코멘트 수정 권한이 없거나 요청이 잘못됨 (예: 자식 코멘트의 visibility 변경 시도) | 권한 및 요청 본문 확인 |
| 401 | - | 인증 정보가 잘못되었거나 없음 | 토큰 재발급/재인증 |
| 404 | - | 이슈 또는 코멘트를 찾을 수 없거나 조회 권한 없음 | 이슈/코멘트 ID 및 권한 확인 |

## 주의 사항

- 자식 코멘트는 부모의 가시성을 상속하므로 개별적으로 `visibility`를 바꾸면 400 에러가 발생한다.
- `overrideEditableFlag`는 일반 사용자 계정이 아닌 Connect/Forge 앱 전용 옵션이다.

---

### [높음] 5. 코멘트 삭제 (DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id})

## 기본 정보

- **기능:** 이슈에 달린 코멘트를 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id}`
- **인증:** Bearer Token 필요 (익명 호출 시 405 에러)
- **권한:** 프로젝트의 *Browse projects* 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한. *Delete all comments* 권한(모든 코멘트 삭제) 또는 *Delete own comments* 권한(본인 작성 코멘트만 삭제).

## 설명

프로젝트 운영 지원 흐름에서 코멘트 CRUD의 마지막 조각으로, 잘못 등록된 코멘트나 자동화가 남긴 임시 코멘트를 정리할 때 사용한다. 반드시 인증된 사용자로 호출해야 하며 익명 호출은 허용되지 않는다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Yes | 이슈의 ID 또는 키 | `10010` |
| `id` | string | Yes | 코멘트 ID | `10000` |

## Response

### `204 No Content`

삭제 성공 시 응답 본문 없음.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 코멘트 삭제 권한이 없음 | 사용자 권한(Delete all/own comments) 확인 |
| 401 | - | 인증 정보가 잘못되었거나 없음 | 토큰 재발급/재인증 |
| 404 | - | 이슈 또는 코멘트를 찾을 수 없거나 조회 권한 없음 | 이슈/코멘트 ID 및 권한 확인 |
| 405 | - | 익명 호출로 요청함 | 인증된 사용자로 재요청 |

## 주의 사항

- 익명 사용자는 이 API를 호출할 수 없다(405).
- 삭제는 되돌릴 수 없으므로 자동화에서 호출 시 대상 코멘트 ID를 명확히 확인해야 한다.

---

### [중간] 6. 코멘트 ID 목록으로 일괄 조회 (POST /rest/api/3/comment/list)

## 기본 정보

- **기능:** 여러 코멘트 ID를 한 번에 지정해 해당 코멘트들을 페이지 단위로 일괄 조회한다.
- **Endpoint:** `POST /rest/api/3/comment/list`
- **인증:** Bearer Token 필요 (익명 접근 가능)
- **권한:** 각 코멘트가 속한 프로젝트의 *Browse projects* 권한. 이슈 수준 보안이 설정된 경우 해당 이슈를 볼 수 있는 권한. 코멘트 가시성 제한이 있는 경우 해당 그룹/역할 소속 필요.

## 설명

여러 코멘트를 ID로 한 번에 조회해야 하는 배치성 작업(예: 여러 webhook 이벤트를 모아 한 번에 상세 조회)에 유용하지만, 팀 생성/알림/운영 지원의 핵심 흐름에서 필수적이지는 않다. 최대 1000개의 ID까지 한 번에 조회할 수 있다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `expand` | string | No | - | 추가 정보 포함. `renderedBody`(HTML 렌더링 본문), `properties`(코멘트 속성) 지원 | `renderedBody,properties` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ids` | integer[] | Yes | 최대 1000개 | 조회할 코멘트 ID 목록 | `[10000, 10001]` |

```json
{
  "ids": [10000, 10001]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isLast` | boolean | 마지막 페이지 여부 | `true` |
| `maxResults` | integer | 페이지당 최대 개수 | `1048576` |
| `startAt` | integer | 시작 오프셋 | `0` |
| `total` | integer | 전체 개수 | `1` |
| `values` | array | 코멘트 객체 배열 | - |
| `values[].author` | object | 작성자 정보 | `{"accountId":"5b10a2844c20165700ede21g","displayName":"Mia Krystof"}` |
| `values[].body` | object | 코멘트 본문(ADF) | `{"type":"doc","version":1,...}` |
| `values[].id` | string | 코멘트 ID | `10000` |
| `values[].visibility` | object | 가시성 제한 | `{"identifier":"Administrators","type":"role","value":"Administrators"}` |

```json
{
  "isLast": true,
  "maxResults": 1048576,
  "startAt": 0,
  "total": 1,
  "values": [
    {
      "author": {
        "accountId": "5b10a2844c20165700ede21g",
        "active": false,
        "displayName": "Mia Krystof",
        "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
      },
      "body": {
        "type": "doc",
        "version": 1,
        "content": [
          {
            "type": "paragraph",
            "content": [
              { "type": "text", "text": "Lorem ipsum dolor sit amet..." }
            ]
          }
        ]
      },
      "created": "2021-01-17T12:34:00.000+0000",
      "id": "10000",
      "self": "https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000",
      "updateAuthor": {
        "accountId": "5b10a2844c20165700ede21g",
        "active": false,
        "displayName": "Mia Krystof",
        "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
      },
      "updated": "2021-01-18T23:45:00.000+0000",
      "visibility": {
        "identifier": "Administrators",
        "type": "role",
        "value": "Administrators"
      }
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청에 1000개를 초과하는 ID가 포함되었거나 `ids`가 비어 있음 | ID 개수를 1000개 이하로 줄이거나 최소 1개 이상 지정 |

## 주의 사항

- `ids`는 최대 1000개까지만 허용되며, 빈 배열이면 400 에러가 발생한다.
- 여러 프로젝트에 걸친 코멘트 ID를 섞어서 조회할 수 있으나, 각 코멘트별로 권한 검사가 개별 적용된다.
