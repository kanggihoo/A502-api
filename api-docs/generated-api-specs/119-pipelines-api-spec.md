# 119-pipelines API Spec

---

## 1. List all project pipelines

## 기본 정보
- **기능:** 프로젝트의 모든 파이프라인 목록을 조회한다. 기본적으로 child pipeline은 포함되지 않으며, `source=parent_pipeline`으로 child pipeline을 조회할 수 있다.
- **Endpoint:** `GET /api/v4/projects/{id}/pipelines`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
프로젝트에 속한 모든 파이프라인 목록을 반환한다. `scope`, `status`, `ref`, `sha`, `source` 등 다양한 필터 파라미터로 결과를 좁힐 수 있다. 페이징(page, per_page)을 지원한다.

## Request

### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `string` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `page` | `integer` | N | 현재 페이지 번호 | `1` |
| `per_page` | `integer` | N | 페이지당 항목 수 | `20` |
| `scope` | `string` | N | 파이프라인 조회 범위 | `running` |
| `status` | `string` | N | 파이프라인 상태로 필터 | `success` |
| `ref` | `string` | N | 브랜치/태그 ref로 필터 | `main` |
| `sha` | `string` | N | 커밋 SHA로 필터 | `abc123` |
| `yaml_errors` | `boolean` | N | 잘못된 YAML 설정을 가진 파이프라인만 반환 | `true` |
| `username` | `string` | N | 트리거한 사용자명으로 필터 | `root` |
| `updated_before` | `string` | N | 지정 시간 이전에 업데이트된 파이프라인 필터 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `updated_after` | `string` | N | 지정 시간 이후에 업데이트된 파이프라인 필터 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `created_before` | `string` | N | 지정 시간 이전에 생성된 파이프라인 필터 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `created_after` | `string` | N | 지정 시간 이후에 생성된 파이프라인 필터 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `order_by` | `string` | N | 정렬 기준 필드 | `created_at` |
| `sort` | `string` | N | 정렬 방향 | `desc` |
| `source` | `string` | N | 파이프라인 소스로 필터 | `push` |
| `name` | `string` | N | 파이프라인 이름으로 필터 | `deploy` |

## Response

### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 파이프라인 고유 ID |
| `iid` | `integer` | 프로젝트 내 파이프라인 ID |
| `project_id` | `integer` | 프로젝트 ID |
| `sha` | `string` | 커밋 SHA |
| `ref` | `string` | 브랜치 또는 태그 ref |
| `status` | `string` | 파이프라인 상태 |
| `source` | `string` | 파이프라인 트리거 소스 |
| `created_at` | `string` | 생성 일시 (ISO 8601) |
| `updated_at` | `string` | 업데이트 일시 (ISO 8601) |
| `web_url` | `string` | GitLab 웹 UI URL |

## Errors
| 코드 | 설명 |
|---:|---|
| 400 | Bad Request - 잘못된 요청 |
| 401 | Unauthorized - 인증 실패 |
| 403 | Forbidden - 권한 부족 |
| 404 | Not Found - 프로젝트를 찾을 수 없음 |

---

## 2. Retrieve the latest pipeline

## 기본 정보
- **기능:** 프로젝트의 특정 ref에서 가장 최근 커밋에 대한 최신 파이프라인을 조회한다. 해당 커밋에 파이프라인이 없으면 403을 반환한다.
- **Endpoint:** `GET /api/v4/projects/{id}/pipelines/latest`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 ref(브랜치)의 가장 최근 커밋에서 실행된 최신 파이프라인을 반환한다. ref를 생략하면 프로젝트 기본 브랜치를 기준으로 조회한다.

## Request

### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `string` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `ref` | `string` | N | 파이프라인을 조회할 브랜치 ref. 미지정 시 기본 브랜치 사용 | `main` |

## Response

### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 파이프라인 고유 ID |
| `iid` | `integer` | 프로젝트 내 파이프라인 ID |
| `project_id` | `integer` | 프로젝트 ID |
| `sha` | `string` | 커밋 SHA |
| `ref` | `string` | 브랜치 또는 태그 ref |
| `status` | `string` | 파이프라인 상태 |
| `source` | `string` | 파이프라인 트리거 소스 |
| `created_at` | `string` | 생성 일시 (ISO 8601) |
| `updated_at` | `string` | 업데이트 일시 (ISO 8601) |
| `web_url` | `string` | GitLab 웹 UI URL |
| `before_sha` | `string` | 이전 커밋 SHA |
| `tag` | `boolean` | 태그 여부 |
| `yaml_errors` | `string` | YAML 설정 오류 메시지 |
| `user` | `object` | 파이프라인을 트리거한 사용자 정보 |
| `user.id` | `integer` | 사용자 ID |
| `user.username` | `string` | 사용자명 |
| `user.public_email` | `string` | 공개 이메일 |
| `user.name` | `string` | 사용자 이름 |
| `user.state` | `string` | 계정 상태 |
| `user.locked` | `boolean` | 계정 잠김 여부 |
| `user.avatar_url` | `string` | 아바타 URL |
| `user.avatar_path` | `string` | 아바타 경로 |
| `user.custom_attributes` | `array` | 사용자 정의 속성 목록 |
| `user.web_url` | `string` | 사용자 프로필 URL |
| `started_at` | `string` | 시작 일시 (ISO 8601) |
| `finished_at` | `string` | 완료 일시 (ISO 8601) |
| `committed_at` | `string` | 커밋 일시 (ISO 8601) |
| `duration` | `integer` | 실행 시간 (초) |
| `queued_duration` | `integer` | 대기 시간 (초) |
| `coverage` | `number` | 테스트 커버리지 비율 |
| `detailed_status` | `object` | 상세 상태 정보 |
| `detailed_status.icon` | `string` | 상태 아이콘 |
| `detailed_status.text` | `string` | 상태 텍스트 |
| `detailed_status.label` | `string` | 상태 레이블 |
| `detailed_status.group` | `string` | 상태 그룹 |
| `detailed_status.tooltip` | `string` | 툴팁 메시지 |
| `detailed_status.has_details` | `boolean` | 상세 페이지 존재 여부 |
| `detailed_status.details_path` | `string` | 상세 페이지 경로 |
| `detailed_status.illustration` | `object` | 일러스트레이션 정보 |
| `detailed_status.favicon` | `string` | 파비콘 |
| `detailed_status.action` | `string` | 실행 가능한 액션 |
| `archived` | `boolean` | 아카이브 여부 |
| `name` | `string` | 파이프라인 이름 |

## Errors
| 코드 | 설명 |
|---:|---|
| 400 | Bad Request - 잘못된 요청 |
| 401 | Unauthorized - 인증 실패 |
| 403 | Forbidden - 파이프라인이 존재하지 않거나 권한 부족 |
| 404 | Not Found - 프로젝트를 찾을 수 없음 |

---

## 3. Retrieve a pipeline

## 기본 정보
- **기능:** 프로젝트의 특정 파이프라인 단건을 조회한다. child pipeline도 조회 가능하다.
- **Endpoint:** `GET /api/v4/projects/{id}/pipelines/{pipeline_id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
프로젝트 내에서 특정 `pipeline_id`에 해당하는 파이프라인의 상세 정보를 반환한다.

## Request

### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `string` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` |
| `pipeline_id` | `integer` | Y | 파이프라인 ID | `42` |

## Response

### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 파이프라인 고유 ID |
| `iid` | `integer` | 프로젝트 내 파이프라인 ID |
| `project_id` | `integer` | 프로젝트 ID |
| `sha` | `string` | 커밋 SHA |
| `ref` | `string` | 브랜치 또는 태그 ref |
| `status` | `string` | 파이프라인 상태 |
| `source` | `string` | 파이프라인 트리거 소스 |
| `created_at` | `string` | 생성 일시 (ISO 8601) |
| `updated_at` | `string` | 업데이트 일시 (ISO 8601) |
| `web_url` | `string` | GitLab 웹 UI URL |
| `before_sha` | `string` | 이전 커밋 SHA |
| `tag` | `boolean` | 태그 여부 |
| `yaml_errors` | `string` | YAML 설정 오류 메시지 |
| `user` | `object` | 파이프라인을 트리거한 사용자 정보 |
| `user.id` | `integer` | 사용자 ID |
| `user.username` | `string` | 사용자명 |
| `user.public_email` | `string` | 공개 이메일 |
| `user.name` | `string` | 사용자 이름 |
| `user.state` | `string` | 계정 상태 |
| `user.locked` | `boolean` | 계정 잠김 여부 |
| `user.avatar_url` | `string` | 아바타 URL |
| `user.avatar_path` | `string` | 아바타 경로 |
| `user.custom_attributes` | `array` | 사용자 정의 속성 목록 |
| `user.web_url` | `string` | 사용자 프로필 URL |
| `started_at` | `string` | 시작 일시 (ISO 8601) |
| `finished_at` | `string` | 완료 일시 (ISO 8601) |
| `committed_at` | `string` | 커밋 일시 (ISO 8601) |
| `duration` | `integer` | 실행 시간 (초) |
| `queued_duration` | `integer` | 대기 시간 (초) |
| `coverage` | `number` | 테스트 커버리지 비율 |
| `detailed_status` | `object` | 상세 상태 정보 |
| `detailed_status.icon` | `string` | 상태 아이콘 |
| `detailed_status.text` | `string` | 상태 텍스트 |
| `detailed_status.label` | `string` | 상태 레이블 |
| `detailed_status.group` | `string` | 상태 그룹 |
| `detailed_status.tooltip` | `string` | 툴팁 메시지 |
| `detailed_status.has_details` | `boolean` | 상세 페이지 존재 여부 |
| `detailed_status.details_path` | `string` | 상세 페이지 경로 |
| `detailed_status.illustration` | `object` | 일러스트레이션 정보 |
| `detailed_status.favicon` | `string` | 파비콘 |
| `detailed_status.action` | `string` | 실행 가능한 액션 |
| `archived` | `boolean` | 아카이브 여부 |
| `name` | `string` | 파이프라인 이름 |

## Errors
| 코드 | 설명 |
|---:|---|
| 400 | Bad Request - 잘못된 요청 |
| 401 | Unauthorized - 인증 실패 |
| 403 | Forbidden - 권한 부족 |
| 404 | Not Found - 파이프라인을 찾을 수 없음 |

---

## 4. List all jobs by pipeline

## 기본 정보
- **기능:** 특정 파이프라인에 속한 모든 job 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/pipelines/{pipeline_id}/jobs`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 파이프라인에 포함된 모든 CI/CD job의 목록을 반환한다. 재시도된 job 포함 여부(`include_retried`)와 job 범위(`scope`)로 필터링할 수 있다. 페이징(page, per_page)을 지원한다.

## Request

### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `string` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` |
| `pipeline_id` | `integer` | Y | 파이프라인 ID | `42` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `include_retried` | `boolean` | N | 재시도된 job 포함 여부 | `true` |
| `scope` | `any` | N | job 범위로 필터 | `failed` |
| `page` | `integer` | N | 현재 페이지 번호 | `1` |
| `per_page` | `integer` | N | 페이지당 항목 수 | `20` |

## Response

### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | job 고유 ID |
| `status` | `string` | job 상태 |
| `stage` | `string` | job이 속한 스테이지 |
| `name` | `string` | job 이름 |
| `ref` | `string` | 브랜치 또는 태그 ref |
| `tag` | `boolean` | 태그 여부 |
| `coverage` | `number` | 테스트 커버리지 |
| `allow_failure` | `boolean` | 실패 허용 여부 |
| `created_at` | `string` | 생성 일시 (ISO 8601) |
| `started_at` | `string` | 시작 일시 (ISO 8601) |
| `finished_at` | `string` | 완료 일시 (ISO 8601) |
| `erased_at` | `string` | 삭제 일시 (ISO 8601) |
| `duration` | `number` | 실행 시간 (초) |
| `queued_duration` | `number` | 대기 시간 (초) |
| `user` | `object` | job을 트리거한 사용자 정보 |
| `user.id` | `integer` | 사용자 ID |
| `user.username` | `string` | 사용자명 |
| `user.public_email` | `string` | 공개 이메일 |
| `user.name` | `string` | 사용자 이름 |
| `user.state` | `string` | 계정 상태 |
| `user.locked` | `boolean` | 계정 잠김 여부 |
| `user.avatar_url` | `string` | 아바타 URL |
| `user.avatar_path` | `string` | 아바타 경로 |
| `user.custom_attributes` | `array` | 사용자 정의 속성 |
| `user.web_url` | `string` | 사용자 프로필 URL |
| `user.created_at` | `string` | 계정 생성일 |
| `user.bio` | `string` | 자기소개 |
| `user.location` | `string` | 위치 |
| `user.linkedin` | `string` | LinkedIn ID |
| `user.twitter` | `string` | Twitter ID |
| `user.discord` | `string` | Discord ID |
| `user.website_url` | `string` | 웹사이트 URL |
| `user.github` | `string` | GitHub ID |
| `user.job_title` | `string` | 직함 |
| `user.pronouns` | `string` | 대명사 |
| `user.organization` | `string` | 조직 |
| `user.bot` | `boolean` | 봇 계정 여부 |
| `user.work_information` | `string` | 업무 정보 |
| `user.followers` | `string` | 팔로워 수 |
| `user.following` | `string` | 팔로잉 수 |
| `user.is_followed` | `string` | 현재 사용자의 팔로우 여부 |
| `user.local_time` | `string` | 사용자 로컬 시간 |
| `commit` | `object` | 관련 커밋 정보 |
| `commit.id` | `string` | 커밋 SHA |
| `commit.short_id` | `string` | 단축 SHA |
| `commit.created_at` | `string` | 생성 일시 |
| `commit.parent_ids` | `array` | 부모 커밋 ID 목록 |
| `commit.title` | `string` | 커밋 제목 |
| `commit.message` | `string` | 커밋 메시지 |
| `commit.author_name` | `string` | 작성자 이름 |
| `commit.author_email` | `string` | 작성자 이메일 |
| `commit.authored_date` | `string` | 작성 일시 |
| `commit.committer_name` | `string` | 커밋터 이름 |
| `commit.committer_email` | `string` | 커밋터 이메일 |
| `commit.trailers` | `object` | Git trailers |
| `commit.extended_trailers` | `object` | 확장 Git trailers |
| `commit.web_url` | `string` | 커밋 웹 URL |
| `pipeline` | `object` | job이 속한 파이프라인 요약 정보 |
| `pipeline.id` | `integer` | 파이프라인 ID |
| `pipeline.iid` | `integer` | 프로젝트 내 파이프라인 ID |
| `pipeline.project_id` | `integer` | 프로젝트 ID |
| `pipeline.sha` | `string` | 커밋 SHA |
| `pipeline.ref` | `string` | 브랜치/태그 ref |
| `pipeline.status` | `string` | 파이프라인 상태 |
| `pipeline.source` | `string` | 트리거 소스 |
| `pipeline.created_at` | `string` | 파이프라인 생성 일시 |
| `pipeline.updated_at` | `string` | 파이프라인 업데이트 일시 |
| `pipeline.web_url` | `string` | 파이프라인 웹 URL |
| `failure_reason` | `string` | 실패 사유 |
| `web_url` | `string` | job 웹 URL |
| `project` | `string` | job이 속한 프로젝트 경로 |
| `artifacts_file` | `object` | 아티팩트 파일 정보 |
| `artifacts_file.filename` | `string` | 아티팩트 파일명 |
| `artifacts_file.size` | `integer` | 아티팩트 파일 크기 |
| `artifacts` | `array` | 아티팩트 목록 |
| `artifacts[].file_type` | `string` | 아티팩트 파일 타입 |
| `artifacts[].size` | `integer` | 아티팩트 크기 |
| `artifacts[].filename` | `string` | 아티팩트 파일명 |
| `artifacts[].file_format` | `string` | 아티팩트 파일 포맷 |
| `runner` | `object` | job을 실행한 러너 정보 |
| `runner.id` | `integer` | 러너 ID |
| `runner.description` | `string` | 러너 설명 |
| `runner.ip_address` | `string` | 러너 IP 주소 |
| `runner.active` | `boolean` | 활성 여부 |
| `runner.paused` | `boolean` | 일시중지 여부 |
| `runner.is_shared` | `boolean` | 공유 러너 여부 |
| `runner.runner_type` | `string` | 러너 유형 |
| `runner.name` | `string` | 러너 이름 |
| `runner.online` | `boolean` | 온라인 여부 |
| `runner.created_by` | `object` | 생성자 정보 |
| `runner.created_at` | `string` | 생성 일시 |
| `runner.status` | `string` | 러너 상태 |
| `runner.job_execution_status` | `string` | job 실행 상태 |
| `runner_manager` | `object` | 러너 매니저 정보 |
| `runner_manager.id` | `integer` | 매니저 ID |
| `runner_manager.system_id` | `string` | 시스템 ID |
| `runner_manager.version` | `string` | 버전 |
| `runner_manager.revision` | `string` | 리비전 |
| `runner_manager.platform` | `string` | 플랫폼 |
| `runner_manager.architecture` | `string` | 아키텍처 |
| `runner_manager.created_at` | `string` | 생성 일시 |
| `runner_manager.contacted_at` | `string` | 마지막 접촉 일시 |
| `runner_manager.ip_address` | `string` | IP 주소 |
| `runner_manager.status` | `string` | 상태 |
| `runner_manager.job_execution_status` | `string` | job 실행 상태 |
| `artifacts_expire_at` | `string` | 아티팩트 만료 일시 |
| `archived` | `boolean` | 아카이브 여부 |
| `tag_list` | `array` | 태그 목록 |

