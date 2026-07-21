# 46-디스커션(Discussions) API 명세

## 01-Get a list of issue discussions

## 기본 정보
- **기능:** 특정 이슈의 모든 디스커션(토론 스레드)을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/issues/{noteable_id}/discussions`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 이슈에 달린 모든 디스커션(댓글 스레드) 목록을 반환한다. 각 디스커션은 개별 노트 또는 스레드 노트를 포함한다.

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
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|---:|
| `id` | string | 디스커션 ID |
| `individual_note` | boolean | 개별 노트 여부 |
| `resolvable` | boolean | 해결 가능 여부 |
| `resolved` | boolean | 해결 여부 |
| `notes` | array[object] | 디스커션에 포함된 노트 목록 |

notes 항목:
| 필드 | 타입 | 설명 |
|---|---:|---|---:|
| `id` | integer | 노트 ID |
| `type` | string | 노트 타입 (`DiscussionNote`, `DiffNote` 등) |
| `body` | string | 노트 본문 |
| `author` | object | 작성자 정보 (id, username, name, avatar_url, web_url 등) |
| `created_at` | string | 생성 일시 |
| `updated_at` | string | 업데이트 일시 |
| `system` | boolean | 시스템 노트 여부 |
| `noteable_id` | integer | 대상 객체 ID |
| `noteable_type` | string | 대상 객체 타입 (`Issue`, `MergeRequest`, `Commit`) |
| `project_id` | integer | 프로젝트 ID |
| `commit_id` | string | 커밋 ID |
| `position` | object | diff 위치 정보 |
| `resolvable` | boolean | 해결 가능 여부 |
| `resolved` | boolean | 해결 여부 |
| `resolved_by` | object | 해결한 사용자 정보 |
| `resolved_at` | string | 해결 일시 |
| `confidential` | boolean | 비밀 노트 여부 |
| `internal` | boolean | 내부 노트 여부 |
| `imported` | boolean | 가져오기된 노트 여부 |
| `imported_from` | string | 가져온 소스 |
| `noteable_iid` | integer | 대상 객체 IID |
| `commands_changes` | object | 명령어 변경 사항 |

JSON 예시:
```json
[
  {
    "id": "abc123",
    "individual_note": true,
    "resolvable": false,
    "resolved": false,
    "notes": [
      {
        "id": 1,
        "type": null,
        "body": "This is a comment",
        "author": {
          "id": 1,
          "username": "john",
          "name": "John Doe",
          "state": "active",
          "avatar_url": "https://gitlab.example.com/uploads/-/system/user/avatar/1/avatar.png",
          "web_url": "https://gitlab.example.com/john"
        },
        "created_at": "2025-01-01T00:00:00.000+09:00",
        "updated_at": "2025-01-01T00:00:00.000+09:00",
        "system": false,
        "noteable_id": 42,
        "noteable_type": "Issue",
        "project_id": 1234,
        "resolvable": false,
        "resolved": false,
        "confidential": false,
        "internal": false,
        "imported": false
      }
    ]
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 이슈를 찾을 수 없음 |

---

## 18-Get a list of merge request discussions

## 기본 정보
- **기능:** 특정 Merge Request의 모든 디스커션을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{noteable_id}/discussions`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 Merge Request에 달린 모든 디스커션 목록을 반환한다.

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
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
Issue Discussions와 동일한 응답 스키마를 사용한다. (`noteable_type`이 `MergeRequest`로 표시됨)

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - Merge Request를 찾을 수 없음 |

---

## 27-Get a list of commit discussions

## 기본 정보
- **기능:** 특정 커밋의 모든 디스커션을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{noteable_id}/discussions`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 커밋에 달린 모든 디스커션 목록을 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | string | Y | 프로젝트 ID | `1234` |
| `noteable_id` | string | Y | 커밋 SHA | `9b7d3c3...` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
Issue Discussions와 동일한 응답 스키마를 사용한다. (`noteable_type`이 `Commit`으로 표시됨)

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 커밋을 찾을 수 없음 |
