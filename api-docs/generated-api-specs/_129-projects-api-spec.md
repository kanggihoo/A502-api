# 129-projects API Spec

---

## 1. List all projects

## 기본 정보

- **기능:** 모든 프로젝트 목록을 조회한다. 인증되지 않은 요청은 공개 프로젝트만 제한된 속성과 함께 반환한다.
- **Endpoint:** `GET /api/v4/projects`
- **인증:** Bearer Token 필요 (GitLab REST API는 모두 OAuth2/PAT 필요함. 읽기 전용은 `read_api` scope, 쓰기는 `api` scope 필요)
- **권한:** `read_api` (읽기 전용) / `api` (읽기+쓰기)
- **멱등성:** GET은 멱등, POST/PUT은 미지원

## 설명

모든 GitLab 프로젝트의 목록을 반환한다. 인증되지 않은 요청은 공개(public) 프로젝트만 제한된 속성과 함께 반환한다. `search`, `visibility`, `owned`, `starred` 등 다양한 필터 파라미터로 결과를 좁힐 수 있으며, 커스텀 속성(custom attributes)으로도 필터링할 수 있다. 페이징(page, per_page)을 지원한다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

없음

### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `order_by` | `string` | N | 정렬 기준 필드 (admin 전용 필드 포함) | `created_at` |
| `sort` | `string` | N | 정렬 방향 | `asc` |
| `archived` | `boolean` | N | 보관(archived) 여부로 필터 | `false` |
| `visibility` | `string` | N | 공개 범위로 필터 | `public` |
| `search` | `string` | N | 검색어와 일치하는 프로젝트 반환 | `my-project` |
| `search_namespaces` | `boolean` | N | 검색 시 상위 네임스페이스 포함 여부 | `true` |
| `owned` | `boolean` | N | 인증 사용자가 소유한 프로젝트만 필터 | `true` |
| `starred` | `boolean` | N | 즐겨찾기(star)한 프로젝트만 필터 | `true` |
| `imported` | `boolean` | N | 인증 사용자가 가져온(import) 프로젝트만 필터 | `true` |
| `membership` | `boolean` | N | 현재 사용자가 멤버인 프로젝트만 필터 | `true` |
| `with_issues_enabled` | `boolean` | N | 이슈 기능이 활성화된 프로젝트만 필터 | `true` |
| `with_merge_requests_enabled` | `boolean` | N | MR 기능이 활성화된 프로젝트만 필터 | `true` |
| `with_programming_language` | `string` | N | 특정 프로그래밍 언어를 사용하는 저장소만 필터 | `Python` |
| `min_access_level` | `integer` | N | 인증 사용자의 최소 액세스 레벨로 필터 | `10` |
| `id_after` | `integer` | N | 지정 ID보다 큰 프로젝트만 반환 | `100` |
| `id_before` | `integer` | N | 지정 ID보다 작은 프로젝트만 반환 | `500` |
| `last_activity_after` | `string` | N | 지정 시간 이후 활동이 있는 프로젝트만 반환 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `last_activity_before` | `string` | N | 지정 시간 이전 활동이 있는 프로젝트만 반환 (ISO 8601) | `2024-12-31T23:59:59Z` |
| `repository_storage` | `string` | N | 저장소가 위치한 스토리지 샤드 (admin 전용) | `default` |
| `topic` | `array` | N | 모든 토픽을 가진 프로젝트만 반환 (쉼표 구분) | `ruby,rails` |
| `topic_id` | `integer` | N | 특정 토픽 ID가 할당된 프로젝트만 반환 | `1` |
| `updated_before` | `string` | N | 지정 시간 이전에 업데이트된 프로젝트만 반환 (ISO 8601) | `2024-06-01T00:00:00Z` |
| `updated_after` | `string` | N | 지정 시간 이후에 업데이트된 프로젝트만 반환 (ISO 8601) | `2024-06-01T00:00:00Z` |
| `include_pending_delete` | `boolean` | N | 삭제 대기(pending delete) 상태의 프로젝트 포함 (admin 전용) | `false` |
| `marked_for_deletion_on` | `string` | N | 삭제 예정일로 필터 | `2024-12-31` |
| `active` | `boolean` | N | 보관되지 않고 삭제 예정도 아닌 활성 프로젝트만 필터 | `true` |
| `wiki_checksum_failed` | `boolean` | N | Wiki 체크섬이 실패한 프로젝트만 필터 | `false` |
| `repository_checksum_failed` | `boolean` | N | 저장소 체크섬이 실패한 프로젝트만 필터 | `false` |
| `include_hidden` | `boolean` | N | 숨겨진 프로젝트 포함 (admin 전용) | `false` |
| `page` | `integer` | N | 현재 페이지 번호 | `1` |
| `per_page` | `integer` | N | 페이지당 항목 수 | `20` |
| `simple` | `boolean` | N | ID, URL, name, path만 반환 (간략 모드) | `false` |
| `statistics` | `boolean` | N | 프로젝트 통계 포함 | `false` |
| `with_custom_attributes` | `boolean` | N | 커스텀 속성을 응답에 포함 | `false` |
| `custom_attributes` | `object` | N | 커스텀 속성으로 필터 | `{"key":"value"}` |

