# 84-레이블(Labels) API 명세

## 01-List all project labels

## 기본 정보
- **기능:** 특정 프로젝트의 모든 레이블을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/labels`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트의 모든 레이블 목록을 반환한다. 기본적으로 페이지당 20개 결과를 반환하며, 상위 그룹 레이블 포함, 검색, 아카이브 필터링 옵션을 제공한다.

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
| `with_counts` | boolean | N | 이슈 및 MR 개수 포함 여부 |
| `include_ancestor_groups` | boolean | N | 상위 그룹 레이블 포함 여부 |
| `search` | string | N | 레이블 검색 키워드 (GitLab 13.6+) |
| `archived` | boolean | N | 아카이브 상태로 필터링 (GitLab 18.10+) |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | integer | 레이블 ID | `1` |
| `name` | string | 레이블명 | `bug` |
| `description` | string | 레이블 설명 | `Bug report` |
| `text_color` | string | 텍스트 색상 | `#FFFFFF` |
| `description_html` | string | HTML 렌더링된 설명 | `<p>Bug report</p>` |
| `color` | string | 배경 색상 | `#FF0000` |
| `archived` | boolean | 아카이브 여부 | `false` |
| `open_issues_count` | integer | 열린 이슈 수 | `5` |
| `closed_issues_count` | integer | 닫힌 이슈 수 | `3` |
| `open_merge_requests_count` | integer | 열린 MR 수 | `2` |
| `subscribed` | boolean | 구독 여부 | `false` |
| `priority` | integer | 우선순위 | `1` |
| `is_project_label` | boolean | 프로젝트 레이블 여부 | `true` |

JSON 예시:
```json
[
  {
    "id": 1,
    "name": "bug",
    "description": "Bug report",
    "text_color": "#FFFFFF",
    "description_html": "<p>Bug report</p>",
    "color": "#FF0000",
    "archived": false,
    "open_issues_count": 5,
    "closed_issues_count": 3,
    "open_merge_requests_count": 2,
    "subscribed": false,
    "priority": 1,
    "is_project_label": true
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 05-Retrieve a project label

## 기본 정보
- **기능:** 특정 프로젝트의 단일 레이블을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/labels/{name}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트에서 특정 레이블을 이름 또는 ID로 조회한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `name` | string | Y | 레이블 이름 또는 ID | `bug` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `include_ancestor_groups` | boolean | N | 상위 그룹 레이블 포함 여부 |

## Response
### `200 OK`
List project labels와 동일한 응답 스키마를 사용한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 레이블을 찾을 수 없음 |

---

## 10-List all group labels

## 기본 정보
- **기능:** 특정 그룹의 모든 그룹 레이블을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/labels`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 그룹의 모든 그룹 레이블 목록을 반환한다. 상위/하위 그룹 레이블 포함, 그룹 레이블만 표시, 검색 등 다양한 필터링 옵션을 제공한다.

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
| `with_counts` | boolean | N | 이슈 및 MR 개수 포함 여부 |
| `include_ancestor_groups` | boolean | N | 상위 그룹 레이블 포함 여부 |
| `include_descendant_groups` | boolean | N | 하위 그룹 레이블 포함 여부 (GitLab 13.6+) |
| `only_group_labels` | boolean | N | 그룹 레이블만 표시 (GitLab 13.6+) |
| `search` | string | N | 레이블 검색 키워드 (GitLab 13.6+) |
| `archived` | boolean | N | 아카이브 상태로 필터링 (GitLab 18.10+) |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | integer | 레이블 ID | `1` |
| `name` | string | 레이블명 | `bug` |
| `description` | string | 레이블 설명 | `Bug report` |
| `text_color` | string | 텍스트 색상 | `#FFFFFF` |
| `description_html` | string | HTML 렌더링된 설명 | `<p>Bug report</p>` |
| `color` | string | 배경 색상 | `#FF0000` |
| `archived` | boolean | 아카이브 여부 | `false` |
| `open_issues_count` | integer | 열린 이슈 수 | `5` |
| `closed_issues_count` | integer | 닫힌 이슈 수 | `3` |
| `open_merge_requests_count` | integer | 열린 MR 수 | `2` |
| `subscribed` | boolean | 구독 여부 | `false` |

JSON 예시:
```json
[
  {
    "id": 1,
    "name": "bug",
    "description": "Bug report",
    "text_color": "#FFFFFF",
    "description_html": "<p>Bug report</p>",
    "color": "#FF0000",
    "archived": false,
    "open_issues_count": 5,
    "closed_issues_count": 3,
    "open_merge_requests_count": 2,
    "subscribed": false
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 그룹을 찾을 수 없음 |
