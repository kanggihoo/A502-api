# __84-tasks API 요약

이 리소스 그룹은 Jira의 장기 실행 비동기 작업(long-running asynchronous task)의 진행 상태를 조회하거나 취소하는 API를 제공한다. 대량 작업(bulk operation) 등이 비동기로 처리될 때 그 결과를 폴링하거나 중단시키는 용도로 쓰인다.

## 제외된 API

- 없음 (두 API 모두 "Administer Jira 글로벌 권한 또는 작업 생성자"이면 호출 가능하여, 프로젝트 관리자/작업 생성자 권한으로도 사용 가능하므로 제외하지 않음)

---

### [중간] 1. Get task (GET /rest/api/3/task/{taskId})

## 기본 정보

- **기능:** 장기 실행 비동기 작업의 진행 상태 및 결과 조회
- **Endpoint:** `GET /rest/api/3/task/{taskId}`
- **인증:** Bearer Token(OAuth 2.0) 또는 Basic 인증 필요
- **권한:** *Administer Jira* 글로벌 권한 또는 해당 작업(task)의 생성자

## 설명

비동기로 실행되는 장기 작업의 상태(진행률, 시작/종료 시각, 결과 등)를 조회한다. 작업이 완료되면 해당 작업을 생성한 오퍼레이션에 따라 정의된 JSON 결과가 `result` 필드에 담겨 반환된다. 작업 상세 정보는 영구 보관되지 않으며 (2019년 9월 기준) 약 14일간만 유지된다. 필요 OAuth 2.0 스코프는 2024년 6월 15일부로 `read:jira-work`로 변경될 예정이다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `taskId` | `string` | Yes | 작업(task)의 ID | `1` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `self` | `string` | 이 작업의 API 링크 | `https://your-domain.atlassian.net/rest/api/3/task/1` |
| `id` | `string` | 작업 ID | `1` |
| `description` | `string` | 작업 설명 | `Task description` |
| `status` | `string` | 작업 상태 | `COMPLETE` |
| `result` | `any` | 작업 완료 시 결과 (작업 종류에 따라 임의의 JSON) | `the task result, this may be any JSON` |
| `submittedBy` | `integer` | 작업을 제출한 사용자 ID | `10000` |
| `progress` | `integer` | 진행률(%) | `100` |
| `elapsedRuntime` | `integer` | 경과 실행 시간(ms) | `156` |
| `submitted` | `integer` | 제출 시각(epoch ms) | `1501708132800` |
| `started` | `integer` | 시작 시각(epoch ms) | `1501708132900` |
| `finished` | `integer` | 종료 시각(epoch ms) | `1501708133000` |
| `lastUpdate` | `integer` | 마지막 업데이트 시각(epoch ms) | `1501708133000` |

```json
{
  "self": "https://your-domain.atlassian.net/rest/api/3/task/1",
  "id": "1",
  "description": "Task description",
  "status": "COMPLETE",
  "result": "the task result, this may be any JSON",
  "submittedBy": 10000,
  "progress": 100,
  "elapsedRuntime": 156,
  "submitted": 1501708132800,
  "started": 1501708132900,
  "finished": 1501708133000,
  "lastUpdate": 1501708133000
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 401 | - | 인증 정보가 올바르지 않거나 누락됨 | 인증 토큰 확인 후 재요청 |
| 403 | - | 조회 권한 없음 (Administer Jira 권한도 없고 작업 생성자도 아님) | 작업 생성자 계정으로 조회하거나 관리자 권한 필요 |
| 404 | - | 해당 taskId의 작업을 찾을 수 없음 (14일 경과로 만료되었을 수 있음) | taskId 확인, 만료 여부 확인 |

## 주의 사항

- 작업 상세 정보는 영구 보관되지 않으며 약 14일 후 삭제될 수 있다.
- 필요 OAuth 2.0 스코프가 2024-06-15부로 `read:jira-work`로 변경 예정이었음(문서 작성 시점 기준 공지).

---

### [중간] 2. Cancel task (POST /rest/api/3/task/{taskId}/cancel)

## 기본 정보

- **기능:** 장기 실행 비동기 작업 취소
- **Endpoint:** `POST /rest/api/3/task/{taskId}/cancel`
- **인증:** Bearer Token(OAuth 2.0) 또는 Basic 인증 필요
- **권한:** *Administer Jira* 글로벌 권한 또는 해당 작업(task)의 생성자

## 설명

지정한 taskId의 비동기 작업을 취소한다. 이미 완료되었거나 취소 불가능한 상태의 작업에 대해서는 400 에러가 반환된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `taskId` | `string` | Yes | 작업(task)의 ID | `1` |

## Response

### `202 Accepted`

취소 요청이 접수되었음을 나타내며, 응답 스키마는 `any`(내용 없음/비정형)이다.

```json
{}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 작업 취소가 불가능한 상태 (예: 이미 완료됨) | 작업 상태를 먼저 조회 후 취소 가능 여부 확인 |
| 401 | - | 인증 정보가 올바르지 않거나 누락됨 | 인증 토큰 확인 후 재요청 |
| 403 | - | 취소 권한 없음 (Administer Jira 권한도 없고 작업 생성자도 아님) | 작업 생성자 계정으로 취소하거나 관리자 권한 필요 |
| 404 | - | 해당 taskId의 작업을 찾을 수 없음 | taskId 확인 |

## 주의 사항

- 400/401/403/404 응답 바디는 모두 문자열 배열(`string[]`) 형태의 에러 메시지 스키마이다.