### Body

없음 (GET 요청)

## Response

### `200 OK`

응답은 프로젝트 객체의 배열이다. 각 프로젝트 객체의 필드는 다음과 같다.

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | 프로젝트 고유 ID | `1` |
| `description` | `string` | 프로젝트 설명 | `"My example project"` |
| `name` | `string` | 프로젝트 이름 | `"example-project"` |
| `name_with_namespace` | `string` | 네임스페이스를 포함한 전체 이름 | `"John Doe / example-project"` |
| `path` | `string` | 프로젝트 경로 | `"example-project"` |
| `path_with_namespace` | `string` | 네임스페이스를 포함한 전체 경로 | `"john-doe/example-project"` |
| `created_at` | `string` | 생성 일시 (ISO 8601) | `"2024-01-01T00:00:00.000Z"` |
| `default_branch` | `string` | 기본 브랜치 이름 | `"main"` |
| `tag_list` | `array[string]` | 태그 목록 | `["stable","production"]` |
| `topics` | `array[string]` | 토픽 목록 | `["ruby","rails"]` |
| `ssh_url_to_repo` | `string` | SSH 저장소 URL | `"git@gitlab.example.com:john-doe/example-project.git"` |
| `http_url_to_repo` | `string` | HTTP 저장소 URL | `"https://gitlab.example.com/john-doe/example-project.git"` |
| `web_url` | `string` | 웹 브라우저 URL | `"https://gitlab.example.com/john-doe/example-project"` |
| `readme_url` | `string` | README 파일 URL | `"https://gitlab.example.com/john-doe/example-project/-/blob/main/README.md"` |
| `forks_count` | `integer` | 포크 수 | `3` |
| `license_url` | `string` | 라이선스 URL | `"https://gitlab.example.com/john-doe/example-project/blob/main/LICENSE"` |
| `license` | `object` | 라이선스 정보 | `{"key":"mit","name":"MIT License","nickname":null,"html_url":"https://opensource.org/licenses/MIT","source_url":"https://opensource.org/licenses/MIT"}` |
| `avatar_url` | `string` | 아바타 이미지 URL | `"https://gitlab.example.com/uploads/avatar.png"` |
| `star_count` | `integer` | 즐겨찾기(star) 수 | `10` |
| `last_activity_at` | `string` | 마지막 활동 일시 (ISO 8601) | `"2024-06-15T12:00:00.000Z"` |
| `visibility` | `string` | 공개 범위 | `"public"` |
| `namespace` | `object` | 네임스페이스 정보 | `{"id":1,"name":"John Doe","path":"john-doe","kind":"user","full_path":"john-doe","parent_id":null,"avatar_url":"https://gitlab.example.com/uploads/avatar.png","web_url":"https://gitlab.example.com/john-doe"}` |
| `custom_attributes` | `object` | 커스텀 속성 (key-value 쌍) | `{"key":"value"}` |
| `repository_storage` | `string` | 저장소가 위치한 스토리지 샤드 (admin 전용) | `"default"` |

