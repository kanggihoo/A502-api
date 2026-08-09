# __17-issue-bulk-operations API 요약

이 리소스 그룹은 여러 이슈를 한 번에 삭제/편집/이동/상태전환/watch-unwatch 하는 Jira 이슈 벌크(bulk) 작업 API와, 벌크 작업의 편집 가능 필드·가능한 전환·진행 상태를 조회하는 보조 API로 구성된다. 모든 벌크 작업은 비동기로 처리되며 `taskId`를 반환하고, 이 `taskId`로 진행 상태를 조회할 수 있다.

## 제외된 API

- 없음 (모든 엔드포인트가 "Global bulk change permission" 등 프로젝트/사이트 권한 스킴 상의 permission을 요구할 뿐, 문서에 "Jira administrators only" 또는 사이트 전체 시스템 관리자 전용이라는 명시적 제약이 없어 제외하지 않았다.)

---

### [높음] 1. Bulk delete issues (POST /rest/api/3/bulk/issues/delete)

## 기본 정보

- **기능:** 여러 이슈를 한 번의 요청으로 일괄 삭제
- **Endpoint:** `POST /rest/api/3/bulk/issues/delete`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission, 대상 이슈가 속한 모든 프로젝트에서 Delete issues permission 및 Browse project permission, (이슈 레벨 보안이 설정된 경우) 해당 이슈를 볼 수 있는 권한

## 설명

지정한 이슈 ID/키 목록을 한 번의 요청으로 최대 1,000개까지 삭제할 수 있다. 이슈들은 서로 다른 프로젝트/이슈 타입에서 섞여 있어도 된다. 요청은 즉시 처리되지 않고 비동기 작업으로 등록되며, 응답으로 받은 `taskId`를 09번 API(진행 상태 조회)로 추적해야 한다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `selectedIssueIdsOrKeys` | `string[]` | 예 | - | 벌크 삭제할 이슈 ID/키 목록. 서로 다른 프로젝트/이슈 타입 혼용 가능 | `["ISSUE-1","ISSUE-2"]` |
| `sendBulkNotification` | `boolean` | 아니오 | - | `true`면 삭제 시 대상 사용자에게 벌크 알림 이메일 발송 | `false` |

```json
{
  "selectedIssueIdsOrKeys": ["ISSUE-1", "ISSUE-2"],
  "sendBulkNotification": false
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `taskId` | `string` | 생성된 비동기 벌크 작업의 ID. 진행 상태 조회에 사용 | `"10641"` |

```json
{"taskId":"10641"}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음(예: 잘못된 이슈 ID/키 포함) | 이슈 ID/키 목록 검증 후 재요청 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | 사용자 권한(삭제/브라우즈/벌크 change) 확인 |

```json
{"errors":[{"message":"Some of the issues in the issueIdsOrKeys are not valid"}]}
```

## 주의 사항

- 한 번에 최대 1,000개 이슈까지 삭제 가능하다.
- 삭제는 되돌릴 수 없으므로 팀 운영 자동화에 사용할 경우 확인 절차를 둘 것을 권장한다.

---

### [높음] 2. Bulk edit issues (POST /rest/api/3/bulk/issues/fields)

## 기본 정보

- **기능:** 여러 이슈의 필드를 한 번의 요청으로 동시에 일괄 수정
- **Endpoint:** `POST /rest/api/3/bulk/issues/fields`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission, 대상 프로젝트 전체에 대한 Browse project / Edit issues permission, (이슈 레벨 보안 설정 시) 해당 권한

## 설명

최대 1,000개 이슈(서브태스크 포함), 200개 필드까지 한 번에 편집할 수 있는 비동기 API다. 편집할 필드 ID 목록(`selectedActions`)과 실제 값(`editedFieldsInput`)을 함께 전달해야 하며, 필드 ID는 `__02-get-bulk-editable-fields-get.md`(Get bulk editable fields) API로 먼저 조회하는 것이 권장된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `editedFieldsInput` | `any` | 예 | 필드 타입에 따라 구조가 다름 | 수정할 필드 값들을 정의하는 객체. `selectedActions`의 필드 ID와 일치해야 함 | - |
| `selectedActions` | `string[]` | 예 | - | 벌크 편집할 필드 ID 목록. Get bulk editable fields API로 조회 가능 | `["assignee","priority"]` |
| `selectedIssueIdsOrKeys` | `string[]` | 예 | 최대 1000개(서브태스크 포함) | 벌크 편집할 이슈 ID/키 목록 | `["ISSUE-1","ISSUE-2"]` |
| `sendBulkNotification` | `boolean` | 아니오 | - | `true`면 편집 시 벌크 알림 이메일 발송 | `false` |

