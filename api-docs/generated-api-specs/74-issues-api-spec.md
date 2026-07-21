# 74 Issues API Specification

> GitLab REST API — Issues 카테고리의 주요 GET Endpoint 문서

---

## 1. List all issues for the currently authenticated user

### 기본 정보
- **기능:** 현재 인증된 사용자가 접근 가능한 모든 이슈 목록을 조회한다. 기본적으로는 현재 사용자가 생성한 이슈만 반환하며, `scope=all`을 지정하면 모든 이슈를 조회할 수 있다.
- **Endpoint:** `GET /api/v4/issues`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
인증된 사용자가 액세스할 수 있는 프로젝트의 이슈를 페이지네이션하여 반환한다. 다양한 필터 파라미터를 지원하여 상태, 레이블, 마일스톤, 담당자, 검색어 등으로 결과를 좁힐 수 있다.

### Request

#### Headers
| 이름 | 값 | 필수 |
| --- | --- | --- |
| `Authorization` | `Bearer <token>` | Yes |
| `Content-Type` | `application/json` | No |

#### Path parameters
없음

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `with_labels_details` | `boolean` | No | 레이블의 제목 등 상세 정보를 반환 |
| `state` | `string` | No | 이슈 상태로 필터 (`opened`, `closed`, `all`) |
| `closed_by_id` | `integer` | No | 특정 사용자가 닫은 이슈만 반환 |
| `order_by` | `string` | No | 정렬 기준 (`created_at`, `due_date`, `label_priority`, `milestone_due`, `popularity`, `priority`, `relative_position`, `title`, `updated_at`) |
| `sort` | `string` | No | 정렬 방향 (`asc`, `desc`) |
| `due_date` | `string` | No | 마감일 필터 (`overdue`, `week`, `month`, `next_month_and_previous_two_weeks`, `0`) |
| `issue_type` | `string` | No | 이슈 유형 (`issue`, `incident`, `test_case`, `requirement`, `task`, `ticket`) |
| `labels` | `array` | No | 쉼표로 구분된 레이블 이름 목록 |
| `milestone` | `string` | No | 마일스톤 제목 |
| `milestone_id` | `string` | No | 특정 시간박스 값을 가진 마일스톤의 이슈 (`Any`, `None`, `Upcoming`, `Started`) |
| `iids` | `array` | No | 이슈 IID 배열 |
| `search` | `string` | No | 제목, 설명 또는 이들의 조합에서 텍스트 검색 |
| `in` | `string` | No | 검색 대상 필드 (`title`, `description`, 또는 쉼표 조합) |
| `author_id` | `integer` | No | 특정 작성자의 이슈만 반환 |
| `author_username` | `string` | No | 특정 사용자명의 작성자가 만든 이슈만 반환 |
| `assignee_id` | `any` | No | 특정 담당자에게 할당된 이슈만 반환 |
| `assignee_username` | `array` | No | 특정 사용자명의 담당자에게 할당된 이슈만 반환 |
| `created_after` | `string` | No | 지정된 시간 이후 생성된 이슈 |
| `created_before` | `string` | No | 지정된 시간 이전 생성된 이슈 |
| `updated_after` | `string` | No | 지정된 시간 이후 업데이트된 이슈 |
| `updated_before` | `string` | No | 지정된 시간 이전 업데이트된 이슈 |
| `not` | `object` | No | 지정된 파라미터를 제외하는 필터 (하위 필드: `labels`, `milestone`, `milestone_id`, `iids`, `author_id`, `author_username`, `assignee_id`, `assignee_username`, `weight`, `iteration_id`, `iteration_title`) |
| `scope` | `string` | No | 조회 범위 (`created_by_me`, `assigned_to_me`, `all`) |
| `my_reaction_emoji` | `string` | No | 인증된 사용자가 특정 이모지로 반응한 이슈만 반환 |
| `confidential` | `boolean` | No | 기밀 이슈 또는 공개 이슈 필터 |
| `weight` | `any` | No | 이슈 weight 값으로 필터 |
| `epic_id` | `any` | No | 특정 Epic과 연결된 이슈 필터 |
| `health_status` | `string` | No | 상태값 필터 (`on_track`, `needs_attention`, `at_risk`, `none`, `any`) |
| `iteration_id` | `any` | No | 특정 iteration ID에 할당된 이슈 |
| `iteration_title` | `string` | No | 특정 iteration 제목에 할당된 이슈 |
| `page` | `integer` | No | 페이지 번호 |
| `per_page` | `integer` | No | 페이지당 항목 수 |
| `non_archived` | `boolean` | No | 보관되지 않은 프로젝트의 이슈만 반환 |