### `401 Unauthorized`

토큰이 없거나 유효하지 않은 경우 발생한다.

### `403 Forbidden`

토큰은 유효하지만 필요한 권한(`read_api`)이 없는 경우 발생한다.

### `404 Not Found`

해당 조건에 맞는 프로젝트가 없는 경우 (빈 배열 반환 가능)

---

## 2. Retrieve a project

## 기본 정보

- **기능:** 특정 프로젝트의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}`
- **인증:** Bearer Token 필요 (GitLab REST API는 모두 OAuth2/PAT 필요함. 읽기 전용은 `read_api` scope, 쓰기는 `api` scope 필요)
- **권한:** `read_api` (읽기 전용) / `api` (읽기+쓰기). 단, 공개 프로젝트는 인증 없이도 접근 가능
- **멱등성:** GET은 멱등, POST/PUT은 미지원

## 설명

프로젝트 ID 또는 URL 인코딩된 경로로 특정 프로젝트의 상세 정보를 조회한다. 공개 프로젝트의 경우 인증 없이 접근할 수 있다. 프로젝트 통계(`statistics`), 커스텀 속성(`with_custom_attributes`), 라이선스 데이터(`license`)를 선택적으로 포함할 수 있다. 목록 조회 API보다 더 많은 필드(CI/CD 설정, 접근 레벨, 포크 정보 등)를 반환한다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` 또는 `john-doe%2Fexample-project` |

### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `statistics` | `boolean` | N | 프로젝트 통계 정보 포함 | `true` |
| `with_custom_attributes` | `boolean` | N | 커스텀 속성을 응답에 포함 | `true` |
| `custom_attributes` | `object` | N | 커스텀 속성으로 필터 | `{"key":"value"}` |
| `license` | `boolean` | N | 프로젝트 라이선스 데이터 포함 | `true` |

### Body

