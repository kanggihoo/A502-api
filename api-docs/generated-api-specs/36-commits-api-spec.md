# 36-커밋(Commits) API 명세

## 01-List all repository commits

## 기본 정보
- **기능:** 특정 프로젝트의 모든 커밋 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트의 저장소에 있는 모든 커밋을 반환한다. 날짜, 브랜치, 작성자 등 다양한 조건으로 필터링할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `ref_name` | string | N | 브랜치 또는 태그 이름. 기본 브랜치를 기준으로 함 |
| `since` | string | N | 이 날짜 이후의 커밋만 반환 (ISO 8601) |
| `until` | string | N | 이 날짜 이전의 커밋만 반환 (ISO 8601) |
| `path` | string | N | 특정 파일 경로로 필터링 |
| `follow` | boolean | N | path 필터링 시 파일 이름 변경 추적 |
| `author` | string | N | 작성자로 커밋 검색 |
| `all` | boolean | N | 모든 커밋 반환 |
| `with_stats` | boolean | N | 각 커밋의 통계 정보 포함 |
| `first_parent` | boolean | N | 병합의 첫 번째 부모만 포함 |
| `order` | string | N | 커밋 정렬 순서 지정 |
| `trailers` | boolean | N | Git 트레일러 파싱 및 포함 |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 (기본값: 20) |
| `pagination` | string | N | 페이지네이션 방식 지정 |
| `page_token` | string | N | 키셋 페이지네이션 시작 레코드 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | string | 커밋 SHA | `9b7d3c3...` |
| `short_id` | string | 커밋 짧은 SHA | `9b7d3c3` |
| `created_at` | string | 생성 일시 | `2025-01-01T00:00:00.000+09:00` |
| `parent_ids` | array[string] | 부모 커밋 SHA 목록 | `["abc123"]` |
| `title` | string | 커밋 제목 | `Initial commit` |
| `message` | string | 커밋 메시지 | `Initial commit\n` |
| `author_name` | string | 작성자 이름 | `John Doe` |
| `author_email` | string | 작성자 이메일 | `john@example.com` |
| `authored_date` | string | 작성 일시 | `2025-01-01T00:00:00.000+09:00` |
| `committer_name` | string | 커밋터 이름 | `John Doe` |
| `committer_email` | string | 커밋터 이메일 | `john@example.com` |
| `committed_date` | string | 커밋 일시 | `2025-01-01T00:00:00.000+09:00` |
| `trailers` | object | Git 트레일러 | `{"Signed-off-by": "John <john@example.com>"}` |
| `extended_trailers` | object | 확장 트레일러 | `{}` |
| `web_url` | string | 웹 UI URL | `https://gitlab.example.com/group/project/-/commit/9b7d3c3` |

JSON 예시:
```json
[
  {
    "id": "9b7d3c3a8e3c1a5b6d7f8e9a0b1c2d3e4f5a6b7c",
    "short_id": "9b7d3c3",
    "created_at": "2025-01-01T00:00:00.000+09:00",
    "parent_ids": ["abc123"],
    "title": "Initial commit",
    "message": "Initial commit\n",
    "author_name": "John Doe",
    "author_email": "john@example.com",
    "authored_date": "2025-01-01T00:00:00.000+09:00",
    "committer_name": "John Doe",
    "committer_email": "john@example.com",
    "committed_date": "2025-01-01T00:00:00.000+09:00",
    "trailers": {},
    "extended_trailers": {},
    "web_url": "https://gitlab.example.com/group/project/-/commit/9b7d3c3"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `401` | Unauthorized - 인증 실패 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 03-Retrieve a commit

## 기본 정보
- **기능:** 특정 커밋의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
커밋 SHA 또는 브랜치/태그 이름으로 특정 커밋을 조회한다. stats 파라미터로 통계 정보를 추가로 요청할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `sha` | string | Y | 커밋 SHA, 브랜치명 또는 태그명 | `9b7d3c3` or `main` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `stats` | boolean | N | 커밋 통계 포함 여부 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | string | 커밋 SHA | `9b7d3c3...` |
| `short_id` | string | 커밋 짧은 SHA | `9b7d3c3` |
| `created_at` | string | 생성 일시 | `2025-01-01T00:00:00.000+09:00` |
| `parent_ids` | array[string] | 부모 커밋 SHA 목록 | `["abc123"]` |
| `title` | string | 커밋 제목 | `Initial commit` |
| `message` | string | 커밋 메시지 | `Initial commit\n` |
| `author_name` | string | 작성자 이름 | `John Doe` |
| `author_email` | string | 작성자 이메일 | `john@example.com` |
| `authored_date` | string | 작성 일시 | `2025-01-01T00:00:00.000+09:00` |
| `committer_name` | string | 커밋터 이름 | `John Doe` |
| `committer_email` | string | 커밋터 이메일 | `john@example.com` |
| `committed_date` | string | 커밋 일시 | `2025-01-01T00:00:00.000+09:00` |
| `trailers` | object | Git 트레일러 | `{}` |
| `extended_trailers` | object | 확장 트레일러 | `{}` |
| `web_url` | string | 웹 UI URL | `https://gitlab.example.com/group/project/-/commit/9b7d3c3` |
| `stats` | object | 커밋 통계 (stats=true 시) | `{"additions": 10, "deletions": 2, "total": 12}` |
| `status` | string | 커밋 상태 | `success` |
| `project_id` | integer | 프로젝트 ID | `1234` |
| `last_pipeline` | object | 마지막 파이프라인 정보 | `{}` |

