# 67-groups API Specification

> GitLab REST API - Groups 카테고리의 엔드포인트 명세

---

## 1. List all groups

## 기본 정보

- **기능:** 인증된 사용자에게 보이는 모든 그룹 목록을 조회한다. 인증되지 않은 요청은 공개 그룹만 반환한다.
- **Endpoint:** `GET /api/v4/groups`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (읽기 전용)
- **멱등성:** GET은 멱등

## 설명

인증된 사용자가 접근 가능한 모든 그룹을 목록으로 반환한다. 인증 없이 요청하면 공개 그룹만 조회된다. 다양한 필터(검색어, 공개 범위, 보관 여부 등)와 페이지네이션을 지원한다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

없음

### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `statistics` | `boolean` | N | 프로젝트 통계 포함 여부 |
| `archived` | `boolean` | N | 보관 상태로 필터링 |
| `skip_groups` | `array` | N | 목록에서 제외할 그룹 ID 배열 |
| `all_available` | `boolean` | N | `true`면 접근 가능한 모든 그룹 반환, `false`면 사용자가 멤버인 그룹만 반환 |
| `visibility` | `string` | N | 공개 범위로 필터링 |
| `search` | `string` | N | 그룹 검색어 |
| `owned` | `boolean` | N | 인증된 사용자가 소유한 그룹만 필터링 |
| `order_by` | `string` | N | 정렬 기준 (`name`, `path`, `id`, 검색 시 `similarity`) |
| `sort` | `string` | N | 정렬 방향 (`asc`, `desc`) |
| `min_access_level` | `integer` | N | 인증된 사용자의 최소 접근 수준 |
| `top_level_only` | `boolean` | N | 최상위 그룹만 포함 |
| `marked_for_deletion_on` | `string` | N | 특정 날짜에 삭제 예정인 그룹 반환 |
| `active` | `boolean` | N | 보관되지 않고 삭제 예정이 아닌 그룹만 필터링 |
| `repository_storage` | `string` | N | 그룹이 사용하는 저장소 스토리지 필터 |
| `page` | `integer` | N | 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |
| `with_custom_attributes` | `boolean` | N | 응답에 사용자 정의 속성 포함 |
| `custom_attributes` | `object` | N | 사용자 정의 속성으로 필터링 |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | 그룹 ID | `1` |
| `web_url` | `string` | 그룹 웹 URL | `https://gitlab.com/groups/my-group` |
| `name` | `string` | 그룹 이름 | `My Group` |
| `path` | `string` | 그룹 경로 | `my-group` |
| `description` | `string` | 그룹 설명 | `My group description` |
| `visibility` | `string` | 공개 범위 | `public` |
| `share_with_group_lock` | `boolean` | 그룹 공유 잠금 여부 | `false` |
| `require_two_factor_authentication` | `boolean` | 2FA 요구 여부 | `false` |
| `two_factor_grace_period` | `integer` | 2FA 유예 기간(일) | `48` |
| `project_creation_level` | `string` | 프로젝트 생성 권한 수준 | `developer` |
| `auto_devops_enabled` | `string` | Auto DevOps 활성화 여부 | `enabled` |
| `subgroup_creation_level` | `string` | 하위 그룹 생성 권한 수준 | `owner` |
| `emails_disabled` | `boolean` | 이메일 비활성화 여부 | `false` |
| `emails_enabled` | `boolean` | 이메일 활성화 여부 | `true` |
| `show_diff_preview_in_email` | `boolean` | 이메일 diff 미리보기 표시 여부 | `true` |
| `mentions_disabled` | `string` | 멘션 비활성화 여부 | `false` |
| `lfs_enabled` | `boolean` | LFS 활성화 여부 | `true` |
| `archived` | `boolean` | 보관 여부 | `false` |
| `math_rendering_limits_enabled` | `boolean` | 수학 렌더링 제한 활성화 여부 | `true` |
| `lock_math_rendering_limits_enabled` | `boolean` | 수학 렌더링 제한 잠금 여부 | `false` |
| `crm_enabled` | `boolean` | CRM 활성화 여부 | `false` |
| `resource_access_token_notify_inherited` | `boolean` | 리소스 액세스 토큰 알림 상속 여부 | `false` |
| `lock_resource_access_token_notify_inherited` | `boolean` | 리소스 액세스 토큰 알림 상속 잠금 여부 | `false` |
| `default_branch` | `string` | 기본 브랜치명 | `main` |
| `default_branch_protection` | `integer` | 기본 브랜치 보호 수준 | `2` |
| `default_branch_protection_defaults` | `string` | 기본 브랜치 보호 기본값 | `{}` |
| `avatar_url` | `string` | 아바타 URL | `https://gitlab.com/uploads/avatar.png` |
| `request_access_enabled` | `boolean` | 액세스 요청 허용 여부 | `true` |
| `full_name` | `string` | 전체 그룹 이름 | `My Group` |
| `full_path` | `string` | 전체 그룹 경로 | `my-group` |
| `created_at` | `string` | 생성 일시 | `2020-01-01T00:00:00.000Z` |
| `parent_id` | `string` | 상위 그룹 ID (없으면 null) | `null` |
| `organization_id` | `integer` | 조직 ID | `1` |
| `shared_runners_setting` | `string` | 공유 러너 설정 | `enabled` |
| `max_artifacts_size` | `integer` | 최대 아티팩트 크기(MB) | `100` |
| `custom_attributes` | `object` | 사용자 정의 속성 | `{"key": "value"}` |
| `statistics` | `string` | 그룹 통계 | - |
| `marked_for_deletion_on` | `string` | 삭제 예정일 | `null` |
| `root_storage_statistics` | `object` | 루트 스토리지 통계 (하위 객체 참조) | - |
| `ldap_cn` | `string` | LDAP CN | `null` |
| `ldap_access` | `string` | LDAP 액세스 수준 | `null` |
| `ldap_group_links` | `object` | LDAP 그룹 링크 | - |
| `saml_group_links` | `object` | SAML 그룹 링크 | - |
| `file_template_project_id` | `string` | 파일 템플릿 프로젝트 ID | `null` |
| `wiki_access_level` | `string` | Wiki 액세스 수준 | `enabled` |
| `repository_storage` | `string` | 저장소 스토리지 | `default` |
| `duo_core_features_enabled` | `boolean` | GitLab Duo Core 기능 활성화 여부 (실험적) | `true` |
| `duo_features_enabled` | `string` | Duo 기능 활성화 여부 | `true` |
| `lock_duo_features_enabled` | `string` | Duo 기능 잠금 여부 | `false` |
| `auto_duo_code_review_enabled` | `string` | 자동 Duo 코드 리뷰 활성화 여부 | `false` |
| `web_based_commit_signing_enabled` | `string` | 웹 기반 커밋 서명 활성화 여부 | `false` |
| `allow_personal_snippets` | `string` | 개인 스니펫 허용 여부 | `true` |
| `duo_namespace_access_rules` | `string` | Duo 네임스페이스 액세스 규칙 | `{}` |
| `built_in_project_templates_enabled` | `boolean` | 내장 프로젝트 템플릿 활성화 여부 | `true` |
| `lock_built_in_project_templates_enabled` | `boolean` | 내장 프로젝트 템플릿 잠금 여부 | `false` |