없음 (GET 요청)

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | 프로젝트 고유 ID | `1` |
| `description` | `string` | 프로젝트 설명 | `"My example project"` |
| `name` | `string` | 프로젝트 이름 | `"example-project"` |
| `name_with_namespace` | `string` | 네임스페이스를 포함한 전체 이름 | `"John Doe / example-project"` |
| `path` | `string` | 프로젝트 경로 | `"example-project"` |
| `path_with_namespace` | `string` | 네임스페이스를 포함한 전체 경로 | `"john-doe/example-project"` |
| `created_at` | `string` | 생성 일시 (ISO 8601) | `"2024-01-01T00:00:00.000Z"` |
| `default_branch` | `string` | 기본 브랜치 이름 | `"main"` |
| `tag_list` | `array[string]` | 태그 목록 | `["stable","production"]` |
| `topics` | `array[string]` | 토픽 목록 | `["ruby","rails"]` |
| `ssh_url_to_repo` | `string` | SSH 저장소 URL | `"git@gitlab.example.com:john-doe/example-project.git"` |
| `http_url_to_repo` | `string` | HTTP 저장소 URL | `"https://gitlab.example.com/john-doe/example-project.git"` |
| `web_url` | `string` | 웹 브라우저 URL | `"https://gitlab.example.com/john-doe/example-project"` |
| `readme_url` | `string` | README 파일 URL | `"https://gitlab.example.com/john-doe/example-project/-/blob/main/README.md"` |
| `forks_count` | `integer` | 포크 수 | `3` |
| `license_url` | `string` | 라이선스 파일 URL | `"https://gitlab.example.com/john-doe/example-project/blob/main/LICENSE"` |
| `license` | `object` | 라이선스 정보 | `{"key":"mit","name":"MIT License","nickname":null,"html_url":"https://opensource.org/licenses/MIT","source_url":"https://opensource.org/licenses/MIT"}` |
| `avatar_url` | `string` | 아바타 이미지 URL | `"https://gitlab.example.com/uploads/avatar.png"` |
| `star_count` | `integer` | 즐겨찾기(star) 수 | `10` |
| `last_activity_at` | `string` | 마지막 활동 일시 (ISO 8601) | `"2024-06-15T12:00:00.000Z"` |
| `visibility` | `string` | 공개 범위 | `"public"` |
| `namespace` | `object` | 네임스페이스 정보 | `{"id":1,"name":"John Doe","path":"john-doe","kind":"user","full_path":"john-doe","parent_id":null,"avatar_url":"https://gitlab.example.com/uploads/avatar.png","web_url":"https://gitlab.example.com/john-doe"}` |
| `custom_attributes` | `object` | 커스텀 속성 (key-value 쌍) | `{"key":"value"}` |
| `repository_storage` | `string` | 저장소 스토리지 샤드 (admin 전용) | `"default"` |
| `forked_from_project` | `object` | 포크한 원본 프로젝트 정보 | `{"id":10,"name":"origin-project","name_with_namespace":"Team / origin-project","path":"origin-project","path_with_namespace":"team/origin-project","created_at":"2023-01-01T00:00:00.000Z","default_branch":"main","visibility":"public"}` |
| `container_registry_image_prefix` | `string` | 컨테이너 레지스트리 이미지 접두사 | `"registry.gitlab.example.com/john-doe/example-project"` |
| `_links` | `object` | 관련 링크 | `{}` |
| `marked_for_deletion_at` | `string` | 삭제 예정 일시 (ISO 8601) | `"2025-01-01T00:00:00.000Z"` |
| `marked_for_deletion_on` | `string` | 삭제 예정일 | `"2025-01-01"` |
| `packages_enabled` | `boolean` | 패키지 레지스트리 활성화 여부 | `true` |
| `empty_repo` | `boolean` | 빈 저장소 여부 | `false` |
| `archived` | `boolean` | 보관됨(archived) 여부 | `false` |
| `owner` | `object` | 프로젝트 소유자 정보 | `{"id":1,"username":"johndoe","public_email":"john@example.com","name":"John Doe","state":"active","locked":false,"avatar_url":"https://gitlab.example.com/uploads/avatar.png","avatar_path":"","web_url":"https://gitlab.example.com/johndoe"}` |
| `resolve_outdated_diff_discussions` | `boolean` | 오래된 diff 토론 자동 해결 여부 | `false` |
| `container_expiration_policy` | `object` | 컨테이너 레지스트리 만료 정책 | `{"cadence":"7d","enabled":"true","keep_n":"10","older_than":"30d","name_regex":".*","name_regex_keep":"","next_run_at":"2024-07-01T00:00:00.000Z"}` |
| `repository_object_format` | `string` | 저장소 객체 포맷 | `"sha256"` |
| `issues_enabled` | `boolean` | 이슈 기능 활성화 여부 | `true` |
| `merge_requests_enabled` | `boolean` | MR 기능 활성화 여부 | `true` |
| `wiki_enabled` | `boolean` | Wiki 기능 활성화 여부 | `true` |
| `jobs_enabled` | `boolean` | CI/CD Jobs 기능 활성화 여부 | `true` |
| `snippets_enabled` | `boolean` | 스니펫 기능 활성화 여부 | `true` |
| `container_registry_enabled` | `boolean` | 컨테이너 레지스트리 활성화 여부 | `true` |
| `service_desk_enabled` | `boolean` | Service Desk 활성화 여부 | `true` |
| `service_desk_address` | `string` | Service Desk 이메일 주소 | `"contact+project-1-issue-@incoming.gitlab.com"` |
| `can_create_merge_request_in` | `boolean` | 현재 사용자가 MR 생성 가능 여부 | `true` |
| `issues_access_level` | `string` | 이슈 접근 레벨 | `"enabled"` |
| `repository_access_level` | `string` | 저장소 접근 레벨 | `"enabled"` |
| `merge_requests_access_level` | `string` | MR 접근 레벨 | `"enabled"` |
| `forking_access_level` | `string` | 포크 접근 레벨 | `"enabled"` |
| `wiki_access_level` | `string` | Wiki 접근 레벨 | `"enabled"` |
| `builds_access_level` | `string` | CI/CD 빌드 접근 레벨 | `"enabled"` |
| `snippets_access_level` | `string` | 스니펫 접근 레벨 | `"enabled"` |
| `pages_access_level` | `string` | GitLab Pages 접근 레벨 | `"enabled"` |
| `analytics_access_level` | `string` | 분석 접근 레벨 | `"enabled"` |
| `container_registry_access_level` | `string` | 컨테이너 레지스트리 접근 레벨 | `"enabled"` |
| `security_and_compliance_access_level` | `string` | 보안 및 규정 준수 접근 레벨 | `"enabled"` |
| `releases_access_level` | `string` | 릴리스 접근 레벨 | `"enabled"` |
| `environments_access_level` | `string` | 환경(environments) 접근 레벨 | `"enabled"` |
| `feature_flags_access_level` | `string` | 기능 플래그 접근 레벨 | `"enabled"` |
| `infrastructure_access_level` | `string` | 인프라 접근 레벨 | `"enabled"` |
| `monitor_access_level` | `string` | 모니터 접근 레벨 | `"enabled"` |
| `model_experiments_access_level` | `string` | 모델 실험 접근 레벨 | `"enabled"` |
| `model_registry_access_level` | `string` | 모델 레지스트리 접근 레벨 | `"enabled"` |
| `package_registry_access_level` | `string` | 패키지 레지스트리 접근 레벨 | `"enabled"` |
| `emails_disabled` | `boolean` | 이메일 알림 비활성화 여부 | `false` |
| `emails_enabled` | `boolean` | 이메일 알림 활성화 여부 | `true` |
| `show_diff_preview_in_email` | `boolean` | 이메일에 diff 미리보기 표시 여부 | `true` |
| `shared_runners_enabled` | `boolean` | 공유 러너 활성화 여부 | `true` |
| `lfs_enabled` | `boolean` | LFS 활성화 여부 | `true` |
| `creator_id` | `integer` | 프로젝트 생성자 ID | `1` |
| `mr_default_target_self` | `boolean` | MR 기본 대상이 자체 프로젝트인지 여부 | `false` |
| `import_url` | `string` | 가져오기(import) 소스 URL | `"https://github.com/johndoe/example.git"` |
| `import_type` | `string` | 가져오기 유형 | `"github"` |
| `import_status` | `string` | 가져오기 상태 | `"finished"` |
| `import_error` | `string` | 가져오기 오류 메시지 | `null` |
| `open_issues_count` | `integer` | 열린 이슈 수 | `5` |
| `description_html` | `string` | HTML로 렌더링된 설명 | `"<p>My example project</p>"` |
| `updated_at` | `string` | 마지막 업데이트 일시 (ISO 8601) | `"2024-06-15T12:00:00.000Z"` |
| `ci_default_git_depth` | `integer` | CI 기본 git depth | `50` |
| `ci_delete_pipelines_in_seconds` | `integer` | CI 파이프라인 자동 삭제 주기 (초) | `604800` |
| `ci_forward_deployment_enabled` | `boolean` | CI 순방향 배포 활성화 여부 | `true` |
| `ci_forward_deployment_rollback_allowed` | `boolean` | CI 순방향 배포 롤백 허용 여부 | `false` |
| `ci_job_token_scope_enabled` | `boolean` | CI Job Token Scope 활성화 여부 | `true` |
| `ci_separated_caches` | `boolean` | CI 캐시 분리 여부 | `true` |
| `ci_allow_fork_pipelines_to_run_in_parent_project` | `boolean` | 포크 파이프라인이 부모 프로젝트에서 실행 허용 여부 | `false` |
| `ci_id_token_sub_claim_components` | `array[string]` | CI ID Token sub claim 구성 요소 | `["project_path","ref_type","ref"]` |
| `build_git_strategy` | `string` | 빌드 git 전략 | `"fetch"` |
| `keep_latest_artifact` | `boolean` | 최신 아티팩트 보관 여부 | `true` |
| `restrict_user_defined_variables` | `boolean` | 사용자 정의 변수 제한 여부 | `false` |
| `ci_pipeline_variables_minimum_override_role` | `string` | CI 파이프라인 변수 재정의 최소 역할 | `"developer"` |
| `runner_token_expiration_interval` | `integer` | 러너 토큰 만료 간격 (초) | `86400` |
| `group_runners_enabled` | `boolean` | 그룹 러너 활성화 여부 | `true` |
| `resource_group_default_process_mode` | `string` | 리소스 그룹 기본 처리 모드 | `"oldest_first"` |
| `auto_cancel_pending_pipelines` | `string` | 보류 중인 파이프라인 자동 취소 설정 | `"enabled"` |
| `build_timeout` | `integer` | 빌드 타임아웃 (초) | `3600` |
| `auto_devops_enabled` | `boolean` | Auto DevOps 활성화 여부 | `true` |
| `auto_devops_deploy_strategy` | `string` | Auto DevOps 배포 전략 | `"continuous"` |
| `ci_push_repository_for_job_token_allowed` | `boolean` | Job Token으로 저장소 푸시 허용 여부 | `false` |
| `protect_merge_request_pipelines` | `boolean` | MR 파이프라인 보호 여부 | `false` |
| `ci_display_pipeline_variables` | `boolean` | CI 파이프라인 변수 표시 여부 | `false` |
| `runners_token` | `string` | 러너 등록 토큰 | `"REGISTRATION_TOKEN"` |
| `ci_config_path` | `string` | CI 설정 파일 경로 | `".gitlab-ci.yml"` |
| `public_jobs` | `boolean` | 공개 Job 표시 여부 | `true` |
| `shared_with_groups` | `array[object]` | 공유된 그룹 목록 | `[]` |
| `only_allow_merge_if_pipeline_succeeds` | `boolean` | 파이프라인 성공 시에만 MR 병합 허용 | `true` |
| `allow_merge_on_skipped_pipeline` | `boolean` | 건너뛴 파이프라인에서도 MR 병합 허용 | `false` |
| `request_access_enabled` | `boolean` | 액세스 요청 기능 활성화 여부 | `true` |
| `only_allow_merge_if_all_discussions_are_resolved` | `boolean` | 모든 토론 해결 시에만 MR 병합 허용 | `false` |
| `remove_source_branch_after_merge` | `boolean` | MR 병합 후 소스 브랜치 자동 삭제 | `true` |
| `printing_merge_request_link_enabled` | `boolean` | MR 링크 출력 활성화 여부 | `true` |
| `merge_method` | `string` | MR 병합 방식 | `"merge_commit"` |
| `squash_option` | `string` | Squash 옵션 | `"default_on"` |
| `enforce_auth_checks_on_uploads` | `boolean` | 업로드 인증 검사 강제 여부 | `true` |
| `suggestion_commit_message` | `string` | 제안 커밋 메시지 템플릿 | `"Apply suggestion"` |
| `merge_commit_template` | `string` | MR 병합 커밋 템플릿 | `"Merge branch 'feature' into 'main'"` |
| `squash_commit_template` | `string` | Squash 커밋 템플릿 | `"Squashed commit"` |
| `mr_default_title_template` | `string` | MR 기본 제목 템플릿 | `"Draft: %{title}"` |
| `issue_branch_template` | `string` | 이슈 브랜치 템플릿 | `"issue-%{id}"` |
| `statistics` | `object` | 프로젝트 통계 (요청 시 포함) | `{"commit_count":120,"storage_size":50000000,"repository_size":30000000,"wiki_size":1000000,"lfs_objects_size":5000000,"job_artifacts_size":10000000,"pipeline_artifacts_size":2000000,"packages_size":1000000,"snippets_size":500000,"uploads_size":500000,"container_registry_size":0}` |
| `warn_about_potentially_unwanted_characters` | `boolean` | 잠재적 원하지 않는 문자 경고 여부 | `true` |
| `autoclose_referenced_issues` | `boolean` | 참조된 이슈 자동 닫기 여부 | `true` |
| `max_artifacts_size` | `integer` | 최대 아티팩트 크기 (MB) | `100` |
| `approvals_before_merge` | `string` | MR 병합 전 필요한 승인 수 | `"1"` |
| `mirror` | `string` | 미러 설정 | `"disabled"` |
| `mirror_user_id` | `string` | 미러 사용자 ID | `null` |
| `mirror_trigger_builds` | `string` | 미러 트리거 빌드 여부 | `"disabled"` |
| `only_mirror_protected_branches` | `string` | 보호된 브랜치만 미러 여부 | `"disabled"` |
| `mirror_overwrites_diverged_branches` | `string` | 분기된 브랜치 미러 덮어쓰기 여부 | `"disabled"` |
| `external_authorization_classification_label` | `string` | 외부 인증 분류 레이블 | `""` |
| `requirements_enabled` | `string` | 요구사항(requirements) 기능 활성화 여부 | `"enabled"` |
| `requirements_access_level` | `string` | 요구사항 접근 레벨 | `"enabled"` |
| `security_and_compliance_enabled` | `string` | 보안 및 규정 준수 탭 활성화 여부 | `"enabled"` |
| `secret_push_protection_enabled` | `boolean` | 시크릿 푸시 보호 활성화 여부 | `false` |
| `pre_receive_secret_detection_enabled` | `boolean` | Pre-receive 시크릿 탐지 활성화 여부 | `false` |
| `compliance_frameworks` | `string` | 규정 준수 프레임워크 | `"gdpr"` |
| `issues_template` | `string` | 이슈 템플릿 내용 | `"## Description\n\n..."` |
| `merge_requests_template` | `string` | MR 템플릿 내용 | `"## Summary\n\n..."` |
| `ci_restrict_pipeline_cancellation_role` | `string` | 파이프라인 취소 제한 역할 | `"developer"` |
| `merge_pipelines_enabled` | `string` | 병합 파이프라인 활성화 여부 | `"disabled"` |
| `merge_trains_enabled` | `string` | 병합 트레인 활성화 여부 | `"disabled"` |
| `merge_trains_skip_train_allowed` | `string` | 병합 트레인 건너뛰기 허용 여부 | `"disabled"` |
| `merge_train_enforcement` | `string` | 병합 트레인 강제 여부 | `"disabled"` |
| `max_pipelines_per_merge_train` | `string` | 병합 트레인당 최대 파이프라인 수 | `"5"` |
| `only_allow_merge_if_all_status_checks_passed` | `string` | 모든 상태 체크 통과 시에만 MR 병합 허용 | `"disabled"` |
| `allow_pipeline_trigger_approve_deployment` | `boolean` | 파이프라인 트리거 배포 승인 허용 여부 | `false` |
| `prevent_merge_without_jira_issue` | `string` | Jira 이슈 없이 MR 병합 금지 여부 | `"disabled"` |
| `auto_duo_code_review_enabled` | `string` | Duo Code Review 자동 활성화 여부 | `"disabled"` |
| `reviewer_assignment_strategy` | `string` | 리뷰어 할당 전략 | `"random"` |
| `duo_remote_flows_enabled` | `string` | Duo Remote Flows 활성화 여부 | `"disabled"` |
| `duo_foundational_flows_enabled` | `string` | Duo Foundational Flows 활성화 여부 | `"disabled"` |
| `duo_sast_fp_detection_enabled` | `string` | Duo SAST 오탐지 탐지 활성화 여부 | `"disabled"` |
| `duo_secret_detection_fp_enabled` | `string` | Duo Secret Detection 오탐지 탐지 활성화 여부 | `"disabled"` |
| `duo_dependency_bump_breaking_changes_enabled` | `string` | Duo Dependency Bump Breaking Changes 활성화 여부 | `"disabled"` |
| `duo_sast_vr_workflow_enabled` | `string` | Duo SAST VR Workflow 활성화 여부 | `"disabled"` |
| `web_based_commit_signing_enabled` | `string` | 웹 기반 커밋 서명 활성화 여부 | `"disabled"` |
| `spp_repository_pipeline_access` | `boolean` | 보안 정책 파이프라인의 저장소 접근 허용 여부 (보안 오케스트레이션 정책 기능 필요) | `true` |
| `security_policy_pipeline_must_succeed` | `boolean` | MR 병합 전 모든 보안 정책 파이프라인 성공 필요 여부 | `true` |
| `merge_request_title_regex` | `string` | MR 제목 정규식 검증 | `""` |
| `merge_request_title_regex_description` | `string` | MR 제목 정규식 설명 | `""` |
| `permissions` | `object` | 권한 정보 | `{}` |