## Errors
| 코드 | 설명 |
|---:|---|
| 400 | Bad Request - 잘못된 요청 |
| 401 | Unauthorized - 인증 실패 |
| 403 | Forbidden - 권한 부족 |
| 404 | Not Found - 파이프라인을 찾을 수 없음 |

---

## 5. Retrieve a test report for a pipeline

## 기본 정보
- **기능:** 특정 파이프라인의 테스트 리포트를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/pipelines/{pipeline_id}/test_report`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
파이프라인에서 실행된 전체 테스트 결과를 요약 및 상세(suite별, 케이스별) 정보로 반환한다. `test_suites` 아래에 각 테스트 스위트와 개별 테스트 케이스의 상태, 실행 시간, 실패 정보 등을 포함한다.

## Request

### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `string` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` |
| `pipeline_id` | `integer` | Y | 파이프라인 ID | `42` |

## Response

### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `total_time` | `integer` | 전체 테스트 실행 시간 |
| `total_count` | `integer` | 전체 테스트 케이스 수 |
| `success_count` | `integer` | 성공한 테스트 수 |
| `failed_count` | `integer` | 실패한 테스트 수 |
| `skipped_count` | `integer` | 스킵된 테스트 수 |
| `error_count` | `integer` | 에러 발생 테스트 수 |
| `test_suites` | `array` | 테스트 스위트 목록 |
| `test_suites[].name` | `string` | 스위트 이름 |
| `test_suites[].total_time` | `integer` | 스위트 실행 시간 |
| `test_suites[].total_count` | `integer` | 스위트 내 테스트 수 |
| `test_suites[].success_count` | `integer` | 스위트 내 성공 수 |
| `test_suites[].failed_count` | `integer` | 스위트 내 실패 수 |
| `test_suites[].skipped_count` | `integer` | 스위트 내 스킵 수 |
| `test_suites[].error_count` | `integer` | 스위트 내 에러 수 |
| `test_suites[].suite_error` | `string` | 스위트 에러 메시지 |
| `test_suites[].test_cases` | `array` | 개별 테스트 케이스 목록 |
| `test_suites[].test_cases[].status` | `string` | 테스트 결과 상태 |
| `test_suites[].test_cases[].name` | `string` | 테스트 이름 |
| `test_suites[].test_cases[].classname` | `string` | 테스트 클래스명 |
| `test_suites[].test_cases[].file` | `string` | 테스트 파일 경로 |
| `test_suites[].test_cases[].execution_time` | `integer` | 실행 시간 |
| `test_suites[].test_cases[].system_output` | `string` | 시스템 출력 |
| `test_suites[].test_cases[].stack_trace` | `string` | 스택 트레이스 |
| `test_suites[].test_cases[].recent_failures` | `object` | 최근 실패 이력 |
| `test_suites[].test_cases[].attachment_url` | `string` | 첨부 파일 URL |