`root_storage_statistics` 하위 객체:

| 필드 | 타입 | 설명 |
|---|---:|---|
| `build_artifacts_size` | `integer` | CI 아티팩트 크기 (bytes) |
| `container_registry_size` | `integer` | 컨테이너 레지스트리 크기 (bytes) |
| `container_registry_size_is_estimated` | `boolean` | 중복 제거된 크기가 추정치인지 여부 |
| `dependency_proxy_size` | `integer` | Dependency Proxy 크기 (bytes) |
| `lfs_objects_size` | `integer` | LFS 객체 크기 (bytes) |
| `packages_size` | `integer` | 패키지 크기 (bytes) |
| `pipeline_artifacts_size` | `integer` | CI 파이프라인 아티팩트 크기 (bytes) |
| `repository_size` | `integer` | Git 저장소 크기 (bytes) |
| `snippets_size` | `integer` | 스니펫 크기 (bytes) |
| `storage_size` | `integer` | 전체 스토리지 크기 (bytes) |
| `uploads_size` | `integer` | 업로드 크기 (bytes) |
| `wiki_size` | `integer` | Wiki 크기 (bytes) |

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `400` | `INVALID_ARGUMENT` | 입력값 형식 또는 범위 오류 | 응답 확인 후 수정 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 후 재시도 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 대상 리소스 없음 | ID 확인 |
| `500` | `INTERNAL_ERROR` | 서버 오류 | 재시도 후 지원팀 문의 |

