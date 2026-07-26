# 1. List channel views

## 기본 정보
- **기능**: 채널의 view 목록을 조회한다.
- **Endpoint**: `GET /api/v4/channels/{channel_id}/views`
- **인증**: Bearer Token 필요
- **권한**: `read_channel_content` (해당 채널)

## 설명
채널에 등록된 view들의 목록을 페이지 단위로 조회하는 API이다. Experimental 기능으로 향후 변경되거나 제거될 수 있다. 최소 서버 버전은 11.6이다. `include_total_count`를 true로 주면 views 배열과 total_count를 포함한 객체가, 아니면 View 객체 배열이 반환된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| per_page | integer | No | 60 | 페이지당 view 수 (최대 200) |
| page | integer | No | 0 | 0부터 시작하는 페이지 번호 |
| include_total_count | boolean | No | false | true면 views 배열 + total_count를 담은 ViewsWithCount 객체 반환, false/생략 시 View 배열 반환 |

## Response

### 200 - Channel views retrieval successful
응답 스키마는 `include_total_count` 값에 따라 달라진다 (View 배열 또는 ViewsWithCount 객체).

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

## 주의 사항
Experimental endpoint로 향후 릴리스에서 변경/제거될 수 있다.

---

# 2. Create channel view

## 기본 정보
- **기능**: 채널에 새 view를 생성한다.
- **Endpoint**: `POST /api/v4/channels/{channel_id}/views`
- **인증**: Bearer Token 필요
- **권한**: `create_post` (해당 채널)

## 설명
채널에 새로운 view(현재 kanban 타입)를 생성하는 API이다. Experimental 기능이며 최소 서버 버전은 11.6이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| title | string | Yes | view의 제목 |
| type | enum("kanban") | Yes | view 타입 (`kanban`: 칸반 view) |
| description | string | No | view 설명 |
| sort_order | integer | No | 채널 내 view의 표시 순서 |
| props | object | No | view의 임의 key-value 속성 |

```json
{
  "title": "string",
  "type": "kanban",
  "description": "string",
  "sort_order": 0,
  "props": {}
}
```

## Response

### 201 - Channel view creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | view의 고유 식별자 |
| channel_id | string | view가 속한 채널 ID |
| type | enum("kanban") | view 타입 |
| creator_id | string | view를 생성한 사용자 ID |
| title | string | view 제목 |
| description | string | view 설명 |
| sort_order | integer | 채널 내 표시 순서 |
| props | object | 임의 key-value 속성 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

## 주의 사항
Experimental endpoint로 향후 릴리스에서 변경/제거될 수 있다.

---

# 3. Get a channel view

## 기본 정보
- **기능**: view ID로 단일 view를 조회한다.
- **Endpoint**: `GET /api/v4/channels/{channel_id}/views/{view_id}`
- **인증**: Bearer Token 필요
- **권한**: `read_channel_content` (해당 채널)

## 설명
채널의 특정 view를 ID로 조회하는 API이다. Experimental 기능이며 최소 서버 버전은 11.6이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| view_id | string | Yes | view GUID |

## Response

### 200 - Channel view retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | view의 고유 식별자 |
| channel_id | string | view가 속한 채널 ID |
| type | enum("kanban") | view 타입 |
| creator_id | string | view를 생성한 사용자 ID |
| title | string | view 제목 |
| description | string | view 설명 |
| sort_order | integer | 채널 내 표시 순서 |
| props | object | 임의 key-value 속성 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

## 주의 사항
Experimental endpoint로 향후 릴리스에서 변경/제거될 수 있다.

---

# 4. Update a channel view

## 기본 정보
- **기능**: 채널 view를 부분 수정한다.
- **Endpoint**: `PATCH /api/v4/channels/{channel_id}/views/{view_id}`
- **인증**: Bearer Token 필요
- **권한**: `create_post` (해당 채널)