JSON 예시:
```json
{
  "id": "9b7d3c3a8e3c1a5b6d7f8e9a0b1c2d3e4f5a6b7c",
  "short_id": "9b7d3c3",
  "created_at": "2025-01-01T00:00:00.000+09:00",
  "parent_ids": ["abc123"],
  "title": "Initial commit",
  "message": "Initial commit\n",
  "author_name": "John Doe",
  "author_email": "john@example.com",
  "authored_date": "2025-01-01T00:00:00.000+09:00",
  "committer_name": "John Doe",
  "committer_email": "john@example.com",
  "committed_date": "2025-01-01T00:00:00.000+09:00",
  "trailers": {},
  "extended_trailers": {},
  "web_url": "https://gitlab.example.com/group/project/-/commit/9b7d3c3",
  "stats": {
    "additions": 10,
    "deletions": 2,
    "total": 12
  },
  "status": "success",
  "project_id": 1234,
  "last_pipeline": {}
}
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 커밋을 찾을 수 없음 |

---

## 04-Retrieve a commit diff

## 기본 정보
- **기능:** 특정 커밋의 diff(변경 사항)를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/diff`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 커밋의 diff 내용을 반환한다. 각 파일별 변경 사항, 추가/삭제 여부 등을 확인할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `sha` | string | Y | 커밋 SHA, 브랜치명 또는 태그명 | `9b7d3c3` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `unidiff` | boolean | N | Unified diff 형식으로 반환 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `diff` | string | diff 내용 | `@@ -1,3 +1,4 @@\n...` |
| `collapsed` | boolean | diff 접힘 여부 | `false` |
| `too_large` | boolean | diff가 너무 큰지 여부 | `false` |
| `new_path` | string | 새 파일 경로 | `src/main.js` |
| `old_path` | string | 이전 파일 경로 | `src/main.js` |
| `a_mode` | string | 이전 파일 모드 | `100644` |
| `b_mode` | string | 새 파일 모드 | `100644` |
| `new_file` | boolean | 새 파일 여부 | `false` |
| `renamed_file` | boolean | 파일명 변경 여부 | `false` |
| `deleted_file` | boolean | 삭제된 파일 여부 | `false` |
| `generated_file` | boolean | 생성된 파일 여부 | `false` |