---

## 2. Retrieve a group

## 기본 정보

- **기능:** ID 또는 path로 특정 그룹의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (읽기 전용)
- **멱등성:** GET은 멱등

## 설명

그룹 ID나 path를 지정하여 단일 그룹의 상세 정보를 반환한다. List all groups보다 더 많은 필드(소속 프로젝트, 공유 프로젝트, AI 설정, IP 제한, runners 토큰 등)를 포함한다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 조회할 그룹의 ID 또는 path |

### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `with_custom_attributes` | `boolean` | N | 응답에 사용자 정의 속성 포함 |
| `custom_attributes` | `object` | N | 사용자 정의 속성으로 필터링 |
| `with_projects` | `boolean` | N | `false`로 설정하면 프로젝트 세부 정보 생략 |

## Response

### `200 OK`

List all groups의 모든 필드를 포함하며, 다음 필드가 추가된다:

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `shared_with_groups` | `array` | 그룹과 공유된 그룹 목록 | `[]` |
| `runners_token` | `string` | 그룹 러너 등록 토큰 | `token` |
| `enabled_git_access_protocol` | `string` | 활성화된 Git 액세스 프로토콜 | `ssh` |
| `prevent_sharing_groups_outside_hierarchy` | `boolean` | 계층 외부 그룹 공유 방지 여부 | `false` |
| `step_up_auth_required_oauth_provider` | `string` | 단계 인증에 필요한 OAuth 제공자 | `null` |
| `projects` | `object` | 그룹에 속한 프로젝트 객체 | - |
| `shared_projects` | `object` | 그룹과 공유된 프로젝트 객체 | - |
| `shared_runners_minutes_limit` | `string` | 공유 러너 분 제한 | `null` |
| `extra_shared_runners_minutes_limit` | `string` | 추가 공유 러너 분 제한 | `null` |
| `prevent_forking_outside_group` | `string` | 그룹 외부 포크 방지 여부 | `false` |
| `service_access_tokens_expiration_enforced` | `string` | 서비스 액세스 토큰 만료 강제 여부 | `false` |
| `experiment_features_enabled` | `string` | 실험 기능 활성화 여부 | `false` |
| `ai_settings` | `object` | AI 설정 (Duo Agent 등) | - |
| `membership_lock` | `string` | 멤버십 잠금 여부 | `false` |
| `ip_restriction_ranges` | `string` | IP 제한 범위 | `null` |
| `allowed_email_domains_list` | `string` | 허용된 이메일 도메인 목록 | `null` |
| `only_allow_merge_if_pipeline_succeeds` | `string` | 파이프라인 성공 시에만 병합 허용 | `false` |
| `allow_merge_on_skipped_pipeline` | `string` | 건너뛴 파이프라인에서 병합 허용 | `false` |
| `only_allow_merge_if_all_discussions_are_resolved` | `string` | 모든 토론 해결 시에만 병합 허용 | `false` |
| `unique_project_download_limit` | `string` | 고유 프로젝트 다운로드 제한 | `null` |
| `unique_project_download_limit_interval_in_seconds` | `string` | 고유 프로젝트 다운로드 제한 간격(초) | `null` |
| `unique_project_download_limit_allowlist` | `string` | 고유 프로젝트 다운로드 제한 허용 목록 | `null` |
| `unique_project_download_limit_alertlist` | `string` | 고유 프로젝트 다운로드 제한 알림 목록 | `null` |
| `auto_ban_user_on_excessive_projects_download` | `string` | 과도한 프로젝트 다운로드 시 자동 차단 여부 | `false` |

`ai_settings` 하위 객체:

