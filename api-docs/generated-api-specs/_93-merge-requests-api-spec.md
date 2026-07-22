# 93 - Merge Requests API Spec

> GitLab REST API의 Merge Requests 관련 엔드포인트 모음입니다.
> 인증은 모든 엔드포인트에 대해 Bearer Token이 필요하며, `read_api` 권한이 필요합니다.

---

## 09. List all merge requests

### 기본 정보
- **기능:** 인증된 사용자가 접근 가능한 모든 Merge Request를 조회합니다. 기본적으로 현재 사용자가 생성한 MR만 반환하며, `scope=all`로 전체 조회가 가능합니다.
- **Endpoint:** `GET /api/v4/merge_requests`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
인증된 사용자가 접근 가능한 모든 Merge Request를 조회합니다. 기본값은 현재 사용자가 생성한 MR만 반환하며, `scope=all`을 사용하면 모든 MR을 조회할 수 있습니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Query parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `author_id` | `integer` | No | 특정 사용자 ID가 생성한 MR 조회. `author_username`과 상호 배타적 |
| `author_username` | `string` | No | 특정 사용자명이 생성한 MR 조회. `author_id`와 상호 배타적 |
| `assignee_id` | `any` | No | 특정 사용자 ID에 할당된 MR 조회. `None`=미할당, `Any`=할당 있음 |
| `assignee_username` | `array` | No | 특정 사용자명에 할당된 MR 조회 |
| `reviewer_username` | `string` | No | 특정 사용자명이 리뷰어인 MR 조회. `None`/`Any` 지원 |
| `labels` | `array` | No | 라벨 필터 (쉼표 구분). `None`/`Any` 지원 |
| `milestone` | `string` | No | 마일스톤 필터. `None`/`Any` 지원 |
| `my_reaction_emoji` | `string` | No | 인증된 사용자가 특정 이모지로 반응한 MR 조회 |
| `reviewer_id` | `any` | No | 특정 리뷰어 ID로 필터 |
| `state` | `string` | No | `all`, `opened`, `closed`, `locked`, `merged` |
| `order_by` | `string` | No | 정렬 기준: `created_at`, `updated_at`, `title` 등 |
| `sort` | `string` | No | `asc` 또는 `desc` |
| `scope` | `string` | No | `created_by_me`, `assigned_to_me`, `reviews_for_me`, `all` |
| `search` | `string` | No | 제목/설명 검색 |
| `source_branch` | `string` | No | 소스 브랜치 필터 |
| `target_branch` | `string` | No | 타겟 브랜치 필터 |
| `draft` | `boolean` | No | Draft 상태 필터 |
| `page` | `integer` | No | 페이지 번호 |
| `per_page` | `integer` | No | 페이지당 항목 수 |

