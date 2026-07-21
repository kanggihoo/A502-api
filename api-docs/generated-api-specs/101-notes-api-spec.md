# 101-노트(Notes) API 명세

## 01-Get a list of issue notes

## 기본 정보
- **기능:** 특정 이슈의 모든 노트(댓글)를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/issues/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 이슈에 달린 모든 노트(댓글) 목록을 반환한다. 생성일 또는 업데이트일 기준 정렬이 가능하다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | string | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | 이슈 ID | `42` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `order_by` | string | N | 정렬 기준 (`created_at` 또는 `updated_at`) |
| `sort` | string | N | 정렬 방향 (`asc` 또는 `desc`) |
| `activity_filter` | string | N | 반환할 notable 유형 필터 |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | integer | 노트 ID | `1` |
| `type` | string | 노트 타입 | `null` 또는 `DiscussionNote` |
| `body` | string | 노트 본문 | `LGTM!` |
| `author` | object | 작성자 정보 | `{"id": 1, "username": "john", ...}` |
| `created_at` | string | 생성 일시 | `2025-01-01T00:00:00.000+09:00` |
| `updated_at` | string | 업데이트 일시 | `2025-01-01T00:00:00.000+09:00` |
| `system` | boolean | 시스템 노트 여부 | `false` |
| `noteable_id` | integer | 대상 객체 ID | `42` |
| `noteable_type` | string | 대상 객체 타입 | `Issue` |
| `project_id` | integer | 프로젝트 ID | `1234` |
| `commit_id` | string | 커밋 ID | `null` |
| `position` | object | diff 위치 정보 | `{}` |
| `resolvable` | boolean | 해결 가능 여부 | `false` |
| `resolved` | boolean | 해결 여부 | `false` |
| `resolved_by` | object | 해결한 사용자 정보 | `null` |
| `resolved_at` | string | 해결 일시 | `null` |
| `confidential` | boolean | 비밀 노트 여부 | `false` |
| `internal` | boolean | 내부 노트 여부 | `false` |
| `imported` | boolean | 가져오기된 노트 여부 | `false` |
| `imported_from` | string | 가져온 소스 | `null` |
| `noteable_iid` | integer | 대상 객체 IID | `1` |
| `commands_changes` | object | 명령어 변경 사항 | `{}` |

JSON 예시:
```json
[
  {
    "id": 1,
    "type": null,
    "body": "This is a great issue!",
    "author": {
      "id": 1,
      "username": "john",
      "public_email": "john@example.com",
      "name": "John Doe",
      "state": "active",
      "locked": false,
      "avatar_url": "https://gitlab.example.com/uploads/-/system/user/avatar/1/avatar.png",
      "web_url": "https://gitlab.example.com/john"
    },
    "created_at": "2025-01-01T00:00:00.000+09:00",
    "updated_at": "2025-01-01T00:00:00.000+09:00",
    "system": false,
    "noteable_id": 42,
    "noteable_type": "Issue",
    "project_id": 1234,
    "commit_id": null,
    "position": {},
    "resolvable": false,
    "resolved": false,
    "confidential": false,
    "internal": false,
    "imported": false,
    "imported_from": null,
    "noteable_iid": 1,
    "commands_changes": {}
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 이슈를 찾을 수 없음 |

---

## 06-Get a list of merge request notes

## 기본 정보
- **기능:** 특정 Merge Request의 모든 노트(댓글)를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{noteable_id}/notes`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 Merge Request에 달린 모든 노트(댓글) 목록을 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | string | Y | 프로젝트 ID | `1234` |
| `noteable_id` | integer | Y | Merge Request ID | `42` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `order_by` | string | N | 정렬 기준 (`created_at` 또는 `updated_at`) |
| `sort` | string | N | 정렬 방향 (`asc` 또는 `desc`) |
| `activity_filter` | string | N | 반환할 notable 유형 필터 |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
Issue Notes와 동일한 응답 스키마를 사용한다. (`noteable_type`이 `MergeRequest`로 표시됨)

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - Merge Request를 찾을 수 없음 |