JSON 예시:
```json
[
  {
    "diff": "@@ -1,3 +1,4 @@\n+new line\n line1\n line2\n line3\n",
    "collapsed": false,
    "too_large": false,
    "new_path": "src/main.js",
    "old_path": "src/main.js",
    "a_mode": "100644",
    "b_mode": "100644",
    "new_file": false,
    "renamed_file": false,
    "deleted_file": false,
    "generated_file": false
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 커밋을 찾을 수 없음 |

---

## 11-List all merge requests for a commit

## 기본 정보
- **기능:** 특정 커밋과 연결된 모든 Merge Request를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/merge_requests`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 커밋과 연관된 모든 Merge Request 목록을 반환한다. 상태별 필터링이 가능하다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `sha` | string | Y | 커밋 SHA 또는 브랜치/태그명 | `9b7d3c3` or `main` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `state` | string | N | MR 상태로 필터링 (예: `opened`, `closed`, `merged`, `all`) |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | integer | MR ID | `42` |
| `iid` | integer | 프로젝트 내 MR IID | `1` |
| `project_id` | integer | 프로젝트 ID | `1234` |
| `title` | string | MR 제목 | `Add new feature` |
| `description` | string | MR 설명 | `Implements feature X` |
| `state` | string | MR 상태 | `opened` |
| `created_at` | string | 생성 일시 | `2025-01-01T00:00:00.000+09:00` |
| `updated_at` | string | 업데이트 일시 | `2025-01-02T00:00:00.000+09:00` |
| `merged_by` | object | 병합한 사용자 정보 | `{"id": 1, "username": "john", ...}` |
| `merge_user` | object | 병합 승인 사용자 | `{"id": 1, ...}` |
| `merged_at` | string | 병합 일시 | `2025-01-03T00:00:00.000+09:00` |
| `closed_by` | object | 닫은 사용자 정보 | `{"id": 2, ...}` |
| `closed_at` | string | 닫힌 일시 | `2025-01-03T00:00:00.000+09:00` |
| `target_branch` | string | 대상 브랜치 | `main` |
| `source_branch` | string | 소스 브랜치 | `feature/new` |
| `user_notes_count` | integer | 코멘트 수 | `5` |
| `upvotes` | integer | 좋아요 수 | `3` |
| `downvotes` | integer | 싫어요 수 | `0` |
| `author` | object | 작성자 정보 | `{"id": 1, "username": "john", ...}` |
| `assignees` | object | 담당자 정보 | `{"id": 2, "username": "jane", ...}` |
| `assignee` | object | 담당자 정보 | `{"id": 2, ...}` |
| `reviewers` | object | 리뷰어 정보 | `{"id": 3, ...}` |
| `source_project_id` | integer | 소스 프로젝트 ID | `1234` |
| `target_project_id` | integer | 대상 프로젝트 ID | `1234` |
| `labels` | array[string] | 레이블 목록 | `["bug", "critical"]` |
| `draft` | boolean | 초안(Draft) 여부 | `false` |
| `milestone` | object | 마일스톤 정보 | `{"id": 1, "title": "Sprint 1", ...}` |
| `merge_when_pipeline_succeeds` | boolean | 파이프라인 성공 시 자동 병합 | `false` |
| `merge_status` | string | 병합 상태 | `can_be_merged` |
| `sha` | string | MR의 SHA | `9b7d3c3...` |
| `merge_commit_sha` | string | 병합 커밋 SHA | `abc123...` |
| `web_url` | string | 웹 UI URL | `https://gitlab.example.com/group/project/-/merge_requests/1` |
| `has_conflicts` | boolean | 충돌 여부 | `false` |
| `blocking_discussions_resolved` | boolean | 차단 디스커션 해결 여부 | `true` |
| `approvals_before_merge` | integer | 병합 전 필요한 승인 수 | `1` |

JSON 예시:
```json
[
  {
    "id": 42,
    "iid": 1,
    "project_id": 1234,
    "title": "Add new feature",
    "description": "Implements feature X",
    "state": "merged",
    "created_at": "2025-01-01T00:00:00.000+09:00",
    "updated_at": "2025-01-02T00:00:00.000+09:00",
    "target_branch": "main",
    "source_branch": "feature/new",
    "author": {
      "id": 1,
      "username": "john",
      "name": "John Doe",
      "state": "active",
      "avatar_url": "https://gitlab.example.com/uploads/-/system/user/avatar/1/avatar.png",
      "web_url": "https://gitlab.example.com/john"
    },
    "labels": ["bug"],
    "draft": false,
    "merge_status": "can_be_merged",
    "web_url": "https://gitlab.example.com/group/project/-/merge_requests/1"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 커밋을 찾을 수 없음 |
