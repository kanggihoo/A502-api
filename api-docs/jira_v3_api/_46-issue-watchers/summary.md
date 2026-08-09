# _46-issue-watchers API 요약

이 리소스 그룹은 Jira 이슈를 "워칭(watching)"하는 사용자를 다루는 API 모음이다. 이슈의 워처 목록 조회, 워처 추가/삭제, 여러 이슈에 대한 현재 사용자의 워칭 여부 일괄 조회 기능을 제공한다.

이 그룹의 모든 API는 프로젝트 단위 권한(Browse projects, Manage watcher list, View voters and watchers)만 요구하며 Jira 사이트 전체 관리자 권한이 필요한 API는 없어, 제외된 항목은 없다.

---

### [높음] 1. Get issue watchers (GET /rest/api/3/issue/{issueIdOrKey}/watchers)

## 기본 정보

- **기능:** 특정 이슈의 워처(watcher) 목록과 워치 카운트, 현재 사용자의 워칭 여부를 조회한다.
- **Endpoint:** `GET /rest/api/3/issue/{issueIdOrKey}/watchers`
- **인증:** Bearer Token(또는 Basic Auth) 필요 — 단, 이 엔드포인트 자체는 익명 접근도 가능(This operation can be accessed anonymously)
- **권한:** *Browse projects* 프로젝트 권한 (이슈 레벨 보안 설정 시 해당 이슈에 대한 열람 권한 추가 필요). 자기 자신 외 다른 사용자의 워처 상세 정보를 보려면 *View voters and watchers* 프로젝트 권한 필요

## 설명

이슈에 대해 현재 워칭 중인 사용자 목록과 총 워치 수를 반환한다. Jira 관리 화면의 "Allow users to watch issues" 옵션이 켜져 있어야 동작한다. 통합 대시보드에서 이슈별 관심 인원(워처)을 표시하거나 알림 대상을 파악하는 데 사용할 수 있다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `EX-1` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `isWatching` | boolean | 현재 요청 사용자가 해당 이슈를 워칭 중인지 여부 | `false` |
| `self` | string | 이 리소스의 API 링크 | `https://your-domain.atlassian.net/rest/api/3/issue/EX-1/watchers` |
| `watchCount` | integer | 워처 총 수 | `1` |
| `watchers` | array | 워처 사용자 목록 (accountId, active, displayName, self 포함) | 아래 예시 참고 |