### `401 Unauthorized`

토큰이 없거나 유효하지 않은 경우 발생한다. 단, 공개 프로젝트는 인증 없이 접근 가능하다.

### `403 Forbidden`

토큰은 유효하지만 필요한 권한이 없는 경우 발생한다.

### `404 Not Found`

지정한 프로젝트 ID 또는 경로에 해당하는 프로젝트가 없는 경우 발생한다.

---

## 3. List all members of a project

## 기본 정보

- **기능:** 특정 프로젝트에 접근 권한이 있는 모든 멤버 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/users`
- **인증:** Bearer Token 필요 (GitLab REST API는 모두 OAuth2/PAT 필요함. 읽기 전용은 `read_api` scope, 쓰기는 `api` scope 필요)
- **권한:** `read_api` (읽기 전용) / `api` (읽기+쓰기)
- **멱등성:** GET은 멱등, POST/PUT은 미지원

## 설명

특정 프로젝트에 접근 권한이 있는 모든 멤버(사용자)의 목록을 반환한다. 검색어(`search`)로 특정 사용자를 찾을 수 있으며, `skip_users`로 특정 ID의 사용자를 제외할 수 있다. 페이징(`page`, `per_page`)을 지원한다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1` 또는 `john-doe%2Fexample-project` |

### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---|---|
| `search` | `string` | N | 검색어와 일치하는 사용자 반환 | `john` |
| `skip_users` | `array` | N | 지정된 ID의 사용자를 결과에서 제외 | `[2, 5]` |
| `page` | `integer` | N | 현재 페이지 번호 | `1` |
| `per_page` | `integer` | N | 페이지당 항목 수 | `20` |