## 설명
수정하려는 필드만 보내서 채널 view를 부분 업데이트하는 API이다. 생략한 필드는 변경되지 않는다. Experimental 기능이며 최소 서버 버전은 11.6이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| view_id | string | Yes | view GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| title | string | No | view 제목 |
| description | string | No | view 설명 |
| sort_order | integer | No | 채널 내 표시 순서 |
| props | object | No | 임의 key-value 속성 |

```json
{
  "title": "string",
  "description": "string",
  "sort_order": 0,
  "props": {}
}
```

## Response

### 200 - Channel view update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | view의 고유 식별자 |
| channel_id | string | view가 속한 채널 ID |
| type | enum("kanban") | view 타입 |
| creator_id | string | view를 생성한 사용자 ID |
| title | string | view 제목 |
| description | string | view 설명 |
| sort_order | integer | 채널 내 표시 순서 |
| props | object | 임의 key-value 속성 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

## 주의 사항
Experimental endpoint로 향후 릴리스에서 변경/제거될 수 있다.

---

# 5. Delete a channel view

## 기본 정보
- **기능**: 채널 view를 삭제(soft delete)한다.
- **Endpoint**: `DELETE /api/v4/channels/{channel_id}/views/{view_id}`
- **인증**: Bearer Token 필요
- **권한**: `create_post` (해당 채널)

## 설명
채널 view를 soft-delete하는 API로, `delete_at`을 현재 타임스탬프로 설정한다. Experimental 기능이며 최소 서버 버전은 11.6이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| view_id | string | Yes | view GUID |

## Response

### 200 - Channel view deletion successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청 성공 시 "ok" 반환 |

```json
{ "status": "ok" }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

## 주의 사항
Soft delete 방식이며, Experimental endpoint로 향후 릴리스에서 변경/제거될 수 있다.

---

# 6. Get posts for a view

## 기본 정보
- **기능**: 특정 view에 속한 게시물 목록을 조회한다.
- **Endpoint**: `GET /api/v4/channels/{channel_id}/views/{view_id}/posts`
- **인증**: Bearer Token 필요
- **권한**: `read_channel_content` (해당 채널)

## 설명
특정 view에 속한 게시물들을 페이지 단위로 조회하는 API이다. Experimental 기능이며 최소 서버 버전은 11.6이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| view_id | string | Yes | view GUID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | 0 | 0부터 시작하는 페이지 번호 |
| per_page | integer | No | 60 | 페이지당 게시물 수 (최대 200) |

## Response

### 200 - Post list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| order | string[] | 게시물 ID 순서 배열 |
| posts | object | 게시물 객체 맵 |
| next_post_id | string | 다음 게시물 ID |
| prev_post_id | string | 이전 게시물 ID |
| has_next | boolean | 이 페이지 이후 항목이 더 있는지 여부 |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

## 주의 사항
Experimental endpoint로 향후 릴리스에서 변경/제거될 수 있다.

---

# 7. Update a channel view's sort order

## 기본 정보
- **기능**: 채널 view의 정렬 순서를 변경한다.
- **Endpoint**: `POST /api/v4/channels/{channel_id}/views/{view_id}/sort_order`
- **인증**: Bearer Token 필요
- **권한**: `create_post` (해당 채널)

## 설명
채널 view의 정렬 순서를 request body의 새 index로 설정하고, 변경에 맞춰 채널 내 나머지 view들의 순서도 함께 갱신하는 API이다. Experimental 기능이며 최소 서버 버전은 11.6이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| view_id | string | Yes | view GUID |

### Body
새 정렬 index를 나타내는 integer 값 하나를 그대로 전송한다.

```json
0
```

## Response

### 200 - Channel view sort order update successful
갱신된 View 객체 배열을 반환한다.

| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | view의 고유 식별자 |
| channel_id | string | view가 속한 채널 ID |
| type | enum("kanban") | view 타입 |
| creator_id | string | view를 생성한 사용자 ID |
| title | string | view 제목 |
| description | string | view 설명 |
| sort_order | integer | 채널 내 표시 순서 |
| props | object | 임의 key-value 속성 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

## 주의 사항
Experimental endpoint로 향후 릴리스에서 변경/제거될 수 있다.

---