## Errors
| 코드 | 설명 |
|---:|---|
| 400 | Bad Request - 잘못된 요청 |
| 401 | Unauthorized - 인증 실패 |
| 403 | Forbidden - 권한 부족 |
| 404 | Not Found - 파이프라인을 찾을 수 없음 |

---

## 6. Retrieve a test report summary for a pipeline

## 기본 정보
- **기능:** 특정 파이프라인의 테스트 리포트 요약 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/pipelines/{pipeline_id}/test_report_summary`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
전체 테스트 리포트보다 간결한 형태로 파이프라인의 테스트 결과 요약을 반환한다. 전체 통계(`total`)와 테스트 스위트별 상세를 포함하며, 각 스위트에 연결된 build ID도 함께 제공한다.

## Request

### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `string` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` |
| `pipeline_id` | `integer` | Y | 파이프라인 ID | `42` |

## Response

### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `total` | `object` | 전체 테스트 요약 통계 |
| `test_suites` | `object` | 테스트 스위트별 상세 정보 |
| `test_suites.name` | `string` | 스위트 이름 |
| `test_suites.total_time` | `integer` | 스위트 실행 시간 |
| `test_suites.total_count` | `integer` | 스위트 내 테스트 수 |
| `test_suites.success_count` | `integer` | 스위트 내 성공 수 |
| `test_suites.failed_count` | `integer` | 스위트 내 실패 수 |
| `test_suites.skipped_count` | `integer` | 스위트 내 스킵 수 |
| `test_suites.error_count` | `integer` | 스위트 내 에러 수 |
| `test_suites.suite_error` | `string` | 스위트 에러 메시지 |
| `test_suites.test_cases` | `array` | 개별 테스트 케이스 목록 |
| `test_suites.test_cases[].status` | `string` | 테스트 결과 상태 |
| `test_suites.test_cases[].name` | `string` | 테스트 이름 |
| `test_suites.test_cases[].classname` | `string` | 테스트 클래스명 |
| `test_suites.test_cases[].file` | `string` | 테스트 파일 경로 |
| `test_suites.test_cases[].execution_time` | `integer` | 실행 시간 |
| `test_suites.test_cases[].system_output` | `string` | 시스템 출력 |
| `test_suites.test_cases[].stack_trace` | `string` | 스택 트레이스 |
| `test_suites.test_cases[].recent_failures` | `object` | 최근 실패 이력 |
| `test_suites.test_cases[].attachment_url` | `string` | 첨부 파일 URL |
| `test_suites.build_ids` | `array` | 이 스위트와 연결된 build ID 목록 |

## Errors
| 코드 | 설명 |
|---:|---|
| 400 | Bad Request - 잘못된 요청 |
| 401 | Unauthorized - 인증 실패 |
| 403 | Forbidden - 권한 부족 |
| 404 | Not Found - 파이프라인을 찾을 수 없음 |