### Body

없음 (GET 요청)

## Response

### `200 OK`

응답은 사용자 객체의 배열이다. 각 사용자 객체의 필드는 다음과 같다.

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | 사용자 고유 ID | `1` |
| `username` | `string` | 사용자명 | `"johndoe"` |
| `public_email` | `string` | 공개 이메일 주소 | `"john@example.com"` |
| `name` | `string` | 사용자 이름 | `"John Doe"` |
| `state` | `string` | 사용자 계정 상태 | `"active"` |
| `locked` | `boolean` | 계정 잠김 여부 | `false` |
| `avatar_url` | `string` | 아바타 이미지 URL | `"https://gitlab.example.com/uploads/-/system/user/avatar/1/avatar.png"` |
| `avatar_path` | `string` | 아바타 경로 | `""` |
| `custom_attributes` | `array[object]` | 커스텀 속성 목록 | `[{"key":"department","value":"engineering"}]` |
| `web_url` | `string` | 사용자 프로필 웹 URL | `"https://gitlab.example.com/johndoe"` |

### `401 Unauthorized`

토큰이 없거나 유효하지 않은 경우 발생한다.

### `403 Forbidden`

토큰은 유효하지만 필요한 권한이 없는 경우 발생한다.

### `404 Not Found`

지정한 프로젝트 ID 또는 경로에 해당하는 프로젝트가 없는 경우 발생한다.

---

## Errors

다음 표는 모든 엔드포인트에 공통으로 적용되는 오류 응답이다.

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `400` | `INVALID_ARGUMENT` | 입력값 형식 또는 범위 오류 | 응답 확인 후 수정 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 후 재시도 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 대상 리소스 없음 | ID 확인 |
| `500` | `INTERNAL_ERROR` | 서버 오류 | 재시도 후 지원팀 문의 |
