# 1. List playbook conditions

## 기본 정보
- **기능**: 특정 playbook의 condition 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/playbooks/{id}/conditions`
- **인증**: Bearer Token 필요
- **권한**: 문서에 명시 없음 (해당 playbook 접근 권한 기준으로 추정, 일반 사용자는 자신이 접근 가능한 playbook에 대해 사용 가능)

## 설명
지정한 playbook에 정의된 condition들을 페이지네이션으로 조회하는 API이다. Playbooks 플러그인 endpoint(`/plugins/playbooks/api/v0`)이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | condition을 조회할 playbook ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 요청할 페이지의 0 기반 인덱스 |
| per_page | integer | No | - | 페이지당 반환할 condition 수 |

## Response

### 200 - A paged list of playbook conditions.
| 필드 | 타입 | 설명 |
|---|---|---|
| total_count | integer | 페이징과 무관한 전체 condition 수 |
| page_count | integer | 전체 페이지 수 |
| has_more | boolean | 현재 페이지 이후에 더 있는지 여부 |
| items | array | 이 페이지의 condition 목록 |
| items[].id | string | condition의 고유 식별자 (26자 영숫자) |
| items[].condition_expr | object | 조건식 (`and`/`or`/`is`/`isNot` 조합, 재귀 구조) |
| items[].version | integer | 조건식 포맷 버전 (현재 1만 지원) |
| items[].playbook_id | string | 이 condition이 속한 playbook ID |
| items[].run_id | string | run condition(읽기 전용 스냅샷)인 경우 run ID, playbook condition이면 빈 값 |
| items[].create_at | integer | 생성 시각 (밀리초) |
| items[].update_at | integer | 수정 시각 (밀리초) |

```json
{
  "total_count": 0,
  "page_count": 0,
  "has_more": false,
  "items": [
    {
      "id": "string",
      "condition_expr": {
        "is": { "field_id": "string", "value": "any" }
      },
      "version": 1,
      "playbook_id": "string",
      "run_id": "",
      "create_at": 0,
      "update_at": 0
    }
  ]
}
```

---

# 2. Create a playbook condition

## 기본 정보
- **기능**: playbook에 새 condition을 생성한다.
- **Endpoint**: `POST /plugins/playbooks/api/v0/playbooks/{id}/conditions`
- **인증**: Bearer Token 필요
- **권한**: 문서에 명시 없음 (해당 playbook 편집 권한 기준으로 추정 — 일반 사용자도 `playbook_public_create`/`playbook_private_create`로 자신의 playbook 관리 가능)

## 설명
지정한 playbook에 새 condition을 생성하는 API이다. 조건식은 `and`/`or`/`is`/`isNot`을 재귀적으로 조합한 구조이며, 현재 version 1 포맷만 지원된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | condition을 생성할 playbook ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| condition_expr | object | Yes | 조건식. `and`(array)/`or`(array)/`is`/`isNot` 조합 |
| condition_expr.is | object | No | 일치 조건. `field_id`(string, 필수)와 `value`(any, 필수) |
| condition_expr.isNot | object | No | 불일치 조건. `field_id`(string, 필수)와 `value`(any, 필수) |
| version | integer | Yes | 조건식 포맷 버전 (현재 1만 지원) |
| id | string | No | condition 식별자 |
| playbook_id | string | No | condition이 속할 playbook ID |
| run_id | string | No | run condition인 경우 run ID. playbook condition은 빈 값 |

```json
{
  "condition_expr": {
    "is": { "field_id": "string", "value": "any" }
  },
  "version": 1,
  "playbook_id": "string"
}
```

## Response

### 201 - Created condition.
(요청과 동일한 구조의 condition 객체에 `create_at`/`update_at` 포함)

```json
{
  "id": "string",
  "condition_expr": {
    "is": { "field_id": "string", "value": "any" }
  },
  "version": 1,
  "playbook_id": "string",
  "run_id": "",
  "create_at": 0,
  "update_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 500 | 서버 내부 오류 |

---

# 3. Update a playbook condition

## 기본 정보
- **기능**: playbook의 기존 condition을 수정한다.
- **Endpoint**: `PUT /plugins/playbooks/api/v0/playbooks/{id}/conditions/{conditionID}`
- **인증**: Bearer Token 필요
- **권한**: 문서에 명시 없음 (해당 playbook 편집 권한 기준으로 추정)

## 설명
지정한 playbook의 기존 condition을 수정하는 API이다. Body 구조는 생성 API와 동일하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | playbook ID |
| conditionID | string | Yes | 수정할 condition ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| condition_expr | object | Yes | 조건식. `and`/`or`/`is`/`isNot` 조합 |
| version | integer | Yes | 조건식 포맷 버전 (현재 1만 지원) |
| id | string | No | condition 식별자 |
| playbook_id | string | No | condition이 속한 playbook ID |
| run_id | string | No | run condition인 경우 run ID |

```json
{
  "condition_expr": {
    "isNot": { "field_id": "string", "value": "any" }
  },
  "version": 1
}
```

## Response

### 200 - Updated condition.
(condition 객체 반환, 구조는 생성 응답과 동일)

```json
{
  "id": "string",
  "condition_expr": {
    "isNot": { "field_id": "string", "value": "any" }
  },
  "version": 1,
  "playbook_id": "string",
  "run_id": "",
  "create_at": 0,
  "update_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 404 | 찾을 수 없음 |
| 500 | 서버 내부 오류 |

---

# 4. Delete a playbook condition

## 기본 정보
- **기능**: playbook에서 condition을 삭제한다.
- **Endpoint**: `DELETE /plugins/playbooks/api/v0/playbooks/{id}/conditions/{conditionID}`
- **인증**: Bearer Token 필요
- **권한**: 문서에 명시 없음 (해당 playbook 편집 권한 기준으로 추정)

## 설명
playbook에서 condition을 삭제하는 API이다. run condition은 읽기 전용 스냅샷이므로 삭제할 수 없다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | playbook ID |
| conditionID | string | Yes | 삭제할 condition ID |

## Response

### 204 - Condition successfully deleted.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 403 | 권한 없음 |
| 404 | 찾을 수 없음 |
| 500 | 서버 내부 오류 |

## 주의 사항
run condition은 읽기 전용 스냅샷이라 삭제할 수 없다.

---

# 5. List run conditions

## 기본 정보
- **기능**: 특정 run의 condition 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /plugins/playbooks/api/v0/runs/{id}/conditions`
- **인증**: Bearer Token 필요
- **권한**: 문서에 명시 없음 (해당 run 접근 권한 기준으로 추정)

## 설명
지정한 run의 condition들을 페이지네이션으로 조회하는 API이다. run condition은 playbook에서 복사된 읽기 전용 스냅샷이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | condition을 조회할 run ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 요청할 페이지의 0 기반 인덱스 |
| per_page | integer | No | - | 페이지당 반환할 condition 수 |

## Response

### 200 - A paged list of run conditions.
(1번 endpoint와 동일한 페이지 구조. `items[].run_id`에 run ID가 채워짐)

```json
{
  "total_count": 0,
  "page_count": 0,
  "has_more": false,
  "items": [
    {
      "id": "string",
      "condition_expr": {
        "is": { "field_id": "string", "value": "any" }
      },
      "version": 1,
      "playbook_id": "string",
      "run_id": "string",
      "create_at": 0,
      "update_at": 0
    }
  ]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 권한 없음 |
| 404 | 찾을 수 없음 |
| 500 | 서버 내부 오류 |

---
