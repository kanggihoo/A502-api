# 20-보드(Boards) API 명세

## 02-List all group issue boards in a group

## 기본 정보
- **기능:** 특정 그룹의 모든 이슈 보드를 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/boards`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 그룹의 모든 이슈 보드 목록을 반환한다. 각 보드는 프로젝트 정보, 리스트(레이블/마일스톤/이터레이션), 그룹 정보 등을 포함한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | string | Y | 그룹 ID | `6789` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|---:|
| `id` | integer | 보드 ID |
| `name` | string | 보드 이름 |
| `hide_backlog_list` | boolean | 백로그 리스트 숨김 여부 |
| `hide_closed_list` | boolean | 닫힌 리스트 숨김 여부 |
| `project` | object | 연결된 프로젝트 정보 |
| `lists` | array[object] | 보드 리스트 목록 (레이블/마일스톤/이터레이션 기반) |
| `group` | object | 그룹 정보 |
| `milestone` | object | 마일스톤 필터 |
| `assignee` | object | 담당자 필터 |
| `labels` | object | 레이블 필터 |
| `weight` | integer | 가중치 필터 |

JSON 예시:
```json
[
  {
    "id": 1,
    "name": "Development Board",
    "hide_backlog_list": false,
    "hide_closed_list": false,
    "project": {
      "id": 1234,
      "name": "My Project",
      "name_with_namespace": "Group / My Project",
      "path_with_namespace": "group/my-project",
      "web_url": "https://gitlab.example.com/group/my-project"
    },
    "lists": [
      {
        "id": 1,
        "label": {
          "id": 1,
          "name": "To Do",
          "color": "#FF0000",
          "description": "Tasks to do"
        },
        "position": 0
      }
    ],
    "group": {
      "id": 6789,
      "name": "Group",
      "web_url": "https://gitlab.example.com/groups/group"
    }
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 그룹을 찾을 수 없음 |

---

## 11-List all project issue boards

## 기본 정보
- **기능:** 특정 프로젝트의 모든 이슈 보드를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/boards`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트의 모든 이슈 보드 목록을 반환한다.

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
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
Group issue boards와 동일한 응답 스키마를 사용한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 13-Retrieve an issue board

## 기본 정보
- **기능:** 특정 프로젝트의 단일 이슈 보드를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/boards/{board_id}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트에서 특정 보드의 상세 정보를 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `board_id` | integer | Y | 보드 ID | `1` |

## Response
### `200 OK`
List project issue boards와 동일한 응답 스키마를 사용한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 보드를 찾을 수 없음 |

---

## 16-List all board lists in an issue board

## 기본 정보
- **기능:** 특정 이슈 보드의 모든 리스트를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/boards/{board_id}/lists`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 이슈 보드의 모든 리스트 목록을 반환한다. `open` 및 `closed` 리스트는 포함되지 않는다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `board_id` | integer | Y | 보드 ID | `1` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|---:|
| `id` | integer | 리스트 ID |
| `label` | object | 연결된 레이블 정보 (id, name, color 등) |
| `position` | integer | 리스트 위치 순서 |
| `milestone` | object | 연결된 마일스톤 정보 |
| `iteration` | object | 연결된 이터레이션 정보 |
| `assignee` | object | 연결된 담당자 정보 |
| `max_issue_count` | integer | 최대 이슈 개수 제한 |
| `max_issue_weight` | integer | 최대 이슈 가중치 제한 |
| `limit_metric` | string | 제한 메트릭 (`issue_count` 또는 `issue_weight`) |

JSON 예시:
```json
[
  {
    "id": 1,
    "label": {
      "id": 1,
      "name": "To Do",
      "description": "Tasks to do",
      "text_color": "#FFFFFF",
      "color": "#FF0000",
      "archived": false
    },
    "position": 0,
    "max_issue_count": 0,
    "max_issue_weight": 0,
    "limit_metric": null
  },
  {
    "id": 2,
    "label": {
      "id": 2,
      "name": "In Progress",
      "color": "#0000FF",
      "archived": false
    },
    "position": 1,
    "max_issue_count": 5,
    "max_issue_weight": 20,
    "limit_metric": "issue_count"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 보드를 찾을 수 없음 |