### Response
#### `200 OK`
| 필드명 | 타입 | 설명 | 예시 |
| --- | --- | --- | --- |
| `id` | `integer` | MR 고유 ID | `1` |
| `iid` | `integer` | 프로젝트 내 MR ID | `1` |
| `project_id` | `integer` | 프로젝트 ID | `3` |
| `title` | `string` | MR 제목 | "Add new feature" |
| `description` | `string` | MR 설명 | "Implemented..." |
| `state` | `string` | 상태 (`opened`, `closed`, `merged`) | `opened` |
| `created_at` | `string` (ISO 8601) | 생성 시간 | `2024-01-01T00:00:00.000Z` |
| `updated_at` | `string` (ISO 8601) | 수정 시간 | `2024-01-02T00:00:00.000Z` |
| `merged_by` | `object` | 머지한 사용자 정보 | `{id, username, name, ...}` |
| `merge_user` | `object` | 머지 사용자 정보 | `{id, username, name, ...}` |
| `merged_at` | `string` | 머지 시간 | `2024-01-03T00:00:00.000Z` |
| `closed_by` | `object` | 닫은 사용자 정보 | `{id, username, name, ...}` |
| `closed_at` | `string` | 닫힌 시간 | `2024-01-03T00:00:00.000Z` |
| `target_branch` | `string` | 타겟 브랜치 | `main` |
| `source_branch` | `string` | 소스 브랜치 | `feature-branch` |
| `user_notes_count` | `integer` | 코멘트 수 | `5` |
| `upvotes` | `integer` | 추천 수 | `3` |
| `downvotes` | `integer` | 비추천 수 | `0` |
| `author` | `object` | 작성자 정보 | `{id, username, name, ...}` |
| `assignees` | `array` | 담당자 목록 | `[{id, username, ...}]` |
| `assignee` | `object` | 주 담당자 | `{id, username, ...}` |
| `reviewers` | `array` | 리뷰어 목록 | `[{id, username, ...}]` |
| `source_project_id` | `integer` | 소스 프로젝트 ID | `3` |
| `target_project_id` | `integer` | 타겟 프로젝트 ID | `3` |
| `labels` | `array[string]` | 라벨 목록 | `["bug"]` |
| `draft` | `boolean` | Draft 여부 | `false` |
| `work_in_progress` | `boolean` | WIP 여부 (deprecated) | `false` |
| `milestone` | `object` | 마일스톤 정보 | `{id, title, ...}` |
| `merge_when_pipeline_succeeds` | `boolean` | 파이프라인 성공 시 자동 머지 | `false` |
| `merge_status` | `string` | 머지 상태 | `can_be_merged` |
| `sha` | `string` | 최신 SHA | `abc123...` |
| `merge_commit_sha` | `string` | 머지 커밋 SHA | `def456...` |
| `squash_commit_sha` | `string` | 스쿼시 커밋 SHA | `ghi789...` |
| `discussion_locked` | `boolean` | 토론 잠금 여부 | `false` |
| `should_remove_source_branch` | `boolean` | 소스 브랜치 제거 여부 | `false` |
| `force_remove_source_branch` | `boolean` | 강제 소스 브랜치 제거 | `false` |
| `web_url` | `string` | GitLab 웹 URL | `https://gitlab.com/...` |
| `reference` | `string` | 참조 문자열 | `!1` |
| `time_stats` | `object` | 시간 통계 | `{time_estimate, total_time_spent}` |
| `squash` | `boolean` | 스쿼시 여부 | `false` |
| `has_conflicts` | `boolean` | 충돌 여부 | `false` |
| `blocking_discussions_resolved` | `boolean` | 차단 토론 해결 여부 | `true` |
| `approvals_before_merge` | `integer` | 머지 전 필요한 승인 수 | `0` |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request - 잘못된 요청 파라미터 |
| `401` | Unauthorized - 인증 실패 |
| `422` | Unprocessable Entity - 처리 불가능한 요청 |

---

## 10. List all group merge requests

### 기본 정보
- **기능:** 특정 그룹 및 하위 그룹의 모든 Merge Request를 조회합니다.
- **Endpoint:** `GET /api/v4/groups/{id}/merge_requests`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 그룹과 그 하위 그룹의 모든 Merge Request를 조회합니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `string` | Yes | 그룹 ID 또는 URL-인코딩된 경로 |

#### Query parameters
09번(List all merge requests)과 동일한 query parameter를 지원합니다.

### Response
#### `200 OK`
09번(List all merge requests)과 동일한 응답 스키마를 반환합니다.

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `401` | Unauthorized |
| `404` | Not Found - 그룹을 찾을 수 없음 |
| `422` | Unprocessable Entity |

---

## 16. List all project merge requests

### 기본 정보
- **기능:** 특정 프로젝트의 모든 Merge Request를 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트의 모든 Merge Request를 조회합니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |

#### Query parameters
09번(List all merge requests)과 동일한 query parameter를 지원하며, 추가로 다음 파라미터가 있습니다:

| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `iids` | `array` | No | 특정 IID를 가진 MR만 반환 |

### Response
#### `200 OK`
09번(List all merge requests)과 동일한 응답 스키마를 반환합니다.

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `401` | Unauthorized |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |
| `422` | Unprocessable Entity |

---

## 19. Retrieve a merge request

### 기본 정보
- **기능:** 특정 프로젝트의 단일 Merge Request를 상세 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트의 특정 Merge Request를 상세 조회합니다. 파이프라인, diff_refs, 충돌 정보 등 추가 필드를 포함합니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | `integer` | Yes | Merge Request의 내부 ID (IID) |

#### Query parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `render_html` | `boolean` | No | `true` 시 title/description의 HTML 렌더링 포함 |
| `include_diverged_commits_count` | `boolean` | No | 타겟 브랜치 대비 커밋 수 포함 |
| `include_rebase_in_progress` | `boolean` | No | 리베이스 진행 중 여부 포함 |

