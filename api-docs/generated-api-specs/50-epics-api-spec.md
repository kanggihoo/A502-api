# 50 - Epics API Specification

---

## 1. List all group epics

## 기본 정보
- **기능:** 특정 그룹과 그 하위 그룹의 모든 에픽 목록을 조회한다. 페이지네이트되며 기본 20개 결과를 반환한다.
- **Endpoint:** `GET /api/v4/groups/{id}/epics`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 그룹 및 서브그룹의 모든 에픽을 조회한다. 다양한 필터(상태, 작성자, 라벨, 날짜 범위 등)를 지원한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 그룹의 ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `order_by` | `string` | N | 정렬 기준 (`created_at`, `updated_at`, `title`) |
| `sort` | `string` | N | 정렬 방향 (`asc`, `desc`) |
| `search` | `string` | N | 제목 또는 설명에서 텍스트 검색 |
| `state` | `string` | N | 에픽 상태 필터 (`opened`, `closed`, `all`) |
| `author_id` | `integer` | N | 특정 작성자 ID로 필터 |
| `author_username` | `string` | N | 특정 작성자 username으로 필터 |
| `labels` | `array` | N | 쉼표로 구분된 라벨 이름 목록 |
| `with_labels_details` | `boolean` | N | 라벨 제목 및 기타 세부 정보 반환 |
| `created_after` | `string` | N | 지정 시간 이후 생성된 에픽 |
| `created_before` | `string` | N | 지정 시간 이전 생성된 에픽 |
| `updated_after` | `string` | N | 지정 시간 이후 업데이트된 에픽 |
| `updated_before` | `string` | N | 지정 시간 이전 업데이트된 에픽 |
| `include_ancestor_groups` | `boolean` | N | 상위 그룹의 에픽 포함 |
| `include_descendant_groups` | `boolean` | N | 하위 그룹의 에픽 포함 |
| `my_reaction_emoji` | `string` | N | 인증된 사용자가 특정 이모지로 반응한 에픽 |
| `confidential` | `boolean` | N | 기밀 에픽 필터 |
| `page` | `integer` | N | 페이지 번호 (기본: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본: 20) |
| `not` | `object` | N | 필터 제외 조건을 담은 객체 |
| `not[labels]` | `array` | N | 제외할 라벨 이름 목록 |
| `not[author_id]` | `integer` | N | 제외할 작성자 ID |
| `not[author_username]` | `string` | N | 제외할 작성자 username |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 에픽 ID |
| `work_item_id` | `integer` | 연결된 Work Item ID |
| `iid` | `integer` | 에픽 내부 ID |
| `color` | `string` | 색상 |
| `text_color` | `string` | 텍스트 색상 |
| `group_id` | `integer` | 그룹 ID |
| `parent_id` | `integer` | 부모 에픽 ID |
| `parent_iid` | `integer` | 부모 에픽 내부 ID |
| `imported` | `boolean` | 가져오기 여부 |
| `imported_from` | `string` | 가져온 소스 |
| `title` | `string` | 제목 |
| `description` | `string` | 설명 |
| `confidential` | `boolean` | 기밀 여부 |
| `author` | `object` | 작성자 정보 (id, username, name, avatar_url 등) |
| `start_date` | `string` | 시작일 |
| `start_date_is_fixed` | `boolean` | 시작일 고정 여부 |
| `start_date_fixed` | `string` | 고정된 시작일 |
| `start_date_from_inherited_source` | `string` | 상속된 소스의 시작일 |
| `start_date_from_milestones` | `string` | 마일스톤 기반 시작일 |
| `end_date` | `string` | 종료일 |
| `due_date` | `string` | 마감일 |
| `due_date_is_fixed` | `boolean` | 마감일 고정 여부 |
| `due_date_fixed` | `string` | 고정된 마감일 |
| `due_date_from_inherited_source` | `string` | 상속된 소스의 마감일 |
| `due_date_from_milestones` | `string` | 마일스톤 기반 마감일 |
| `state` | `string` | 상태 (opened/closed) |
| `web_edit_url` | `string` | 웹 편집 URL |
| `web_url` | `string` | 웹 URL |
| `references` | `array` | 참조 정보 |
| `reference` | `string` | 참조 문자열 |
| `created_at` | `string` | 생성일시 |
| `updated_at` | `string` | 업데이트일시 |
| `closed_at` | `string` | 종료일시 |
| `labels` | `array` | 라벨 목록 |
| `upvotes` | `integer` | 추천 수 |
| `downvotes` | `integer` | 비추천 수 |
| `subscribed` | `boolean` | 구독 여부 |
| `_links` | `object` | 관련 링크 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `403 Forbidden` | 권한 없음 |
| `404 Not Found` | 그룹을 찾을 수 없음 |
| `422 Unprocessable Entity` | 처리할 수 없는 요청 |

---

## 2. Get details of an epic