```json
{
  "editedFieldsInput": {},
  "selectedActions": ["assignee", "priority"],
  "selectedIssueIdsOrKeys": ["ISSUE-1", "ISSUE-2"],
  "sendBulkNotification": false
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `taskId` | `string` | 생성된 비동기 벌크 작업의 ID | `"10641"` |

```json
{"taskId":"10641"}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음(예: `editedFieldsInput`에 있는 필드가 `selectedActions`에 없음) | `selectedActions`와 `editedFieldsInput`의 필드 ID 일치 여부 확인 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |

```json
{"errors":[{"message":"The following editedFieldInput values are not listed as selectedActions : issuetype"}]}
```

## 주의 사항

- 최대 1,000개 이슈(서브태스크 포함) 및 200개 필드 제한이 있다.
- `selectedActions`에 없는 필드를 `editedFieldsInput`에 넣으면 400 오류가 발생한다.

---

### [높음] 3. Bulk move issues (POST /rest/api/3/bulk/issues/move)

## 기본 정보

- **기능:** 여러 프로젝트의 이슈를 하나의 대상 프로젝트/이슈타입/부모로 일괄 이동
- **Endpoint:** `POST /rest/api/3/bulk/issues/move`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission, 원본 프로젝트에서 Move issues permission, 대상 프로젝트에서 Create issues permission, (서브태스크만 이동 시) 대상 프로젝트 Browse permission, (이슈 레벨 보안 설정 시) 해당 권한

## 설명

여러 프로젝트의 이슈를 단일 대상 프로젝트·이슈타입·부모로 이동하는 비동기 API로, 한 번에 최대 1,000개 이슈(서브태스크 포함)를 이동할 수 있다. Bulk Move UI와 완전히 동일한 기능 범위는 아니며(초기 버전), 에픽과 그 하위 이슈를 함께 이동하려면 별도의 다중 요청이 필요하다. 전체 이슈에 걸친 필드 총합이 1,500,000개를 넘을 수 없다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `sendBulkNotification` | `boolean` | 아니오 | - | `true`면 이동 시 벌크 알림 이메일 발송 | `false` |
| `targetToSourcesMapping` | `object` | 아니오(구조상 사실상 필요) | 키는 `<프로젝트 ID/키>,<이슈타입 ID>,<부모 ID/키>` 형식 | 이동 대상 프로젝트/이슈타입/부모 및 관련 필드·상태 매핑 정보 | `{"10001,10002,": {}}` |

```json
{
  "sendBulkNotification": false,
  "targetToSourcesMapping": {}
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `taskId` | `string` | 생성된 비동기 벌크 작업의 ID | `"10641"` |

```json
{"taskId":"10641"}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음(예: 잘못된 이슈 ID/키 포함) | 이슈 ID/키, 매핑 값 검증 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |

```json
{"errors":[{"message":"Some of the issues in the issueIdsOrKeys are not valid"}]}
```

## 주의 사항

- 최대 1,000개 이슈(서브태스크 포함), 전체 필드 합계 1,500,000개 제한이 있다.
- 에픽과 하위 이슈의 관계를 유지하며 이동하려면 에픽 이동 후 자식 이슈를 별도 요청으로 이동해야 한다.
- 동일한 매핑 키가 중복되면 하나만 처리되고 에러 없이 무시될 수 있어 주의가 필요하다.

---

### [높음] 4. Bulk transition issue statuses (POST /rest/api/3/bulk/issues/transition)

## 기본 정보

- **기능:** 여러 이슈의 상태(워크플로우 전환)를 한 번에 일괄 변경
- **Endpoint:** `POST /rest/api/3/bulk/issues/transition`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission, 대상 프로젝트 전체에서 Transition issues permission 및 Browse project permission, (이슈 레벨 보안 설정 시) 해당 권한

## 설명

