# 24 - CI Jobs API Spec

---

## 01 - List all jobs for a project

### 기본 정보
- **기능:** 특정 프로젝트의 모든 CI/CD Job 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/jobs`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원 (조회만 수행)

### 설명
프로젝트에 속한 모든 CI/CD Job을 반환한다. 페이지네이션을 지원하며 기본적으로 20개의 결과를 반환한다. `scope`나 `ref` 파라미터로 결과를 필터링할 수 있다.

### Request
#### Headers
| Name | Value |
| --- | --- |
| `Authorization` | `Bearer <token>` |
| `Accept` | `application/json` |

#### Path parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |

#### Query parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scope` | `array<string>` | No | 조회할 Job 범위 (예: `pending`, `running`, `failed`, `success`) |
| `ref` | `string` | No | 특정 브랜치(ref)로 Job 필터링 |
| `page` | `integer` | No | 페이지 번호 (기본값: 1) |
| `per_page` | `integer` | No | 페이지당 항목 수 (기본값: 20) |

### Response
#### `200 OK`
```json
{
  "id": "integer",
  "status": "string",
  "stage": "string",
  "name": "string",
  "ref": "string",
  "tag": "boolean",
  "coverage": "number",
  "allow_failure": "boolean",
  "created_at": "string (datetime)",
  "started_at": "string (datetime)",
  "finished_at": "string (datetime)",
  "erased_at": "string (datetime)",
  "duration": "number (seconds)",
  "queued_duration": "number (seconds)",
  "failure_reason": "string",
  "web_url": "string",
  "project": "string",
  "artifacts_expire_at": "string (datetime)",
  "archived": "boolean",
  "tag_list": "array<string>",
  "user": { "id": "integer", "username": "string", "name": "string", "state": "string", "web_url": "string" },
  "commit": { "id": "string", "short_id": "string", "title": "string", "message": "string", "web_url": "string" },
  "pipeline": { "id": "integer", "iid": "integer", "project_id": "integer", "sha": "string", "ref": "string", "status": "string", "source": "string", "web_url": "string" },
  "artifacts_file": { "filename": "string", "size": "integer" },
  "artifacts": [{ "file_type": "string", "size": "integer", "filename": "string", "file_format": "string" }],
  "runner": { "id": "integer", "description": "string", "active": "boolean", "runner_type": "string", "status": "string" }
}
```

| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `id` | `integer` | Job 고유 ID |
| `status` | `string` | Job 상태 (pending/running/failed/success/canceled 등) |
| `stage` | `string` | CI/CD 파이프라인 내 stage 이름 |
| `name` | `string` | Job 이름 |
| `ref` | `string` | 연결된 브랜치/태그 참조 |
| `tag` | `boolean` | Tag 실행 여부 |
| `coverage` | `number` | 코드 커버리지 값 (설정된 경우) |
| `allow_failure` | `boolean` | 실패 허용 여부 |
| `created_at` | `string` | Job 생성 일시 |
| `started_at` | `string` | Job 시작 일시 |
| `finished_at` | `string` | Job 완료 일시 |
| `duration` | `number` | 실행에 소요된 시간 (초) |
| `queued_duration` | `number` | 대기열에서 소요된 시간 (초) |
| `failure_reason` | `string` | 실패 사유 (실패한 경우) |
| `web_url` | `string` | GitLab 웹 UI에서의 Job 페이지 URL |
| `pipeline` | `object` | 연결된 파이프라인 정보 (id, iid, sha, ref, status, web_url) |
| `user` | `object` | Job을 트리거한 사용자 정보 |
| `commit` | `object` | 연결된 커밋 정보 |
| `runner` | `object` | Job을 실행한 Runner 정보 |
| `artifacts` | `array` | 생성된 아티팩트 목록 |
| `artifacts_file` | `object` | 아티팩트 파일 정보 (filename, size) |

---

## 02 - Retrieve a job

### 기본 정보
- **기능:** 특정 Job의 상세 정보 조회
- **Endpoint:** `GET /api/v4/projects/{id}/jobs/{job_id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원 (조회만 수행)

### 설명
Job ID를 기준으로 단일 CI/CD Job의 상세 정보를 반환한다. 응답 구조는 Job 목록 조회와 동일한 Job 객체 스키마를 사용한다.

### Request
#### Headers
| Name | Value |
| --- | --- |
| `Authorization` | `Bearer <token>` |
| `Accept` | `application/json` |

#### Path parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `job_id` | `integer` | Yes | 조회할 Job ID |

### Response
#### `200 OK`
01 (List all jobs)과 동일한 Job 객체 스키마를 반환한다. 위 `01` 섹션의 `200 OK` 필드 표를 참조.

---

## 05 - Retry a job

### 기본 정보
- **기능:** 실패하거나 취소된 Job 재시도
- **Endpoint:** `POST /api/v4/projects/{id}/jobs/{job_id}/retry`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** 미지원 (호출 시마다 새로운 Job 실행)

### 설명
지정된 Job을 재시도한다. 실패(`failed`) 또는 취소(`canceled`) 상태의 Job에 대해 새 Job을 생성하여 실행한다. 성공 시 `201 Created` 상태 코드와 함께 새로 생성된 Job 객체를 반환한다.

### Request
#### Headers
| Name | Value |
| --- | --- |
| `Authorization` | `Bearer <token>` |
| `Content-Type` | `application/json` |
| `Accept` | `application/json` |

#### Path parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `job_id` | `integer` | Yes | 재시도할 Job ID |

#### Body (application/json)
| 필드 | 타입 | Required | 설명 |
| --- | --- | --- | --- |
| `inputs` | `object` | No | Job에 전달할 입력 값 (key-value) |

예시:
```json
{
  "inputs": {
    "version": "1.2.3",
    "deploy_target": "staging"
  }
}
```

### Response
#### `201 Created`
01 (List all jobs)과 동일한 Job 객체 스키마를 반환한다. 위 `01` 섹션의 `200 OK` 필드 표를 참조. 응답 상태 코드는 `201`이다.

---

## Errors (공통)

| 상태 코드 | 설명 |
| --- | --- |
| `400 Bad Request` | 요청 파라미터가 유효하지 않음 |
| `401 Unauthorized` | 유효하지 않거나 누락된 인증 토큰 |
| `403 Forbidden` | 요청에 필요한 권한이 없음 (`read_api` / `api`) |
| `404 Not Found` | 프로젝트 또는 Job이 존재하지 않음 |