### Response
#### `200 OK`
09번 응답 스키마에 다음 필드가 추가됩니다:

| 필드명 | 타입 | 설명 | 예시 |
| --- | --- | --- | --- |
| `subscribed` | `boolean` | 구독 여부 | `true` |
| `changes_count` | `string` | 변경 파일 수 | `"5"` |
| `latest_build_started_at` | `string` | 최신 빌드 시작 시간 | `2024-01-01T00:00:00.000Z` |
| `latest_build_finished_at` | `string` | 최신 빌드 완료 시간 | `2024-01-01T01:00:00.000Z` |
| `first_deployed_to_production_at` | `string` | 프로덕션 최초 배포 시간 | `2024-01-02T00:00:00.000Z` |
| `pipeline` | `object` | 최신 파이프라인 정보 | `{id, iid, sha, ref, status, ...}` |
| `head_pipeline` | `object` | HEAD 파이프라인 상세 정보 | `{id, sha, status, user, duration, ...}` |
| `diff_refs` | `object` | Diff 참조 SHA | `{base_sha, head_sha, start_sha}` |
| `merge_error` | `string` | 머지 오류 메시지 | `null` |
| `rebase_in_progress` | `boolean` | 리베이스 진행 중 여부 | `false` |
| `diverged_commits_count` | `integer` | 분기된 커밋 수 | `3` |
| `first_contribution` | `boolean` | 첫 기여 여부 | `false` |
| `changes_count` | `string` | 변경된 파일 수 | `"5"` |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `404` | Not Found - MR 또는 프로젝트를 찾을 수 없음 |

---

## 21. Retrieve merge request participants

### 기본 정보
- **기능:** 특정 Merge Request의 참여자 목록을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/participants`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 Merge Request에 참여한 사용자(작성자, 코멘트 작성자 등) 목록을 조회합니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | `integer` | Yes | Merge Request의 IID |

### Response
#### `200 OK`
| 필드명 | 타입 | 설명 | 예시 |
| --- | --- | --- | --- |
| `id` | `integer` | 사용자 ID | `1` |
| `username` | `string` | 사용자명 | `johndoe` |
| `public_email` | `string` | 공개 이메일 | `johndoe@example.com` |
| `name` | `string` | 사용자 이름 | `John Doe` |
| `state` | `string` | 계정 상태 | `active` |
| `locked` | `boolean` | 계정 잠금 여부 | `false` |
| `avatar_url` | `string` | 아바타 URL | `https://...` |
| `web_url` | `string` | 프로필 URL | `https://gitlab.com/johndoe` |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `404` | Not Found |

---

## 22. Retrieve merge request reviewers

### 기본 정보
- **기능:** 특정 Merge Request의 리뷰어 목록을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/reviewers`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 Merge Request에 할당된 리뷰어 목록과 각 리뷰어의 상태를 조회합니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | `integer` | Yes | Merge Request의 IID |

### Response
#### `200 OK`
| 필드명 | 타입 | 설명 | 예시 |
| --- | --- | --- | --- |
| `user` | `object` | 리뷰어 사용자 정보 | `{id, username, name, ...}` |
| `user.id` | `integer` | 사용자 ID | `1` |
| `user.username` | `string` | 사용자명 | `johndoe` |
| `user.name` | `string` | 사용자 이름 | `John Doe` |
| `user.state` | `string` | 계정 상태 | `active` |
| `user.avatar_url` | `string` | 아바타 URL | `https://...` |
| `user.web_url` | `string` | 프로필 URL | `https://gitlab.com/johndoe` |
| `state` | `string` | 리뷰 상태 | `unreviewed` |
| `created_at` | `string` (ISO 8601) | 리뷰어 할당 시간 | `2024-01-01T00:00:00.000Z` |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `404` | Not Found |

---

## 27. Retrieve merge request changes