여러 이슈를 각각에 해당하는 전환 ID(`transitionId`)와 함께 최대 1,000개까지 한 번에 전환시키는 비동기 API다. 전환 ID는 05번 API(Get available transitions)로 미리 조회해서 사용하는 것이 일반적이다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `bulkTransitionInputs` | `object[]` | 예 | - | 이슈 목록과 전환 ID의 쌍 목록 | 아래 예시 참고 |
| `bulkTransitionInputs[].selectedIssueIdsOrKeys` | `string[]` | 예 | - | 벌크 전환할 이슈 ID/키 목록 | `["ISSUE-1","ISSUE-2"]` |
| `bulkTransitionInputs[].transitionId` | `string` | 예 | - | 이슈에 적용할 전환 ID | `"21"` |
| `sendBulkNotification` | `boolean` | 아니오 | - | `true`면 전환 시 벌크 알림 이메일 발송 | `false` |

```json
{
  "bulkTransitionInputs": [
    {
      "selectedIssueIdsOrKeys": ["ISSUE-1", "ISSUE-2"],
      "transitionId": "21"
    }
  ],
  "sendBulkNotification": false
}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `taskId` | `string` | 생성된 비동기 벌크 작업의 ID | `"10641"` |

```json
{"taskId":"10641"}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음(예: 잘못된 이슈 ID/키 포함) | 이슈 ID/키, 전환 ID 검증 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | Transition issues permission 등 확인 |

```json
{"errors":[{"message":"Some of the issues in the issueIdsOrKeys are not valid"}]}
```

## 주의 사항

- 한 번에 최대 1,000개 이슈까지 전환 가능하다.
- 워크플로우별로 전환 ID가 다를 수 있으므로 05번 API로 사전 조회한 값을 사용해야 한다.

---

### [높음] 5. Get bulk issue operation progress (GET /rest/api/3/bulk/queue/{taskId})

## 기본 정보

- **기능:** 벌크 작업(삭제/편집/이동/전환/watch/unwatch)의 진행 상태 및 결과 조회
- **Endpoint:** `GET /rest/api/3/bulk/queue/{taskId}`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission

## 설명

다른 벌크 작업 API 호출 시 반환받은 `taskId`로 해당 작업의 진행률과 완료 여부, 처리 결과를 조회한다. 작업 생성일로부터 최대 14일간 진행 상태를 조회할 수 있다. 통합 대시보드에서 벌크 작업의 완료 여부를 폴링하거나 알림을 보낼 때 핵심적으로 사용된다.

## Request

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `taskId` | `string` | 예 | 조회할 작업의 ID | `10000` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `taskId` | `string` | 작업 ID | `"10000"` |
| `status` | `string` | 작업 상태(`RUNNING`, `COMPLETE` 등) | `"COMPLETE"` |
| `progressPercent` | `number` | 진행률(%) | `100` |
| `submittedBy.accountId` | `string` | 작업을 요청한 사용자 accountId | `"5b10a2844c20165700ede21g"` |
| `created` | `number` | 작업 생성 시각(epoch ms) | `1704110400000` |
| `started` | `number` | 작업 시작 시각(epoch ms) | `1704110460000` |
| `updated` | `number` | 최종 갱신 시각(epoch ms) | `1704110520000` |
| `processedAccessibleIssues` | `number[]` | 처리된 접근 가능 이슈 ID 목록(완료 시) | `[10001,10002]` |
| `invalidOrInaccessibleIssueCount` | `number` | 유효하지 않거나 접근 불가능한 이슈 수(완료 시) | `0` |
| `totalIssueCount` | `number` | 전체 대상 이슈 수(완료 시) | `2` |