### Response

#### `200 OK`
| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `id` | `integer` | 이슈 ID (전역 고유) |
| `iid` | `integer` | 이슈 IID (프로젝트 내부 고유) |
| `project_id` | `integer` | 프로젝트 ID |
| `title` | `string` | 이슈 제목 |
| `description` | `string` | 이슈 설명 |
| `state` | `string` | 이슈 상태 (`opened`/`closed`) |
| `created_at` | `string` | 생성 시간 |
| `updated_at` | `string` | 업데이트 시간 |
| `closed_at` | `string` | 닫힌 시간 |
| `closed_by` | `object` | 이슈를 닫은 사용자 정보 |
| `labels` | `array[string]` | 레이블 목록 |
| `milestone` | `object` | 연결된 마일스톤 정보 |
| `assignees` | `array[object]` | 담당자 목록 |
| `author` | `object` | 작성자 정보 |
| `type` | `string` | 이슈 유형 (`ISSUE`, `INCIDENT`, `TEST_CASE`, `REQUIREMENT`, `TASK`, `TICKET`) |
| `assignee` | `object` | 담당자 정보 |
| `user_notes_count` | `integer` | 코멘트 수 |
| `merge_requests_count` | `integer` | 연결된 MR 수 |
| `upvotes` | `integer` | upvote 수 |
| `downvotes` | `integer` | downvote 수 |
| `start_date` | `string` | 시작일 |
| `due_date` | `string` | 마감일 |
| `confidential` | `boolean` | 기밀 이슈 여부 |
| `discussion_locked` | `boolean` | 토론 잠금 여부 |
| `issue_type` | `string` | 이슈 유형 |
| `web_url` | `string` | GitLab 웹 UI URL |
| `time_stats` | `object` | 시간 추적 정보 (`time_estimate`, `total_time_spent`, `human_time_estimate`, `human_total_time_spent`) |
| `task_completion_status` | `object` | 작업 완료 상태 (`count`, `completed_count`) |
| `weight` | `integer` | weight 값 |
| `blocking_issues_count` | `integer` | 차단 중인 이슈 수 |
| `has_tasks` | `boolean` | 작업 항목 포함 여부 |
| `task_status` | `string` | 작업 상태 |
| `_links` | `object` | 관련 링크 |
| `references` | `object` | 참조 문자열 (`short`, `relative`, `full`) |
| `severity` | `string` | 심각도 (`UNKNOWN`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`) |
| `subscribed` | `boolean` | 구독 여부 |
| `moved_to_id` | `integer` | 이동된 대상 이슈 ID |
| `imported` | `boolean` | 가져오기 여부 |
| `imported_from` | `string` | 가져온 소스 |
| `service_desk_reply_to` | `string` | Service Desk 회신 주소 |
| `epic_iid` | `string` | Epic IID |
| `epic` | `object` | 연결된 Epic 정보 |
| `iteration` | `object` | 연결된 Iteration 정보 |
| `health_status` | `string` | 상태값 |

> 응답은 배열 형태로 반환되며, 각 요소는 위 스키마를 따른다.

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400 Bad Request` | 잘못된 요청 (예: 잘못된 파라미터 값) |

---

## 2. Retrieve an issue

### 기본 정보
- **기능:** 지정된 단일 이슈의 상세 정보를 조회한다. 관리자만 사용할 수 있다.
- **Endpoint:** `GET /api/v4/issues/{id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (관리자 전용)
- **멱등성:** 지원

### 설명
이슈의 전역 ID(`id`)를 사용하여 특정 이슈 하나의 모든 필드를 반환한다. 관리자 권한이 필요하다.

### Request

#### Headers
| 이름 | 값 | 필수 |
| --- | --- | --- |
| `Authorization` | `Bearer <token>` | Yes |
| `Content-Type` | `application/json` | No |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `string` | Yes | 조회할 이슈의 전역 ID |

#### Query parameters
없음

### Response

#### `200 OK`
List all issues endpoint의 응답과 동일한 스키마를 가진 단일 이슈 객체를 반환한다.

| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `id` | `integer` | 이슈 ID (전역 고유) |
| `iid` | `integer` | 이슈 IID (프로젝트 내부 고유) |
| `project_id` | `integer` | 프로젝트 ID |
| `title` | `string` | 이슈 제목 |
| `description` | `string` | 이슈 설명 |
| `state` | `string` | 이슈 상태 |
| `created_at` | `string` | 생성 시간 |
| `updated_at` | `string` | 업데이트 시간 |
| `closed_at` | `string` | 닫힌 시간 |
| `closed_by` | `object` | 이슈를 닫은 사용자 |
| `labels` | `array[string]` | 레이블 목록 |
| `milestone` | `object` | 연결된 마일스톤 |
| `assignees` | `array[object]` | 담당자 목록 |
| `author` | `object` | 작성자 |
| `type` | `string` | 이슈 유형 |
| `assignee` | `object` | 담당자 |
| `user_notes_count` | `integer` | 코멘트 수 |
| `merge_requests_count` | `integer` | 연결된 MR 수 |
| `upvotes` | `integer` | upvote 수 |
| `downvotes` | `integer` | downvote 수 |
| `start_date` | `string` | 시작일 |
| `due_date` | `string` | 마감일 |
| `confidential` | `boolean` | 기밀 여부 |
| `discussion_locked` | `boolean` | 토론 잠금 여부 |
| `issue_type` | `string` | 이슈 유형 |
| `web_url` | `string` | GitLab 웹 UI URL |
| `time_stats` | `object` | 시간 추적 정보 |
| `task_completion_status` | `object` | 작업 완료 상태 |
| `weight` | `integer` | weight |
| `blocking_issues_count` | `integer` | 차단 중인 이슈 수 |
| `has_tasks` | `boolean` | 작업 항목 포함 여부 |
| `task_status` | `string` | 작업 상태 |
| `_links` | `object` | 관련 링크 |
| `references` | `object` | 참조 문자열 |
| `severity` | `string` | 심각도 |
| `subscribed` | `boolean` | 구독 여부 |
| `moved_to_id` | `integer` | 이동된 대상 이슈 ID |
| `imported` | `boolean` | 가져오기 여부 |
| `imported_from` | `string` | 가져온 소스 |
| `service_desk_reply_to` | `string` | Service Desk 회신 주소 |
| `epic_iid` | `string` | Epic IID |
| `epic` | `object` | Epic 정보 |
| `iteration` | `object` | Iteration 정보 |
| `health_status` | `string` | 상태값 |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400 Bad Request` | 잘못된 요청 |
| `404 Not Found` | 지정된 ID의 이슈를 찾을 수 없음 |

---

## 3. List all participants in an issue

### 기본 정보
- **기능:** 특정 이슈에 참여자인 모든 사용자 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/issues/{issue_iid}/participants`
- **인증:** Bearer Token 필요 (비공개 프로젝트 또는 기밀 이슈인 경우 필수)
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트와 이슈 IID에 해당하는 이슈의 모든 참여자(participant)를 반환한다. 프로젝트가 비공개이거나 이슈가 기밀인 경우 인증이 필요하다. 일반적으로 Personal Access Token으로 인증한다.

### Request

#### Headers
| 이름 | 값 | 필수 |
| --- | --- | --- |
| `Authorization` | `Bearer <token>` | Yes (비공개/기밀인 경우) |
| `Content-Type` | `application/json` | No |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | `any` | Yes | 프로젝트 ID 또는 URL-인코딩된 프로젝트 경로 |
| `issue_iid` | `integer` | Yes | 프로젝트 내부 이슈 IID |

#### Query parameters
없음

### Response

#### `200 OK`
각 참여자 정보를 포함한 배열을 반환한다.

| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `id` | `integer` | 사용자 ID |
| `username` | `string` | 사용자명 |
| `public_email` | `string` | 공개 이메일 |
| `name` | `string` | 사용자 이름 |
| `state` | `string` | 계정 상태 (`active`/`blocked`) |
| `locked` | `boolean` | 계정 잠금 여부 |
| `avatar_url` | `string` | 아바타 URL |
| `avatar_path` | `string` | 아바타 경로 |
| `custom_attributes` | `array[object]` | 커스텀 속성 목록 |
| `web_url` | `string` | GitLab 프로필 URL |

### Errors
| 상태 코드 | 설명 |
| --- | --- |
| `400 Bad Request` | 잘못된 요청 |
| `404 Not Found` | 프로젝트 또는 이슈를 찾을 수 없음 |
