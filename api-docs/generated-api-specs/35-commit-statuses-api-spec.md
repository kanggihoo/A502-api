# GitLab REST API — 35. Commit Statuses

---

## 1. List all commit statuses (GET)

### 기본 정보
- **기능:** 특정 프로젝트의 커밋에 대한 모든 commit status(CI/CD 상태) 목록을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/statuses`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** yes

### 설명
지정한 프로젝트(`id`)와 커밋(`sha`)에 연결된 commit status 목록을 반환합니다. 브랜치(ref), stage, job name, pipeline ID 등으로 필터링할 수 있으며, 최신 상태만 보거나 전체 이력을 조회할 수 있습니다. 페이지네이션과 정렬을 지원합니다.

### Request

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `id` | `any` | Yes | 프로젝트의 ID 또는 URL-encoded 경로 |
| `sha` | `string` | Yes | 커밋의 SHA 해시 |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|------|------|------|--------|------|
| `ref` | `string` | No | default branch | 브랜치 또는 태그 이름 |
| `stage` | `string` | No | - | 빌드 스테이지로 필터링 |
| `name` | `string` | No | - | Job 이름으로 필터링 |
| `pipeline_id` | `integer` | No | - | Pipeline ID로 필터링 |
| `all` | `boolean` | No | `false` | `true`면 최신 상태뿐 아니라 전체 이력 포함 |
| `order_by` | `string` | No | `id` | 정렬 기준 (`id`, `pipeline_id`) |
| `sort` | `string` | No | `asc` | 정렬 방향 (`asc`, `desc`) |
| `page` | `integer` | No | `1` | 현재 페이지 번호 |
| `per_page` | `integer` | No | `20` | 페이지당 항목 수 |

### Response

#### `200 OK`
```json
{
  "id": "integer",
  "sha": "string",
  "ref": "string",
  "status": "string",
  "name": "string",
  "target_url": "string",
  "description": "string",
  "created_at": "string (datetime)",
  "started_at": "string (datetime)",
  "finished_at": "string (datetime)",
  "allow_failure": "boolean",
  "coverage": "number",
  "pipeline_id": "integer",
  "author": {
    "id": "integer",
    "username": "string",
    "public_email": "string",
    "name": "string",
    "state": "string",
    "locked": "boolean",
    "avatar_url": "string",
    "avatar_path": "string",
    "custom_attributes": [{ "key": "string", "value": "string" }],
    "web_url": "string"
  }
}
```

| 필드 | 타입 | 설명 |
|------|------|------|
| `id` | integer | Commit status의 고유 ID |
| `sha` | string | 대상 커밋의 SHA |
| `ref` | string | 브랜치 또는 태그 참조 |
| `status` | string | 상태 (`pending`, `running`, `success`, `failed`, `canceled`, `skipped`) |
| `name` | string | Job 이름 |
| `target_url` | string | 상태와 연결된 외부 URL |
| `description` | string | 상태에 대한 짧은 설명 |
| `created_at` | string | 생성 시각 (ISO 8601) |
| `started_at` | string | 시작 시각 |
| `finished_at` | string | 완료 시각 |
| `allow_failure` | boolean | 실패 허용 여부 |
| `coverage` | number | 코드 커버리지 비율 |
| `pipeline_id` | integer | 연결된 Pipeline ID |
| `author` | object | 상태를 생성한 사용자 정보 |

### Errors
| 상태 코드 | 설명 |
|-----------|------|
| `400 Bad Request` | 요청 파라미터가 잘못됨 |
| `401 Unauthorized` | 유효하지 않거나 누락된 인증 토큰 |
| `403 Forbidden` | 리소스에 대한 접근 권한 없음 |
| `404 Not Found` | 프로젝트 또는 커밋을 찾을 수 없음 |

---

## 2. Create or update a commit pipeline status (POST)

### 기본 정보
- **기능:** 외부(External) CI/CD 파이프라인에서 커밋의 상태를 생성하거나 업데이트합니다.
- **Endpoint:** `POST /api/v4/projects/{id}/statuses/{sha}`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** no (동일 SHA + name으로 여러 번 호출 시 덮어씀)

### 설명
지정한 프로젝트(`id`)의 커밋(`sha`)에 대해 외부 CI/CD 잡의 상태를 생성하거나 업데이트합니다. 이 엔드포인트는 GitLab CI/CD가 아닌 외부 시스템(예: Jenkins, CircleCI)에서 상태를 보고할 때 사용합니다. 커밋이 Merge Request과 연결된 경우 소스 브랜치의 커밋을 대상으로 합니다. `state` 외 모든 필드는 선택 사항입니다.

### Request

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `id` | `any` | Yes | 프로젝트의 ID 또는 URL-encoded 경로 |
| `sha` | `string` | Yes | 대상 커밋의 SHA 해시 |

#### Body (`application/json`)
| 이름 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `state` | `enum` | Yes | `pending`, `running`, `success`, `failed`, `canceled`, `skipped` 중 하나 |
| `ref` | `string` | No | 타겟 브랜치 또는 태그 |
| `target_url` | `string` | No | 상태와 연결할 외부 URL (예: CI/CD 빌드 링크) |
| `description` | `string` | No | 상태에 대한 설명 |
| `name` | `string` | No | 다른 시스템과 구분할 job label (`context`와 동일) |
| `context` | `string` | No | 다른 시스템과 구분할 job label (`name`과 동일) |
| `coverage` | `number` | No | 코드 커버리지 비율 |
| `pipeline_id` | `integer` | No | 동일 SHA에 여러 파이프라인이 있을 때 기존 pipeline ID |

### Response

#### `200 OK`
응답 본문은 List all commit statuses의 개별 항목과 동일한 구조를 반환합니다.

| 필드 | 타입 | 설명 |
|------|------|------|
| `id` | integer | 생성/업데이트된 commit status의 ID |
| `sha` | string | 대상 커밋 SHA |
| `ref` | string | 브랜치/태그 참조 |
| `status` | string | 현재 상태 |
| `name` | string | Job 이름 (또는 context) |
| `target_url` | string | 연결된 외부 URL |
| `description` | string | 상태 설명 |
| `created_at` | string | 생성 시각 |
| `started_at` | string | 시작 시각 |
| `finished_at` | string | 완료 시각 |
| `allow_failure` | boolean | 실패 허용 여부 |
| `coverage` | number | 코드 커버리지 |
| `pipeline_id` | integer | 연결된 Pipeline ID |
| `author` | object | 상태 생성자 정보 |

### Errors
| 상태 코드 | 설명 |
|-----------|------|
| `400 Bad Request` | 요청 본문(state 누락 등)이 잘못됨 |
| `401 Unauthorized` | 유효하지 않거나 누락된 인증 토큰 |
| `403 Forbidden` | API 권한(`api`) 부족 |
| `404 Not Found` | 프로젝트 또는 커밋을 찾을 수 없음 |
| `409 Conflict` | 동일 commit status에 대한 다른 업데이트가 진행 중 |

---

## 참고 사항

- 두 엔드포인트 모두 응답에 `author` 객체가 포함되며, `custom_attributes`는 설정된 경우에만 반환됩니다.
- POST 엔드포인트는 `name`과 `context`가 동일한 필드를 가리키며, 하나만 설정하면 됩니다.
- POST 요청 시 동일한 `sha` + `name` 조합이 이미 존재하면 기존 status를 업데이트하고, 없으면 새로 생성합니다.
- 페이지네이션은 GET 엔드포인트에서만 사용 가능합니다.