| 필드 | 타입 | 설명 |
|---|---:|---|
| `duo_agent_platform_enabled` | `boolean` | Duo Agent 플랫폼 활성화 여부 |
| `duo_workflow_mcp_enabled` | `boolean` | Duo Workflow MCP 활성화 여부 |
| `foundational_agents_default_enabled` | `boolean` | 기본 Agent 기본 활성화 여부 |
| `ai_catalog_restricted_to_group_hierarchy` | `boolean` | AI 카탈로그를 그룹 계층으로 제한 여부 |
| `ai_usage_data_collection_enabled` | `boolean` | AI 사용 데이터 수집 활성화 여부 |
| `prompt_injection_protection_level` | `string` | 프롬프트 인젝션 보호 수준 |
| `include_recommended_allowed` | `boolean` | 추천 포함 허용 여부 |
| `allow_all_unix_sockets` | `boolean` | 모든 Unix 소켓 허용 여부 |
| `allow_project_extension` | `boolean` | 프로젝트 확장 허용 여부 |
| `minimum_access_level_execute` | `string` | 실행 최소 액세스 수준 |
| `minimum_access_level_execute_async` | `string` | 비동기 실행 최소 액세스 수준 |
| `minimum_access_level_manage` | `string` | 관리 최소 액세스 수준 |
| `minimum_access_level_enable_on_projects` | `string` | 프로젝트 활성화 최소 액세스 수준 |

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `400` | `INVALID_ARGUMENT` | 입력값 형식 또는 범위 오류 | 응답 확인 후 수정 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 후 재시도 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 대상 리소스 없음 | ID 확인 |
| `500` | `INTERNAL_ERROR` | 서버 오류 | 재시도 후 지원팀 문의 |

---

## 3. List all projects in a group

## 기본 정보

- **기능:** 특정 그룹에 속한 모든 프로젝트 목록을 조회한다. 인증되지 않은 요청은 공개 프로젝트만 제한된 속성으로 반환한다.
- **Endpoint:** `GET /api/v4/groups/{id}/projects`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (읽기 전용)
- **멱등성:** GET은 멱등

## 설명

지정된 그룹의 모든 프로젝트를 인증된 사용자의 접근 권한에 따라 반환한다. 서브그룹 포함, 공유 프로젝트 포함, 보안 리포트 필터 등 다양한 조건으로 프로젝트 목록을 필터링할 수 있다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 그룹 ID |

### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `active` | `boolean` | N | 보관되지 않고 삭제 예정이 아닌 프로젝트만 필터링 |
| `archived` | `boolean` | N | 보관 상태로 필터링 |
| `visibility` | `string` | N | 공개 범위로 필터링 |
| `search` | `string` | N | 검색어와 일치하는 프로젝트 반환 |
| `order_by` | `string` | N | 정렬 기준 필드 |
| `sort` | `string` | N | 정렬 방향 (`asc`, `desc`) |
| `simple` | `boolean` | N | ID, URL, name, path만 반환 |
| `owned` | `boolean` | N | 인증된 사용자가 소유한 프로젝트만 필터링 |
| `starred` | `boolean` | N | 즐겨찾기 상태로 필터링 |
| `with_issues_enabled` | `boolean` | N | Issues 기능 활성화된 프로젝트만 필터링 |
| `with_merge_requests_enabled` | `boolean` | N | Merge Requests 기능 활성화된 프로젝트만 필터링 |
| `with_shared` | `boolean` | N | 이 그룹에 공유된 프로젝트 포함 |
| `include_subgroups` | `boolean` | N | 하위 그룹의 프로젝트 포함 |
| `include_ancestor_groups` | `boolean` | N | 상위 그룹의 프로젝트 포함 |
| `min_access_level` | `integer` | N | 인증된 사용자의 최소 접근 수준 |
| `page` | `integer` | N | 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |
| `with_custom_attributes` | `boolean` | N | 응답에 사용자 정의 속성 포함 |
| `custom_attributes` | `object` | N | 사용자 정의 속성으로 필터링 |
| `with_security_reports` | `boolean` | N | 보안 리포트 아티팩트가 있는 프로젝트만 반환 |

## Response

### `200 OK`