```json
{
  "isWatching": false,
  "self": "https://your-domain.atlassian.net/rest/api/3/issue/EX-1/watchers",
  "watchCount": 1,
  "watchers": [
    {
      "accountId": "5b10a2844c20165700ede21g",
      "active": false,
      "displayName": "Mia Krystof",
      "self": "https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g"
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 올바르지 않거나 없음 | 인증 토큰/자격 증명 확인 |
| 404 | - | 이슈를 찾을 수 없거나 열람 권한이 없음 | 이슈 ID/키 및 권한 확인 |

## 주의 사항

- "Allow users to watch issues" 옵션이 꺼져 있으면 호출이 실패할 수 있다.
- 자신 외 다른 사용자의 워처 상세를 보려면 *View voters and watchers* 권한이 별도로 필요하다.

---

### [높음] 2. Add watcher (POST /rest/api/3/issue/{issueIdOrKey}/watchers)

## 기본 정보

- **기능:** 이슈에 사용자를 워처로 추가한다.
- **Endpoint:** `POST /rest/api/3/issue/{issueIdOrKey}/watchers`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** *Browse projects* 프로젝트 권한 (이슈 레벨 보안 시 열람 권한 추가 필요). 자기 자신이 아닌 다른 사용자를 워처로 추가하려면 *Manage watcher list* 프로젝트 권한 필요

## 설명

계정 ID(accountId)를 전달하여 해당 사용자를 이슈의 워처로 등록한다. 사용자를 지정하지 않으면 호출한 사용자 자신이 워처로 추가된다. "Allow users to watch issues" 옵션이 켜져 있어야 동작한다. 팀 생성/온보딩 자동화 시 팀원을 관련 이슈의 워처로 자동 등록하는 데 활용 가능하다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `EX-1` |

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| (본문) | string | Y | 계정 ID 문자열 | 워처로 추가할 사용자의 accountId | `"5b10ac8d82e05b22cc7d4ef5"` |

```json
"5b10ac8d82e05b22cc7d4ef5"
```

## Response

### `204 No Content`

성공 시 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 요청 본문(accountId) 형식 확인 |
| 401 | - | 인증 정보가 올바르지 않거나 없음 | 인증 토큰/자격 증명 확인 |
| 403 | - | 워처 목록 관리 권한이 없음 | *Manage watcher list* 권한 확인 |
| 404 | - | 이슈나 사용자를 찾을 수 없거나 열람 권한이 없음 | 이슈 ID/키, 사용자 accountId, 권한 확인 |

## 주의 사항

- 사용자를 지정하지 않으면 호출자 자신이 워처로 추가된다.
- 다른 사용자를 추가하려면 *Manage watcher list* 프로젝트 권한이 필요하다(프로젝트 관리자 수준에서 부여 가능).

---

### [중간] 3. Get is watching issue bulk (POST /rest/api/3/issue/watching)

## 기본 정보

- **기능:** 여러 이슈 ID에 대해 현재 사용자가 워칭 중인지 여부를 일괄 조회한다.
- **Endpoint:** `POST /rest/api/3/issue/watching`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** *Browse projects* 프로젝트 권한 (이슈 레벨 보안 시 열람 권한 추가 필요)

## 설명

이슈 ID 목록을 받아 각 이슈에 대한 현재 사용자의 워칭 여부(true/false)를 한 번에 반환한다. 유효하지 않은 이슈 ID는 `false`로 처리된다. "Allow users to watch issues" 옵션이 켜져 있어야 동작한다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `issueIds` | array[string] | Y | - | 조회할 이슈 ID 목록 | `["10001", "10002", "10005"]` |

```json
{
  "issueIds": [
    "10001",
    "10002",
    "10005"
  ]
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `issuesIsWatching` | object | 이슈 ID를 키로, 워칭 여부(boolean)를 값으로 하는 맵 | `{"10001":true,"10002":false,"10005":true}` |

```json
{
  "issuesIsWatching": {
    "10001": true,
    "10002": false,
    "10005": true
  }
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 올바르지 않거나 없음 | 인증 토큰/자격 증명 확인 |

## 주의 사항

- 유효하지 않은 이슈 ID를 포함해도 오류 없이 `false`로 응답된다.
- 다건 조회이므로 대시보드에서 여러 이슈의 워칭 상태를 한 번에 표시할 때 유용하지만, 필수 핵심 흐름은 아니다.

---

### [중간] 4. Delete watcher (DELETE /rest/api/3/issue/{issueIdOrKey}/watchers)

## 기본 정보

- **기능:** 이슈에서 특정 사용자를 워처에서 제거한다.
- **Endpoint:** `DELETE /rest/api/3/issue/{issueIdOrKey}/watchers`
- **인증:** Bearer Token(또는 Basic Auth) 필요
- **권한:** *Browse projects* 프로젝트 권한 (이슈 레벨 보안 시 열람 권한 추가 필요). 자기 자신이 아닌 다른 사용자를 제거하려면 *Manage watcher list* 프로젝트 권한 필요

## 설명

계정 ID로 지정한 사용자를 이슈 워처 목록에서 제거한다. `username` 쿼리 파라미터는 더 이상 사용되지 않으며(deprecated), `accountId`가 필수적으로 요구된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `issueIdOrKey` | string | Y | 이슈의 ID 또는 키 | `EX-1` |

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `username` | string | N | - | 더 이상 사용되지 않는 파라미터(사용자 프라이버시 API 마이그레이션으로 폐기) | - |
| `accountId` | string | Y(사실상 필수) | - | 워처에서 제거할 사용자의 계정 ID | `5b10ac8d82e05b22cc7d4ef5` |

## Response

### `204 No Content`

성공 시 본문 없이 204를 반환한다.

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | `accountId`가 제공되지 않음 | 쿼리 파라미터에 accountId 포함 |
| 401 | - | 인증 정보가 올바르지 않거나 없음 | 인증 토큰/자격 증명 확인 |
| 403 | - | 워처 목록 관리 권한이 없음 | *Manage watcher list* 권한 확인 |
| 404 | - | 이슈나 사용자를 찾을 수 없거나 열람 권한이 없음 | 이슈 ID/키, 사용자 accountId, 권한 확인 |

## 주의 사항

- `username` 파라미터는 폐기(deprecated)되었으므로 반드시 `accountId`를 사용해야 한다.
- 자기 자신이 아닌 사용자를 제거하려면 *Manage watcher list* 프로젝트 권한이 필요하다.
