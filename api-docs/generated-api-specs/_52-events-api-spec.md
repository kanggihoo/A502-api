# 52-events API Spec

**조회(Pull) vs 실시간 알림(Push)의 차이.**

---

### 1. Webhook (웹훅)
- **방식**: **Push (실시간 수동 발송)**.
- **동작**: GitLab에서 이벤트(푸시, MR 생성, 댓글) 발생 순간, **내 서버로 HTTP POST 알림을 쏨**.
- **용도**: Mattermost 알림 보내기, Jenkins 빌드 즉시 시작.

---

### 2. Events API (`GET /api/v4/projects/{id}/events`)
- **방식**: **Pull (수동 데이터 조회)**.
- **동작**: 내 서버가 필요할 때 GET 요청을 보내서 **과거~현재 활동 기록(Audit/Activity Log)을 긁어옴**.
- **용도**: 
  - 통합 대시보드에 **"최근 팀원 활동 타임라인"** 출력.
  - 특정 사용자가 작성한 코멘트/푸시 내역 검색 및 통계 추출.

---

### 요약
- **Webhook**: "이벤트 일어났으니 지금 즉시 처리해!" (실시간 알림).
- **Events API**: "지난 1주일 동안 어떤 일들이 있었는지 목록 줘봐." (이력 조회).

## 1. List all visible events for a project

### 기본 정보

- **기능:** 특정 프로젝트의 모든 visible event를 조회한다. Push 이벤트가 Push event activities 제한을 초과하면 개별 commit 대신 단일 bulk push event를 반환한다.
- **Endpoint:** `GET /api/v4/projects/{id}/events`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** GET은 멱등

### 설명

프로젝트의 event 스트림을 조회한다. 필터(before/after 날짜, action, target_type)와 페이지네이션을 지원한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---:|---|
| `id` | `any` | Y | 프로젝트의 ID 또는 URL-encoded 경로 | `130` 또는 `group%2Fproject` |

#### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---:|---|
| `action` | `string` | N | Event action 필터 (예: `created`, `updated`, `merged`, `pushed`, `commented`, `closed`, `reopened`) | `pushed` |
| `target_type` | `string` | N | Event target type 필터 (예: `Issue`, `MergeRequest`, `Note`, `WikiPage::Meta`) | `Issue` |
| `before` | `string` | N | 이 날짜 이전의 event만 포함 (ISO 8601) | `2025-12-31T23:59:59Z` |
| `after` | `string` | N | 이 날짜 이후의 event만 포함 (ISO 8601) | `2025-01-01T00:00:00Z` |
| `sort` | `string` | N | 정렬 순서 (`asc` 또는 `desc`) | `desc` |
| `page` | `integer` | N | 페이지 번호 | `1` |
| `per_page` | `integer` | N | 페이지당 항목 수 (기본값: 20, 최대: 100) | `20` |

### Response

#### `200 OK`

Schema: `application/json` — Event 객체의 배열

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | Event 고유 ID | `1` |
| `project_id` | `integer` | 프로젝트 ID | `130` |
| `action_name` | `string` | Event action 이름 | `pushed` |
| `target_id` | `integer` | 대상 객체 ID (없으면 `null`) | `42` |
| `target_iid` | `integer` | 대상 객체의 IID (없으면 `null`) | `5` |
| `target_type` | `string` | 대상 객체 타입 | `MergeRequest` |
| `author_id` | `integer` | 작성자 ID | `10` |
| `target_title` | `string` | 대상 객체 제목 | `Fix login bug` |
| `created_at` | `string` | Event 생성 시간 (ISO 8601) | `2025-07-20T10:30:00.000Z` |
| `author` | `object` | 작성자 상세 정보 | |
| `author_username` | `string` | 작성자 username | `john` |
| `note` | `object` | 연결된 Note (없으면 `null`) | |
| `wiki_page` | `object` | 연결된 Wiki page (없으면 `null`) | |
| `push_data` | `object` | Push event 상세 (없으면 `null`) | |
| `imported` | `boolean` | 가져온(imported) event 여부 | `false` |
| `imported_from` | `string` | 가져온 소스 (imported가 true일 때) | `gitlab_project_migration` |

**author 객체:**

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | 사용자 ID | `10` |
| `username` | `string` | 사용자명 | `john` |
| `public_email` | `string` | 공개 이메일 | `john@example.com` |
| `name` | `string` | 이름 | `John Doe` |
| `state` | `string` | 계정 상태 | `active` |
| `locked` | `boolean` | 계정 잠김 여부 | `false` |
| `avatar_url` | `string` | 아바타 URL | `https://gitlab.example.com/uploads/avatar.png` |
| `avatar_path` | `string` | 아바타 경로 | `uploads/avatar.png` |
| `custom_attributes` | `array` | 커스텀 속성 배열 (key-value 쌍) | `[{"key": "team", "value": "backend"}]` |
| `web_url` | `string` | 프로필 URL | `https://gitlab.example.com/john` |