각 프로젝트 객체의 주요 필드:

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | 프로젝트 ID | `1` |
| `description` | `string` | 프로젝트 설명 | `My project` |
| `name` | `string` | 프로젝트 이름 | `My Project` |
| `name_with_namespace` | `string` | 네임스페이스를 포함한 이름 | `My Group / My Project` |
| `path` | `string` | 프로젝트 경로 | `my-project` |
| `path_with_namespace` | `string` | 네임스페이스를 포함한 경로 | `my-group/my-project` |
| `created_at` | `string` | 생성 일시 | `2020-01-01T00:00:00.000Z` |
| `default_branch` | `string` | 기본 브랜치명 | `main` |
| `tag_list` | `array` | 태그 목록 | `[]` |
| `topics` | `array` | 토픽 목록 | `["frontend"]` |
| `ssh_url_to_repo` | `string` | SSH 저장소 URL | `git@gitlab.com:group/project.git` |
| `http_url_to_repo` | `string` | HTTP 저장소 URL | `https://gitlab.com/group/project.git` |
| `web_url` | `string` | 프로젝트 웹 URL | `https://gitlab.com/group/project` |
| `readme_url` | `string` | README URL | `https://gitlab.com/group/project/-/blob/main/README.md` |
| `forks_count` | `integer` | 포크 수 | `0` |
| `license_url` | `string` | 라이선스 URL | `null` |
| `license` | `object` | 라이선스 정보 | - |
| `avatar_url` | `string` | 아바타 URL | `null` |
| `star_count` | `integer` | 별표 수 | `0` |
| `last_activity_at` | `string` | 마지막 활동 일시 | `2020-01-01T00:00:00.000Z` |
| `visibility` | `string` | 공개 범위 | `public` |
| `namespace` | `object` | 네임스페이스 정보 | - |
| `custom_attributes` | `object` | 사용자 정의 속성 | `{}` |
| `repository_storage` | `string` | 저장소 스토리지 | `default` |
| `forked_from_project` | `object` | 포크 원본 프로젝트 정보 | `null` |
| `container_registry_image_prefix` | `string` | 컨테이너 레지스트리 이미지 접두사 | `registry.gitlab.com/group/project` |
| `_links` | `object` | 관련 링크 | `{}` |
| `marked_for_deletion_at` | `string` | 삭제 예정일 | `null` |
| `marked_for_deletion_on` | `string` | 삭제 예정일 | `null` |
| `packages_enabled` | `boolean` | 패키지 활성화 여부 | `true` |
| `empty_repo` | `boolean` | 빈 저장소 여부 | `false` |
| `archived` | `boolean` | 보관 여부 | `false` |
| `owner` | `object` | 소유자 정보 | - |
| `resolve_outdated_diff_discussions` | `boolean` | 오래된 diff 토론 해결 여부 | `false` |
| `container_expiration_policy` | `object` | 컨테이너 만료 정책 | - |
| `repository_object_format` | `string` | 저장소 객체 형식 | `sha256` |
| `issues_enabled` | `boolean` | Issues 활성화 여부 | `true` |
| `merge_requests_enabled` | `boolean` | Merge Requests 활성화 여부 | `true` |
| `wiki_enabled` | `boolean` | Wiki 활성화 여부 | `true` |
| `jobs_enabled` | `boolean` | Jobs 활성화 여부 | `true` |
| `snippets_enabled` | `boolean` | Snippets 활성화 여부 | `true` |
| `container_registry_enabled` | `boolean` | 컨테이너 레지스트리 활성화 여부 | `true` |
| `service_desk_enabled` | `boolean` | Service Desk 활성화 여부 | `false` |
| `service_desk_address` | `string` | Service Desk 주소 | `null` |
| `can_create_merge_request_in` | `boolean` | Merge Request 생성 가능 여부 | `true` |
| `issues_access_level` | `string` | Issues 액세스 수준 | `enabled` |
| `repository_access_level` | `string` | 저장소 액세스 수준 | `enabled` |
| `merge_requests_access_level` | `string` | Merge Requests 액세스 수준 | `enabled` |
| `forking_access_level` | `string` | 포크 액세스 수준 | `enabled` |
| `wiki_access_level` | `string` | Wiki 액세스 수준 | `enabled` |
| `builds_access_level` | `string` | CI/CD 액세스 수준 | `enabled` |
| `snippets_access_level` | `string` | Snippets 액세스 수준 | `enabled` |
| `pages_access_level` | `string` | Pages 액세스 수준 | `enabled` |
| `analytics_access_level` | `string` | Analytics 액세스 수준 | `enabled` |
| `container_registry_access_level` | `string` | 컨테이너 레지스트리 액세스 수준 | `enabled` |
| `security_and_compliance_access_level` | `string` | 보안 및 규정 준수 액세스 수준 | `enabled` |
| `releases_access_level` | `string` | Releases 액세스 수준 | `enabled` |
| `environments_access_level` | `string` | Environments 액세스 수준 | `enabled` |
| `feature_flags_access_level` | `string` | Feature Flags 액세스 수준 | `enabled` |
| `infrastructure_access_level` | `string` | Infrastructure 액세스 수준 | `enabled` |
| `monitor_access_level` | `string` | Monitor 액세스 수준 | `enabled` |
| `model_experiments_access_level` | `string` | Model Experiments 액세스 수준 | `enabled` |
| `model_registry_access_level` | `string` | Model Registry 액세스 수준 | `enabled` |
| `package_registry_access_level` | `string` | Package Registry 액세스 수준 | `enabled` |
| `emails_disabled` | `boolean` | 이메일 비활성화 여부 | `false` |
| `emails_enabled` | `boolean` | 이메일 활성화 여부 | `true` |
| `show_diff_preview_in_email` | `boolean` | 이메일 diff 미리보기 표시 여부 | `true` |
| `shared_runners_enabled` | `boolean` | 공유 러너 활성화 여부 | `true` |
| `lfs_enabled` | `boolean` | LFS 활성화 여부 | `true` |
| `creator_id` | `integer` | 생성자 ID | `1` |
| `mr_default_target_self` | `boolean` | MR 기본 대상 자체 여부 | `false` |
| `import_url` | `string` | 가져오기 URL | `null` |
| `import_type` | `string` | 가져오기 유형 | `null` |
| `import_status` | `string` | 가져오기 상태 | `none` |
| `import_error` | `string` | 가져오기 오류 | `null` |
| `open_issues_count` | `integer` | 열린 이슈 수 | `0` |
| `description_html` | `string` | 설명 HTML | `<p>desc</p>` |
| `updated_at` | `string` | 업데이트 일시 | `2020-01-01T00:00:00.000Z` |
| `ci_default_git_depth` | `integer` | CI 기본 git 깊이 | `50` |
| `ci_delete_pipelines_in_seconds` | `integer` | CI 파이프라인 삭제 시간(초) | `null` |
| `ci_forward_deployment_enabled` | `boolean` | CI 순방향 배포 활성화 여부 | `true` |
| `ci_forward_deployment_rollback_allowed` | `boolean` | CI 순방향 배포 롤백 허용 여부 | `false` |
| `ci_job_token_scope_enabled` | `boolean` | CI 작업 토큰 범위 활성화 여부 | `false` |
| `ci_separated_caches` | `boolean` | CI 분리 캐시 여부 | `true` |
| `ci_allow_fork_pipelines_to_run_in_parent_project` | `boolean` | 포크 파이프라인을 부모 프로젝트에서 실행 허용 여부 | `true` |
| `ci_id_token_sub_claim_components` | `array` | CI ID 토큰 sub 클레임 구성 요소 | `[]` |
| `build_git_strategy` | `string` | 빌드 git 전략 | `clone` |
| `keep_latest_artifact` | `boolean` | 최신 아티팩트 보관 여부 | `true` |
| `restrict_user_defined_variables` | `boolean` | 사용자 정의 변수 제한 여부 | `false` |
| `ci_pipeline_variables_minimum_override_role` | `string` | CI 파이프라인 변수 최소 재정의 역할 | `developer` |
| `runner_token_expiration_interval` | `integer` | 러너 토큰 만료 간격(초) | `null` |
| `group_runners_enabled` | `boolean` | 그룹 러너 활성화 여부 | `true` |
| `resource_group_default_process_mode` | `string` | 리소스 그룹 기본 처리 모드 | `unordered` |
| `auto_cancel_pending_pipelines` | `string` | 보류 중인 파이프라인 자동 취소 | `enabled` |
| `build_timeout` | `integer` | 빌드 타임아웃(초) | `3600` |
| `auto_devops_enabled` | `boolean` | Auto DevOps 활성화 여부 | `false` |
| `auto_devops_deploy_strategy` | `string` | Auto DevOps 배포 전략 | `continuous` |
| `ci_push_repository_for_job_token_allowed` | `boolean` | 작업 토큰으로 저장소 push 허용 여부 | `false` |
| `protect_merge_request_pipelines` | `boolean` | MR 파이프라인 보호 여부 | `false` |
| `ci_display_pipeline_variables` | `boolean` | CI 파이프라인 변수 표시 여부 | `false` |
| `runners_token` | `string` | 러너 토큰 | `token` |
| `ci_config_path` | `string` | CI 설정 파일 경로 | `.gitlab-ci.yml` |
| `public_jobs` | `boolean` | 공개 작업 여부 | `true` |
| `shared_with_groups` | `array` | 공유된 그룹 목록 | `[]` |
| `only_allow_merge_if_pipeline_succeeds` | `boolean` | 파이프라인 성공 시에만 병합 허용 | `false` |
| `allow_merge_on_skipped_pipeline` | `boolean` | 건너뛴 파이프라인에서 병합 허용 | `false` |
| `request_access_enabled` | `boolean` | 액세스 요청 허용 여부 | `true` |
| `only_allow_merge_if_all_discussions_are_resolved` | `boolean` | 모든 토론 해결 시에만 병합 허용 | `false` |
| `remove_source_branch_after_merge` | `boolean` | 병합 후 소스 브랜치 제거 여부 | `false` |
| `printing_merge_request_link_enabled` | `boolean` | MR 링크 출력 활성화 여부 | `true` |
| `merge_method` | `string` | 병합 방법 | `merge` |
| `squash_option` | `string` | 스쿼시 옵션 | `never` |
| `enforce_auth_checks_on_uploads` | `boolean` | 업로드 인증 검사 적용 여부 | `true` |
| `suggestion_commit_message` | `string` | 제안 커밋 메시지 | `null` |
| `merge_commit_template` | `string` | 병합 커밋 템플릿 | `null` |
| `squash_commit_template` | `string` | 스쿼시 커밋 템플릿 | `null` |
| `mr_default_title_template` | `string` | MR 기본 제목 템플릿 | `null` |
| `issue_branch_template` | `string` | 이슈 브랜치 템플릿 | `null` |
| `statistics` | `object` | 프로젝트 통계 | - |
| `warn_about_potentially_unwanted_characters` | `boolean` | 잠재적 원치 않는 문자 경고 여부 | `false` |
| `autoclose_referenced_issues` | `boolean` | 참조된 이슈 자동 닫기 여부 | `true` |
| `max_artifacts_size` | `integer` | 최대 아티팩트 크기(MB) | `100` |
| `approvals_before_merge` | `string` | 병합 전 승인 수 | `0` |
| `mirror` | `string` | 미러 설정 | `null` |
| `mirror_user_id` | `string` | 미러 사용자 ID | `null` |
| `mirror_trigger_builds` | `string` | 미러 트리거 빌드 | `null` |
| `only_mirror_protected_branches` | `string` | 보호된 브랜치만 미러 | `null` |
| `mirror_overwrites_diverged_branches` | `string` | 분기된 브랜치 미러 덮어쓰기 | `null` |
| `external_authorization_classification_label` | `string` | 외부 인증 분류 레이블 | `null` |
| `requirements_enabled` | `string` | Requirements 활성화 여부 | `false` |
| `requirements_access_level` | `string` | Requirements 액세스 수준 | `enabled` |
| `security_and_compliance_enabled` | `string` | 보안 및 규정 준수 활성화 여부 | `false` |
| `secret_push_protection_enabled` | `boolean` | 비밀 push 보호 활성화 여부 | `false` |
| `pre_receive_secret_detection_enabled` | `boolean` | 수신 전 비밀 탐지 활성화 여부 | `false` |
| `compliance_frameworks` | `string` | 규정 준수 프레임워크 | `[]` |
| `issues_template` | `string` | Issues 템플릿 | `null` |
| `merge_requests_template` | `string` | Merge Requests 템플릿 | `null` |
| `ci_restrict_pipeline_cancellation_role` | `string` | CI 파이프라인 취소 제한 역할 | `developer` |
| `merge_pipelines_enabled` | `string` | 병합 파이프라인 활성화 여부 | `false` |
| `merge_trains_enabled` | `string` | 병합 트레인 활성화 여부 | `false` |
| `merge_trains_skip_train_allowed` | `string` | 병합 트레인 건너뛰기 허용 여부 | `false` |
| `merge_train_enforcement` | `string` | 병합 트레인 강제 여부 | `false` |
| `max_pipelines_per_merge_train` | `string` | 병합 트레인당 최대 파이프라인 수 | `null` |
| `only_allow_merge_if_all_status_checks_passed` | `string` | 모든 상태 검사 통과 시에만 병합 허용 | `false` |
| `allow_pipeline_trigger_approve_deployment` | `boolean` | 파이프라인 트리거 배포 승인 허용 여부 | `false` |
| `prevent_merge_without_jira_issue` | `string` | Jira 이슈 없이 병합 방지 | `false` |
| `auto_duo_code_review_enabled` | `string` | 자동 Duo 코드 리뷰 활성화 여부 | `false` |
| `reviewer_assignment_strategy` | `string` | 리뷰어 할당 전략 | `null` |
| `duo_remote_flows_enabled` | `string` | Duo 원격 흐름 활성화 여부 | `false` |
| `duo_foundational_flows_enabled` | `string` | Duo 기본 흐름 활성화 여부 | `false` |
| `duo_sast_fp_detection_enabled` | `string` | Duo SAST 위양성 탐지 활성화 여부 | `false` |
| `duo_secret_detection_fp_enabled` | `string` | Duo 비밀 탐지 위양성 탐지 활성화 여부 | `false` |
| `duo_dependency_bump_breaking_changes_enabled` | `string` | Duo 의존성 충돌 변경 활성화 여부 | `false` |
| `duo_sast_vr_workflow_enabled` | `string` | Duo SAST VR 워크플로우 활성화 여부 | `false` |
| `web_based_commit_signing_enabled` | `string` | 웹 기반 커밋 서명 활성화 여부 | `false` |
| `spp_repository_pipeline_access` | `boolean` | 보안 정책 파이프라인 저장소 액세스 | `false` |
| `security_policy_pipeline_must_succeed` | `boolean` | 보안 정책 파이프라인 성공 필수 여부 | `false` |
| `merge_request_title_regex` | `string` | MR 제목 정규식 | `null` |
| `merge_request_title_regex_description` | `string` | MR 제목 정규식 설명 | `null` |

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `400` | `INVALID_ARGUMENT` | 입력값 형식 또는 범위 오류 | 응답 확인 후 수정 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 후 재시도 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 대상 리소스 없음 | ID 확인 |
| `500` | `INTERNAL_ERROR` | 서버 오류 | 재시도 후 지원팀 문의 |