## 기본 정보
- **기능:** 단일 에픽의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/epics/{epic_iid}`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 그룹의 특정 에픽 상세 정보를 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 그룹의 ID |
| `epic_iid` | `integer` | Y | 에픽의 내부 ID |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 에픽 ID |
| `work_item_id` | `integer` | 연결된 Work Item ID |
| `iid` | `integer` | 에픽 내부 ID |
| `color` | `string` | 색상 |
| `text_color` | `string` | 텍스트 색상 |
| `group_id` | `integer` | 그룹 ID |
| `parent_id` | `integer` | 부모 에픽 ID |
| `parent_iid` | `integer` | 부모 에픽 내부 ID |
| `imported` | `boolean` | 가져오기 여부 |
| `imported_from` | `string` | 가져온 소스 |
| `title` | `string` | 제목 |
| `description` | `string` | 설명 |
| `confidential` | `boolean` | 기밀 여부 |
| `author` | `object` | 작성자 정보 |
| `start_date` | `string` | 시작일 |
| `start_date_is_fixed` | `boolean` | 시작일 고정 여부 |
| `start_date_fixed` | `string` | 고정된 시작일 |
| `start_date_from_inherited_source` | `string` | 상속된 소스의 시작일 |
| `start_date_from_milestones` | `string` | 마일스톤 기반 시작일 |
| `end_date` | `string` | 종료일 |
| `due_date` | `string` | 마감일 |
| `due_date_is_fixed` | `boolean` | 마감일 고정 여부 |
| `due_date_fixed` | `string` | 고정된 마감일 |
| `due_date_from_inherited_source` | `string` | 상속된 소스의 마감일 |
| `due_date_from_milestones` | `string` | 마일스톤 기반 마감일 |
| `state` | `string` | 상태 |
| `web_edit_url` | `string` | 웹 편집 URL |
| `web_url` | `string` | 웹 URL |
| `references` | `array` | 참조 정보 |
| `reference` | `string` | 참조 문자열 |
| `created_at` | `string` | 생성일시 |
| `updated_at` | `string` | 업데이트일시 |
| `closed_at` | `string` | 종료일시 |
| `labels` | `array` | 라벨 목록 |
| `upvotes` | `integer` | 추천 수 |
| `downvotes` | `integer` | 비추천 수 |
| `subscribed` | `boolean` | 구독 여부 |
| `_links` | `object` | 관련 링크 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `403 Forbidden` | 권한 없음 |
| `404 Not Found` | 에픽 또는 그룹을 찾을 수 없음 |

---

## 3. List all issues for an epic

## 기본 정보
- **기능:** 특정 에픽에 할당된 모든 이슈 목록을 조회한다. 인증된 사용자가 접근 가능한 이슈만 반환한다. 페이지네이트되며 기본 20개 결과를 반환한다.
- **Endpoint:** `GET /api/v4/groups/{id}/epics/{epic_iid}/issues`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 에픽에 할당된 이슈 목록을 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 그룹의 ID 또는 URL 인코딩된 경로 |
| `epic_iid` | `any` | Y | 에픽의 내부 ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `page` | `integer` | N | 페이지 번호 (기본: 1) |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본: 20) |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|
| `id` | `integer` | 이슈 ID |
| `iid` | `integer` | 이슈 내부 ID |
| `project_id` | `integer` | 프로젝트 ID |
| `title` | `string` | 제목 |
| `description` | `string` | 설명 |
| `state` | `string` | 상태 (opened/closed) |
| `created_at` | `string` | 생성일시 |
| `updated_at` | `string` | 업데이트일시 |
| `closed_at` | `string` | 종료일시 |
| `closed_by` | `object` | 종료한 사용자 정보 |
| `labels` | `array` | 라벨 목록 |
| `milestone` | `object` | 마일스톤 정보 |
| `assignees` | `object` | 담당자 정보 |
| `author` | `object` | 작성자 정보 |
| `type` | `string` | 이슈 타입 (ISSUE, INCIDENT, TEST_CASE, REQUIREMENT, TASK, TICKET) |
| `assignee` | `object` | 담당자 정보 |
| `user_notes_count` | `integer` | 코멘트 수 |
| `merge_requests_count` | `integer` | 연결된 MR 수 |
| `upvotes` | `integer` | 추천 수 |
| `downvotes` | `integer` | 비추천 수 |
| `start_date` | `string` | 시작일 |
| `due_date` | `string` | 마감일 |
| `confidential` | `boolean` | 기밀 여부 |
| `discussion_locked` | `boolean` | 토론 잠금 여부 |
| `issue_type` | `string` | 이슈 유형 |
| `web_url` | `string` | 웹 URL |
| `time_stats` | `object` | 시간 통계 |
| `task_completion_status` | `object` | 작업 완료 상태 |
| `weight` | `integer` | 가중치 |
| `blocking_issues_count` | `integer` | 차단된 이슈 수 |
| `has_tasks` | `boolean` | 작업 항목 포함 여부 |
| `task_status` | `string` | 작업 상태 |
| `_links` | `object` | 관련 링크 |
| `references` | `object` | 참조 정보 (short, relative, full) |
| `severity` | `string` | 심각도 (UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL) |
| `subscribed` | `boolean` | 구독 여부 |
| `moved_to_id` | `integer` | 이동된 대상 ID |
| `imported` | `boolean` | 가져오기 여부 |
| `imported_from` | `string` | 가져온 소스 |
| `service_desk_reply_to` | `string` | Service Desk 회신 주소 |
| `epic_iid` | `string` | 에픽 내부 ID |
| `epic` | `object` | 에픽 정보 (id, iid, title, url, group_id 등) |
| `iteration` | `object` | 반복 정보 |
| `health_status` | `string` | 건강 상태 |
| `epic_issue_id` | `integer` | 에픽-이슈 관계 ID |
| `relative_position` | `integer` | 에픽 트리 내 상대 위치 |

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `401 Unauthorized` | 인증 실패 |
| `403 Forbidden` | 권한 없음 |
| `404 Not Found` | 에픽 또는 그룹을 찾을 수 없음 |
