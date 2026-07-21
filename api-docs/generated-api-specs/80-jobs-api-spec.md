# 80-jobs API Spec

---

## 1. List all jobs processed by a runner

## 기본 정보
- **기능:** 특정 Runner에서 처리 중이거나 처리한 모든 Job 목록을 조회합니다. 사용자는 Reporter, Developer, Maintainer, Owner 역할 이상이어야 합니다.
- **Endpoint:** `GET /api/v4/runners/{id}/jobs`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 Runner ID에 대해 해당 Runner가 처리했거나 처리 중인 Job 목록을 반환합니다. 결과는 사용자가 접근 권한이 있는 프로젝트로 제한됩니다.

## Request
### Headers
| 이름 | 필수 | 설명 |
| --- | --- | --- |
| `PRIVATE-TOKEN` | Yes | GitLab Personal Access Token |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `integer` | Yes | Runner ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `system_id` | `string` | No | Runner Manager 연결된 System ID |
| `status` | `string` | No | Job 상태 필터 |
| `order_by` | `string` | No | 정렬 기준 (`id`) |
| `sort` | `string` | No | 정렬 방향 (`asc` / `desc`). `order_by`와 함께 사용 |
| `cursor` | `string` | No | 커서 기반 페이지네이션을 위한 커서 |
| `page` | `integer` | No | 페이지 번호 |
| `per_page` | `integer` | No | 페이지 당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `id` | `integer` | Job ID |
| `status` | `string` | Job 상태 |
| `stage` | `string` | CI/CD Stage 이름 |
| `name` | `string` | Job 이름 |
| `ref` | `string` | 브랜치/태그 참조 |
| `tag` | `boolean` | 태그 실행 여부 |
| `coverage` | `number` | 커버리지 |
| `allow_failure` | `boolean` | 실패 허용 여부 |
| `created_at` | `string` (datetime) | 생성 시간 |
| `started_at` | `string` (datetime) | 시작 시간 |
| `finished_at` | `string` (datetime) | 종료 시간 |
| `erased_at` | `string` (datetime) | 삭제 시간 |
| `duration` | `number` | 실행 소요 시간(초) |
| `queued_duration` | `number` | 대기열 소요 시간(초) |
| `failure_reason` | `string` | 실패 사유 |
| `web_url` | `string` | Job 페이지 URL |
| `user` | `object` | Job을 트리거한 사용자 정보 |
| `user.id` | `integer` | 사용자 ID |
| `user.username` | `string` | 사용자명 |
| `user.public_email` | `string` | 공개 이메일 |
| `user.name` | `string` | 사용자 이름 |
| `user.state` | `string` | 계정 상태 (`active`, `blocked`) |
| `user.locked` | `boolean` | 계정 잠금 여부 |
| `user.avatar_url` | `string` | 아바타 URL |
| `user.avatar_path` | `string` | 아바타 경로 |
| `user.custom_attributes` | `array[object]` | 커스텀 속성 목록 |
| `user.custom_attributes[].key` | `string` | 속성 키 |
| `user.custom_attributes[].value` | `string` | 속성 값 |
| `user.web_url` | `string` | 사용자 프로필 URL |
| `user.created_at` | `string` (datetime) | 계정 생성일 |
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
| `user.is_followed` | `string` | 현재 사용자가 팔로우 중인지 여부 |
| `user.local_time` | `string` | 현지 시간 |
| `commit` | `object` | 관련 커밋 정보 |
| `commit.id` | `string` | 커밋 SHA |
| `commit.short_id` | `string` | 짧은 SHA |
| `commit.created_at` | `string` (datetime) | 커밋 생성 시간 |
| `commit.parent_ids` | `array[string]` | 부모 커밋 SHA 목록 |
| `commit.title` | `string` | 커밋 제목 |
| `commit.message` | `string` | 커밋 메시지 |
| `commit.author_name` | `string` | 작성자 이름 |
| `commit.author_email` | `string` | 작성자 이메일 |
| `commit.authored_date` | `string` (datetime) | 작성일 |
| `commit.committer_name` | `string` | 커미터 이름 |
| `commit.committer_email` | `string` | 커미터 이메일 |
| `commit.committed_date` | `string` (datetime) | 커밋일 |
| `commit.trailers` | `object` | Git trailers |
| `commit.extended_trailers` | `object` | 확장 Git trailers |
| `commit.web_url` | `string` | 커밋 페이지 URL |
| `pipeline` | `object` | 파이프라인 정보 |
| `pipeline.id` | `integer` | 파이프라인 ID |
| `pipeline.iid` | `integer` | 프로젝트 내부 파이프라인 ID |
| `pipeline.project_id` | `integer` | 프로젝트 ID |
| `pipeline.sha` | `string` | 파이프라인 SHA |
| `pipeline.ref` | `string` | 브랜치/태그 참조 |
| `pipeline.status` | `string` | 파이프라인 상태 |
| `pipeline.source` | `string` | 트리거 소스 |
| `pipeline.created_at` | `string` (datetime) | 생성 시간 |
| `pipeline.updated_at` | `string` (datetime) | 업데이트 시간 |
| `pipeline.web_url` | `string` | 파이프라인 페이지 URL |
| `project` | `object` | 프로젝트 정보 |
| `project.id` | `integer` | 프로젝트 ID |
| `project.description` | `string` | 프로젝트 설명 |
| `project.name` | `string` | 프로젝트 이름 |
| `project.name_with_namespace` | `string` | 네임스페이스 포함 이름 |
| `project.path` | `string` | 프로젝트 경로 |
| `project.path_with_namespace` | `string` | 네임스페이스 포함 경로 |
| `project.created_at` | `string` (datetime) | 생성 시간 |

## Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400 Bad Request` | 요청 파라미터 오류 |
| `401 Unauthorized` | 인증 토큰이 없거나 유효하지 않음 |
| `403 Forbidden` | 접근 권한 없음 |
| `404 Not Found` | Runner를 찾을 수 없음 |

---

## 2. Download the artifacts file for job

## 기본 정보
- **기능:** 특정 Job의 아티팩트 파일을 다운로드합니다.
- **Endpoint:** `GET /api/v4/jobs/{id}/artifacts`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 Job ID에 해당하는 아티팩트 파일을 다운로드합니다. `direct_download` 파라미터를 사용하면 원격 스토리지에서 직접 다운로드할 수 있습니다.

## Request
### Headers
| 이름 | 필수 | 설명 |
| --- | --- | --- |
| `PRIVATE-TOKEN` | Yes | GitLab Personal Access Token |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `integer` | Yes | Job ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `token` | `string` | No | Job 인증 토큰 (Job token으로 인증 시 사용) |
| `direct_download` | `boolean` | No | 원격 스토리지에서 직접 다운로드 (프록시 우회) |

## Response
### `200 OK`
응답 본문은 아티팩트 파일의 바이너리 데이터입니다. Content-Type은 아티팩트 파일 형식에 따라 달라집니다.

### `302 Found`
리다이렉트 응답입니다. `direct_download=true` 설정 시 원격 스토리지 URL로 리다이렉트됩니다.

## Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400 Bad Request` | 요청 파라미터 오류 |
| `401 Unauthorized` | 인증 토큰이 없거나 유효하지 않음 |
| `403 Forbidden` | 접근 권한 없음 |
| `404 Not Found` | 아티팩트를 찾을 수 없음 |
| `429 Too Many Requests` | 요청 속도 제한 초과 |