### 기본 정보
- **기능:** 특정 Merge Request의 변경 사항(diff)을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/changes`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 Merge Request의 코드 변경 사항(diff)을 상세 조회합니다. 각 파일의 diff, 변경 유형(new/renamed/deleted) 등을 포함합니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | `integer` | Yes | Merge Request의 IID |

#### Query parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `unidiff` | `boolean` | No | Unified diff 형식으로 반환 |

### Response
#### `200 OK`
19번(Retrieve a merge request) 응답에 다음 필드가 추가됩니다:

| 필드명 | 타입 | 설명 | 예시 |
| --- | --- | --- | --- |
| `changes` | `array` | 변경 파일 목록 | `[{diff, new_path, old_path, ...}]` |
| `changes[].diff` | `string` | 파일 diff 내용 | `@@ -1,3 +1,4 @@...` |
| `changes[].collapsed` | `boolean` | 접힘 여부 | `false` |
| `changes[].too_large` | `boolean` | diff가 너무 큰지 여부 | `false` |
| `changes[].new_path` | `string` | 새 파일 경로 | `src/feature.ts` |
| `changes[].old_path` | `string` | 이전 파일 경로 | `src/feature.ts` |
| `changes[].new_file` | `boolean` | 새 파일 여부 | `false` |
| `changes[].renamed_file` | `boolean` | 이름 변경 여부 | `false` |
| `changes[].deleted_file` | `boolean` | 삭제된 파일 여부 | `false` |
| `changes[].generated_file` | `boolean` | 생성된 파일 여부 | `false` |
| `overflow` | `boolean` | 변경 사항이 너무 많아 overflow 발생 여부 | `false` |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `404` | Not Found |

---

## 30. List all merge request pipelines

### 기본 정보
- **기능:** 특정 Merge Request와 연관된 모든 파이프라인을 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/pipelines`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 Merge Request에 대해 실행된 모든 CI/CD 파이프라인 목록을 조회합니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | `integer` | Yes | Merge Request의 내부 ID |

### Response
#### `200 OK`
| 필드명 | 타입 | 설명 | 예시 |
| --- | --- | --- | --- |
| `id` | `integer` | 파이프라인 ID | `47` |
| `iid` | `integer` | 파이프라인 IID | `5` |
| `project_id` | `integer` | 프로젝트 ID | `3` |
| `sha` | `string` | 커밋 SHA | `abc123def456` |
| `ref` | `string` | 브랜치/태그 참조 | `main` |
| `status` | `string` | 파이프라인 상태 | `success` |
| `source` | `string` | 트리거 소스 | `merge_request_event` |
| `created_at` | `string` (ISO 8601) | 생성 시간 | `2024-01-01T00:00:00.000Z` |
| `updated_at` | `string` (ISO 8601) | 수정 시간 | `2024-01-01T01:00:00.000Z` |
| `web_url` | `string` | 파이프라인 웹 URL | `https://gitlab.com/.../pipelines/47` |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `404` | Not Found |

---

## 36. List all issues that close on merge

### 기본 정보
- **기능:** Merge Request가 머지될 때 함께 닫히는 모든 Issue를 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/closes_issues`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
MR 설명에 "Closes #123" 등의 키워드로 연결된 Issue 중, MR이 머지되면 자동으로 닫히는 Issue 목록을 조회합니다.

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | `integer` | Yes | Merge Request의 IID |

#### Query parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `page` | `integer` | No | 페이지 번호 |
| `per_page` | `integer` | No | 페이지당 항목 수 |

### Response
#### `200 OK`
| 필드명 | 타입 | 설명 | 예시 |
| --- | --- | --- | --- |
| `note` | `string` | Issue 참조 노트 내용 | "Closes #123" |
| `author` | `object` | 노트 작성자 정보 | `{id, username, name, ...}` |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `403` | Forbidden - 접근 권한 없음 |
| `404` | Not Found |

---

## 37. List all issues related to the merge request

### 기본 정보
- **기능:** 특정 Merge Request와 관련된 모든 Issue를 조회합니다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/related_issues`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 Merge Request와 관련된 Issue 목록을 조회합니다. (36번 closes_issues와 달리, 관련 Issue 전체를 조회합니다.)

### Request
#### Headers
| 헤더 | 필수 | 설명 |
| --- | --- | --- |
| `Authorization` | Yes | `Bearer <token>` 형식 |

#### Path parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | `integer` | Yes | Merge Request의 IID |

#### Query parameters
| 필드명 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `page` | `integer` | No | 페이지 번호 |
| `per_page` | `integer` | No | 페이지당 항목 수 |

### Response
#### `200 OK`
(응답 스키마는 GitLab 문서 참조)

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400` | Bad Request |
| `403` | Forbidden - 접근 권한 없음 |
| `404` | Not Found |

---