**note 객체:**

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | Note ID | `100` |
| `type` | `string` | Note 타입 | `DiscussionNote` |
| `body` | `string` | 본문 | `LGTM!` |
| `author` | `object` | 작성자 (author 객체와 동일 구조) | |
| `created_at` | `string` | 생성 시간 | `2025-07-20T10:30:00.000Z` |
| `updated_at` | `string` | 수정 시간 | `2025-07-20T11:00:00.000Z` |
| `system` | `boolean` | 시스템 생성 여부 | `false` |
| `noteable_id` | `integer` | 대상 객체 ID | `42` |
| `noteable_type` | `string` | 대상 객체 타입 | `MergeRequest` |
| `project_id` | `integer` | 프로젝트 ID | `130` |
| `commit_id` | `string` | 커밋 SHA (없으면 `null`) | `abc123def456` |
| `position` | `object` | diff position 정보 (없으면 `{}`) | |
| `resolvable` | `boolean` | 해결(resolve) 가능 여부 | `true` |
| `resolved` | `boolean` | 해결됨 여부 | `false` |
| `resolved_by` | `object` | 해결한 사용자 (author 객체와 동일 구조) | |
| `resolved_at` | `string` | 해결 시간 | `2025-07-20T12:00:00.000Z` |
| `suggestions` | `object` | 코드 제안 정보 | |
| `confidential` | `boolean` | 기밀 여부 | `false` |
| `internal` | `boolean` | 내부 노트 여부 | `false` |
| `imported` | `boolean` | 가져온 노트 여부 | `false` |
| `imported_from` | `string` | 가져온 소스 | `gitlab_project_migration` |
| `noteable_iid` | `integer` | 대상 객체 IID | `5` |
| `commands_changes` | `object` | quick commands 변경사항 | `{}` |

**suggestions 객체:**

| 필드 | 타입 | 설명 |
|---|---:|---:|
| `id` | `integer` | 제안 ID |
| `from_line` | `integer` | 시작 라인 |
| `to_line` | `integer` | 종료 라인 |
| `appliable` | `boolean` | 적용 가능 여부 |
| `applied` | `boolean` | 적용됨 여부 |
| `from_content` | `string` | 원본 내용 |
| `to_content` | `string` | 제안 내용 |

**wiki_page 객체:**

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `format` | `string` | Wiki page 포맷 | `markdown` |
| `slug` | `string` | URL slug | `home` |
| `title` | `string` | 제목 | `Home` |
| `wiki_page_meta_id` | `integer` | Wiki page meta ID | `1` |

**push_data 객체:**

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `commit_count` | `integer` | 커밋 수 (제한 초과 시 `0`) | `3` |
| `action` | `string` | Push action | `pushed` |
| `ref_type` | `string` | Ref 타입 | `branch` |
| `commit_from` | `string` | 이전 커밋 SHA | `abc123` |
| `commit_to` | `string` | 이후 커밋 SHA | `def456` |
| `ref` | `string` | Ref 이름 | `main` |
| `commit_title` | `string` | 마지막 커밋 제목 | `Fix login bug` |
| `ref_count` | `integer` | Push된 ref 수 | `1` |

### Errors

| 상태 코드 | 설명 |
|---:|---|
| `400 Bad Request` | 요청 파라미터가 유효하지 않음 |
| `404 Not Found` | 프로젝트를 찾을 수 없거나 접근 권한이 없음 |

---

## 2. List all events

### 기본 정보

- **기능:** 인증된 사용자 본인의 모든 event를 조회한다. Epic이나 Merge Request과 관련된 event는 반환하지 않는다.
- **Endpoint:** `GET /api/v4/events`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** GET은 멱등

### 설명

현재 인증된 사용자의 전체 event 스트림을 조회한다. `scope=all`로 설정하면 사용자가 속한 모든 프로젝트의 event를 포함한다. 프로젝트 단위(event/projects) API와 동일한 응답 스키마를 사용한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---:|---:|---|
| `scope` | `string` | N | `all`로 설정 시 사용자의 모든 프로젝트 event 포함 (기본값: 현재 사용자만) | `all` |
| `action` | `string` | N | Event action 필터 | `pushed` |
| `target_type` | `string` | N | Event target type 필터 | `Issue` |
| `before` | `string` | N | 이 날짜 이전의 event만 포함 (ISO 8601) | `2025-12-31T23:59:59Z` |
| `after` | `string` | N | 이 날짜 이후의 event만 포함 (ISO 8601) | `2025-01-01T00:00:00Z` |
| `sort` | `string` | N | 정렬 순서 (`asc` 또는 `desc`) | `desc` |
| `page` | `integer` | N | 페이지 번호 | `1` |
| `per_page` | `integer` | N | 페이지당 항목 수 | `20` |

### Response

#### `200 OK`

Schema: `application/json` — Event 객체의 배열

List all visible events for a project과 동일한 응답 스키마를 사용한다.

| 필드 | 타입 | 설명 | 예시 |
|---|---:|---:|---|
| `id` | `integer` | Event 고유 ID | `1` |
| `project_id` | `integer` | 프로젝트 ID | `130` |
| `action_name` | `string` | Event action 이름 | `pushed` |
| `target_id` | `integer` | 대상 객체 ID | `42` |
| `target_iid` | `integer` | 대상 객체 IID | `5` |
| `target_type` | `string` | 대상 객체 타입 | `MergeRequest` |
| `author_id` | `integer` | 작성자 ID | `10` |
| `target_title` | `string` | 대상 객체 제목 | `Fix login bug` |
| `created_at` | `string` | Event 생성 시간 (ISO 8601) | `2025-07-20T10:30:00.000Z` |
| `author` | `object` | 작성자 상세 정보 | |
| `author_username` | `string` | 작성자 username | `john` |
| `note` | `object` | 연결된 Note (없으면 `null`) | |
| `wiki_page` | `object` | 연결된 Wiki page (없으면 `null`) | |
| `push_data` | `object` | Push event 상세 (없으면 `null`) | |
| `imported` | `boolean` | 가져온 event 여부 | `false` |
| `imported_from` | `string` | 가져온 소스 | `gitlab_project_migration` |

중첩 객체(author, note, suggestions, wiki_page, push_data)의 상세 스키마는 1번 endpoint의 `200 OK` 응답 테이블을 참조한다.

### Errors

| 상태 코드 | 설명 |
|---:|---|
| `400 Bad Request` | 요청 파라미터가 유효하지 않음 |
| `401 Unauthorized` | 인증 토큰이 유효하지 않거나 누락됨 |