---

## 7. Retry jobs in a pipeline

## 기본 정보
- **기능:** 파이프라인에서 실패했거나 취소된 job을 재시도한다. 재시도할 job이 없으면 아무 동작도 하지 않는다.
- **Endpoint:** `POST /api/v4/projects/{id}/pipelines/{pipeline_id}/retry`
- **인증:** Bearer Token 필요
- **권한:** `api`
- **멱등성:** 미지원 (POST는 멱등하지 않음)

## 설명
실패(failed) 또는 취소(canceled) 상태인 job을 새로 실행하여 파이프라인을 재개한다. 성공 시 새로운 파이프라인 객체를 반환한다. 재시도할 job이 없으면 파이프라인 상태는 그대로 유지된다.

## Request

### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `string` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` |
| `pipeline_id` | `integer` | Y | 파이프라인 ID | `42` |

### Body
없음 (POST 본문 불필요)

## Response

### `201 Created`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 파이프라인 고유 ID |
| `iid` | `integer` | 프로젝트 내 파이프라인 ID |
| `project_id` | `integer` | 프로젝트 ID |
| `sha` | `string` | 커밋 SHA |
| `ref` | `string` | 브랜치 또는 태그 ref |
| `status` | `string` | 파이프라인 상태 |
| `source` | `string` | 파이프라인 트리거 소스 |
| `created_at` | `string` | 생성 일시 (ISO 8601) |
| `updated_at` | `string` | 업데이트 일시 (ISO 8601) |
| `web_url` | `string` | GitLab 웹 UI URL |
| `before_sha` | `string` | 이전 커밋 SHA |
| `tag` | `boolean` | 태그 여부 |
| `yaml_errors` | `string` | YAML 설정 오류 메시지 |
| `user` | `object` | 파이프라인을 트리거한 사용자 정보 |
| `user.id` | `integer` | 사용자 ID |
| `user.username` | `string` | 사용자명 |
| `user.public_email` | `string` | 공개 이메일 |
| `user.name` | `string` | 사용자 이름 |
| `user.state` | `string` | 계정 상태 |
| `user.locked` | `boolean` | 계정 잠김 여부 |
| `user.avatar_url` | `string` | 아바타 URL |
| `user.avatar_path` | `string` | 아바타 경로 |
| `user.custom_attributes` | `array` | 사용자 정의 속성 목록 |
| `user.web_url` | `string` | 사용자 프로필 URL |
| `started_at` | `string` | 시작 일시 (ISO 8601) |
| `finished_at` | `string` | 완료 일시 (ISO 8601) |
| `committed_at` | `string` | 커밋 일시 (ISO 8601) |
| `duration` | `integer` | 실행 시간 (초) |
| `queued_duration` | `integer` | 대기 시간 (초) |
| `coverage` | `number` | 테스트 커버리지 비율 |
| `detailed_status` | `object` | 상세 상태 정보 |
| `detailed_status.icon` | `string` | 상태 아이콘 |
| `detailed_status.text` | `string` | 상태 텍스트 |
| `detailed_status.label` | `string` | 상태 레이블 |
| `detailed_status.group` | `string` | 상태 그룹 |
| `detailed_status.tooltip` | `string` | 툴팁 메시지 |
| `detailed_status.has_details` | `boolean` | 상세 페이지 존재 여부 |
| `detailed_status.details_path` | `string` | 상세 페이지 경로 |
| `detailed_status.illustration` | `object` | 일러스트레이션 정보 |
| `detailed_status.favicon` | `string` | 파비콘 |
| `detailed_status.action` | `string` | 실행 가능한 액션 |
| `archived` | `boolean` | 아카이브 여부 |

## Errors
| 코드 | 설명 |
|---:|---|
| 400 | Bad Request - 잘못된 요청 |
| 401 | Unauthorized - 인증 실패 |
| 403 | Forbidden - 권한 부족 |
| 404 | Not Found - 파이프라인을 찾을 수 없음 |