```json
{
  "created": 1704110400000,
  "invalidOrInaccessibleIssueCount": 0,
  "processedAccessibleIssues": [10001, 10002],
  "progressPercent": 100,
  "started": 1704110460000,
  "status": "COMPLETE",
  "submittedBy": {"accountId": "5b10a2844c20165700ede21g"},
  "taskId": "10000",
  "totalIssueCount": 2,
  "updated": 1704110520000
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음(예: 해당 taskId가 벌크 작업 태스크가 아님) | taskId 값 확인 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |

```json
{"errorMessages":["The task associated with this taskId is not a bulk operation task"],"errors":{},"httpStatusCode":{"empty":false,"present":true}}
```

## 주의 사항

- 작업 생성 후 최대 14일까지만 진행 상태 조회가 가능하다.
- `RUNNING` 상태와 `COMPLETE` 상태에서 응답 필드 구성이 다르다.

---

### [중간] 6. Get bulk editable fields (GET /rest/api/3/bulk/issues/fields)

## 기본 정보

- **기능:** 선택한 이슈들에 대해 벌크 편집이 가능한 필드 목록 조회
- **Endpoint:** `GET /rest/api/3/bulk/issues/fields`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission, 대상 프로젝트 전체에서 Browse project permission, (이슈 레벨 보안 설정 시) 해당 권한, 필드별 편집 권한

## 설명

하나 이상의 이슈에 대해 사용자가 실제로 벌크 편집할 수 있는 필드 목록을 조회하는 API로, `_03-bulk-edit-issues-post.md`(Bulk edit issues) 호출 전에 유효한 필드 ID를 확인하는 용도로 사용한다. 응답은 페이지네이션되며 한 번에 50개 필드씩 반환된다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `issueIdsOrKeys` | `string` | 예 | - | 편집 가능 필드를 조회할 이슈 ID/키 | `ISSUE-1` |
| `searchText` | `string` | 아니오 | - | 편집 가능 필드 중 검색할 텍스트 | `assignee` |
| `endingBefore` | `string` | 아니오 | - | 페이지네이션 종료 커서 | - |
| `startingAfter` | `string` | 아니오 | - | 페이지네이션 시작 커서 | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `fields[].id` | `string` | 필드 ID | `"assignee"` |
| `fields[].name` | `string` | 필드 이름 | `"Assignee"` |
| `fields[].isRequired` | `boolean` | 필수 필드 여부 | `false` |
| `fields[].type` | `string` | 필드 타입 | `"assignee"` |
| `fields[].searchUrl` | `string` | 값 검색용 URL(해당하는 경우) | `"https://your-domain.atlassian.net/rest/api/3/user/assignable/multiProjectSearch?projectKeys=KAN&query="` |
| `fields[].multiSelectFieldOptions` | `string[]` | 다중 선택 필드의 조작 옵션 | `["ADD","REMOVE","REPLACE","REMOVE_ALL"]` |

```json
{
  "fields": [
    {"id": "assignee", "isRequired": false, "name": "Assignee", "searchUrl": "https://your-domain.atlassian.net/rest/api/3/user/assignable/multiProjectSearch?projectKeys=KAN&query=", "type": "assignee"},
    {"id": "components", "isRequired": false, "multiSelectFieldOptions": ["ADD", "REMOVE", "REPLACE", "REMOVE_ALL"], "name": "Components", "type": "components", "unavailableMessage": "{0}NOTE{1}: The project of the selected issue(s) does not have any components."}
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음 | 파라미터 확인 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | 권한 확인 |
| 404 | - | 제공된 이슈 ID에 대해 편집 가능한 필드가 없음 | 이슈 ID/키 확인 |

```json
{"errors":[{"message":"string"}]}
```

## 주의 사항

- 응답은 페이지네이션되며 한 번에 50개 필드씩 반환된다.

---

### [중간] 7. Get available transitions (GET /rest/api/3/bulk/issues/transition)

## 기본 정보

- **기능:** 여러 이슈에 대해 벌크 전환 시 사용 가능한 워크플로우 전환 목록 조회
- **Endpoint:** `GET /rest/api/3/bulk/issues/transition`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission, 대상 프로젝트 전체에서 Transition issues permission 및 Browse project permission, (이슈 레벨 보안 설정 시) 해당 권한

## 설명

지정한 이슈들의 워크플로우별로 공통으로 사용 가능한 전환 목록을 조회한다. 추가 필드 업데이트가 필요 없는 전환만 포함되며, 필드 업데이트가 필요한 벌크 전환은 Jira Cloud UI를 사용해야 한다. `_06-bulk-transition-issue-statuses-post.md`(Bulk transition issue statuses) 호출 전 유효한 `transitionId`를 확인하는 데 사용한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `issueIdsOrKeys` | `string` | 예 | - | 콤마(,)로 구분된 전환 대상 이슈 ID/키 | `EPIC-1,TASK-1` |
| `endingBefore` | `string` | 아니오 | - | 페이지네이션 종료 커서 | - |
| `startingAfter` | `string` | 아니오 | - | 페이지네이션 시작 커서 | - |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `availableTransitions[].isTransitionsFiltered` | `boolean` | 일부 전환이 필터링되어 제외되었는지 여부 | `false` |
| `availableTransitions[].issues` | `string[]` | 해당 워크플로우를 공유하는 이슈 목록 | `["EPIC-1","TASK-1"]` |
| `availableTransitions[].transitions[].transitionId` | `number` | 전환 ID | `11` |
| `availableTransitions[].transitions[].transitionName` | `string` | 전환 이름 | `"To Do"` |
| `availableTransitions[].transitions[].to.statusId` | `number` | 전환 후 상태 ID | `10001` |
| `availableTransitions[].transitions[].to.statusName` | `string` | 전환 후 상태 이름 | `"To Do"` |

```json
{
  "availableTransitions": [
    {
      "isTransitionsFiltered": false,
      "issues": ["EPIC-1", "TASK-1"],
      "transitions": [
        {"to": {"statusId": 10001, "statusName": "To Do"}, "transitionId": 11, "transitionName": "To Do"},
        {"to": {"statusId": 10002, "statusName": "In Progress"}, "transitionId": 21, "transitionName": "In Progress"},
        {"to": {"statusId": 10003, "statusName": "Done"}, "transitionId": 31, "transitionName": "Done"}
      ]
    }
  ]
}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음(예: 잘못된 이슈 ID/키) | 이슈 ID/키 확인 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | 권한 확인 |

```json
{"errors":[{"message":"Some of the issues in the issueIdsOrKeys are not valid"}]}
```

## 주의 사항

- 추가 필드 업데이트가 필요한 전환은 결과에서 제외된다(`isTransitionsFiltered: true`로 표시).
- 응답은 페이지네이션되며 한 번에 50개 워크플로우씩 반환된다.

---

### [중간] 8. Bulk watch issues (POST /rest/api/3/bulk/issues/watch)

## 기본 정보

- **기능:** 여러 이슈를 한 번의 요청으로 일괄 watch(구독) 처리
- **Endpoint:** `POST /rest/api/3/bulk/issues/watch`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission, 대상 프로젝트 전체에서 Browse project permission, (이슈 레벨 보안 설정 시) 해당 권한

## 설명

지정한 이슈 목록을 최대 1,000개까지 한 번의 요청으로 watch 상태로 만드는 비동기 API다. 통합 알림 기능에서 특정 사용자를 다수 이슈의 watcher로 일괄 등록할 때 사용할 수 있다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `selectedIssueIdsOrKeys` | `string[]` | 예 | 최대 1000개 | 벌크 watch할 이슈 ID/키 목록 | `["ISSUE-1","ISSUE-2"]` |

```json
{"selectedIssueIdsOrKeys": ["ISSUE-1", "ISSUE-2"]}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `taskId` | `string` | 생성된 비동기 벌크 작업의 ID | `"10641"` |

```json
{"taskId":"10641"}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음(예: 잘못된 이슈 ID/키 포함) | 이슈 ID/키 검증 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | 권한 확인 |

```json
{"errors":[{"message":"Some of the issues in the issueIdsOrKeys are not valid"}]}
```

## 주의 사항

- 한 번에 최대 1,000개 이슈까지 watch 처리 가능하다.

---

### [중간] 9. Bulk unwatch issues (POST /rest/api/3/bulk/issues/unwatch)

## 기본 정보

- **기능:** 여러 이슈를 한 번의 요청으로 일괄 unwatch(구독 해제) 처리
- **Endpoint:** `POST /rest/api/3/bulk/issues/unwatch`
- **인증:** Bearer Token(또는 Basic auth) 필요
- **권한:** Global bulk change permission, 대상 프로젝트 전체에서 Browse project permission, (이슈 레벨 보안 설정 시) 해당 권한

## 설명

지정한 이슈 목록을 최대 1,000개까지 한 번의 요청으로 unwatch 상태로 만드는 비동기 API다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `selectedIssueIdsOrKeys` | `string[]` | 예 | 최대 1000개 | 벌크 unwatch할 이슈 ID/키 목록 | `["ISSUE-1","ISSUE-2"]` |

```json
{"selectedIssueIdsOrKeys": ["ISSUE-1", "ISSUE-2"]}
```

## Response

### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `taskId` | `string` | 생성된 비동기 벌크 작업의 ID | `"10641"` |

```json
{"taskId":"10641"}
```

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| 400 | - | 요청이 유효하지 않음(예: 잘못된 이슈 ID/키 포함) | 이슈 ID/키 검증 |
| 401 | - | 인증 자격 증명이 잘못되었거나 없음 | 인증 토큰 확인 |
| 403 | - | 필요한 권한이 없음 | 권한 확인 |

```json
{"errors":[{"message":"Some of the issues in the issueIdsOrKeys are not valid"}]}
```

## 주의 사항

- 한 번에 최대 1,000개 이슈까지 unwatch 처리 가능하다.
