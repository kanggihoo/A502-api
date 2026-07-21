# 135 Push Rules API Spec

---

## 1. Retrieve the push rules of a group [GET]

### 기본 정보
- **기능:** 그룹의 push 규칙 조회
- **Endpoint:** `GET /api/v4/groups/{id}/push_rule`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 그룹에 설정된 push 규칙을 반환한다. push 규칙은 커밋 메시지 포맷, 파일 크기 제한, 서명 확인 등 저장소에 push할 때 적용되는 제약 조건을 정의한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `string` | Y | 그룹 ID 또는 URL 인코딩된 그룹 경로 |

### Response
#### `200 OK`
```json
{
  "id": "integer",
  "created_at": "string",
  "commit_message_regex": "string",
  "commit_message_negative_regex": "string",
  "branch_name_regex": "string",
  "author_email_regex": "string",
  "file_name_regex": "string",
  "deny_delete_tag": "boolean",
  "member_check": "boolean",
  "prevent_secrets": "boolean",
  "max_file_size": "integer",
  "commit_committer_check": "boolean",
  "commit_committer_name_check": "boolean",
  "reject_unsigned_commits": "boolean",
  "reject_non_dco_commits": "boolean"
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | `integer` | push 규칙 ID |
| `created_at` | `string` (datetime) | 생성 일시 |
| `commit_message_regex` | `string` | 커밋 메시지 허용 정규식 |
| `commit_message_negative_regex` | `string` | 커밋 메시지 금지 정규식 |
| `branch_name_regex` | `string` | 브랜치 이름 허용 정규식 |
| `author_email_regex` | `string` | 작성자 이메일 허용 정규식 |
| `file_name_regex` | `string` | 파일 이름 금지 정규식 |
| `deny_delete_tag` | `boolean` | 태그 삭제 금지 여부 |
| `member_check` | `boolean` | 멤버 확인 여부 |
| `prevent_secrets` | `boolean` | Secret 파일 push 금지 여부 |
| `max_file_size` | `integer` | 최대 파일 크기 (MB) |
| `commit_committer_check` | `boolean` | 커밋 작성자 = push 사용자 일치 확인 여부 |
| `commit_committer_name_check` | `boolean` | 커밋 작성자명 확인 여부 |
| `reject_unsigned_commits` | `boolean` | 서명되지 않은 커밋 거부 여부 |
| `reject_non_dco_commits` | `boolean` | DCO 서명되지 않은 커밋 거부 여부 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 그룹을 찾을 수 없음 |

---

## 2. Retrieve the push rules of a project [GET]

### 기본 정보
- **기능:** 프로젝트의 push 규칙 조회
- **Endpoint:** `GET /api/v4/projects/{id}/push_rule`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에 설정된 push 규칙을 반환한다. 그룹 수준의 push 규칙과 달리 `project_id` 필드가 추가로 포함된다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---:|---|
| `id` | `any` | Y | 프로젝트 ID 또는 URL 인코딩된 프로젝트 경로 |

### Response
#### `200 OK`
```json
{
  "id": "integer",
  "project_id": "integer",
  "created_at": "string",
  "commit_message_regex": "string",
  "commit_message_negative_regex": "string",
  "branch_name_regex": "string",
  "deny_delete_tag": "boolean",
  "member_check": "boolean",
  "prevent_secrets": "boolean",
  "author_email_regex": "string",
  "file_name_regex": "string",
  "max_file_size": "integer",
  "commit_committer_check": "boolean",
  "commit_committer_name_check": "boolean",
  "reject_unsigned_commits": "boolean",
  "reject_non_dco_commits": "boolean"
}
```

| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | `integer` | push 규칙 ID |
| `project_id` | `integer` | 적용 프로젝트 ID |
| `created_at` | `string` (datetime) | 생성 일시 |
| `commit_message_regex` | `string` | 커밋 메시지 허용 정규식 |
| `commit_message_negative_regex` | `string` | 커밋 메시지 금지 정규식 |
| `branch_name_regex` | `string` | 브랜치 이름 허용 정규식 |
| `deny_delete_tag` | `boolean` | 태그 삭제 금지 여부 |
| `member_check` | `boolean` | 멤버 확인 여부 |
| `prevent_secrets` | `boolean` | Secret 파일 push 금지 여부 |
| `author_email_regex` | `string` | 작성자 이메일 허용 정규식 |
| `file_name_regex` | `string` | 파일 이름 금지 정규식 |
| `max_file_size` | `integer` | 최대 파일 크기 (MB) |
| `commit_committer_check` | `boolean` | 커밋 작성자 = push 사용자 일치 확인 여부 |
| `commit_committer_name_check` | `boolean` | 커밋 작성자명 확인 여부 |
| `reject_unsigned_commits` | `boolean` | 서명되지 않은 커밋 거부 여부 |
| `reject_non_dco_commits` | `boolean` | DCO 서명되지 않은 커밋 거부 여부 |

### Errors
| 상태 코드 | 설명 |
|---|---:|
| `400 Bad Request` | 요청 파라미터 오류 |
| `404 Not Found` | 프로젝트를 찾을 수 없음 |