---

## 4. List all subgroups

## 기본 정보

- **기능:** 특정 그룹의 모든 하위 그룹(subgroup) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/subgroups`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (읽기 전용)
- **멱등성:** GET은 멱등

## 설명

지정된 그룹의 직계 하위 그룹(subgroup) 목록을 반환한다. List all groups와 유사한 필터 파라미터(검색, 공개 범위, 보관 여부, 페이지네이션 등)를 지원한다.

## Request

### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

### Path parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 상위 그룹 ID |

### Query parameters

| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `statistics` | `boolean` | N | 프로젝트 통계 포함 여부 |
| `archived` | `boolean` | N | 보관 상태로 필터링 |
| `skip_groups` | `array` | N | 목록에서 제외할 그룹 ID 배열 |
| `all_available` | `boolean` | N | `true`면 접근 가능한 모든 그룹 반환, `false`면 사용자가 멤버인 그룹만 반환 |
| `visibility` | `string` | N | 공개 범위로 필터링 |
| `search` | `string` | N | 그룹 검색어 |
| `owned` | `boolean` | N | 인증된 사용자가 소유한 그룹만 필터링 |
| `order_by` | `string` | N | 정렬 기준 (`name`, `path`, `id`, 검색 시 `similarity`) |
| `sort` | `string` | N | 정렬 방향 (`asc`, `desc`) |
| `min_access_level` | `integer` | N | 인증된 사용자의 최소 접근 수준 |
| `top_level_only` | `boolean` | N | 최상위 그룹만 포함 |
| `marked_for_deletion_on` | `string` | N | 특정 날짜에 삭제 예정인 그룹 반환 |
| `active` | `boolean` | N | 보관되지 않고 삭제 예정이 아닌 그룹만 필터링 |
| `repository_storage` | `string` | N | 그룹이 사용하는 저장소 스토리지 필터 |
| `page` | `integer` | N | 페이지 번호 |
| `per_page` | `integer` | N | 페이지당 항목 수 |
| `with_custom_attributes` | `boolean` | N | 응답에 사용자 정의 속성 포함 |
| `custom_attributes` | `object` | N | 사용자 정의 속성으로 필터링 |

## Response

### `200 OK`

List all groups와 동일한 그룹 객체 스키마를 반환한다. (필드 목록은 List all groups의 Response 표 참조)

## Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `400` | `INVALID_ARGUMENT` | 입력값 형식 또는 범위 오류 | 응답 확인 후 수정 |
| `401` | `UNAUTHENTICATED` | 토큰 없음 또는 만료 | 토큰 갱신 후 재시도 |
| `403` | `FORBIDDEN` | 권한 없음 | 권한 요청 |
| `404` | `NOT_FOUND` | 대상 리소스 없음 | ID 확인 |
| `500` | `INTERNAL_ERROR` | 서버 오류 | 재시도 후 지원팀 문의 |
