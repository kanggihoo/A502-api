# 1. Get channel bookmarks for Channel

## 기본 정보
- **기능**: 특정 채널의 채널 북마크 목록을 조회한다.
- **Endpoint**: `GET /api/v4/channels/{channel_id}/bookmarks`
- **인증**: Bearer Token 필요
- **권한**: 없음 (문서에 Permissions 서술 없음, 채널 멤버 조회 성격)

## 설명
채널의 북마크 목록을 조회한다. `bookmarks_since` 쿼리 파라미터를 지정하면 해당 시각 이후 추가·수정·삭제된 북마크만 반환한다. 최소 서버 버전 9.5.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| bookmarks_since | number | No | - | 필터 기준 타임스탬프. 지정 시 그 이후 추가/수정/삭제된 북마크를 반환 |

## Response

### 200 - Channel Bookmarks retrieval successful
북마크 객체 배열을 반환한다.

```json
[
  any
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 2. Create channel bookmark

## 기본 정보
- **기능**: 채널에 새 채널 북마크를 생성한다.
- **Endpoint**: `POST /api/v4/channels/{channel_id}/bookmarks`
- **인증**: Bearer Token 필요
- **권한**: `add_bookmark_public_channel` 또는 `add_bookmark_private_channel` (채널 유형에 따름). DM/GM 채널은 비게스트 멤버이면 가능

## 설명
해당 채널에 새 북마크를 생성한다. `type`이 `link`이면 `link_url`이, `file`이면 `file_id`가 필수이다. 최소 서버 버전 9.5.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| display_name | string | Yes | 북마크 이름 |
| type | enum("link"\|"file") | Yes | `link`: 링크 참조(`link_url` 필수), `file`: 파일 참조(`file_id` 필수) |
| file_id | string | No | 북마크에 연결된 파일 ID (`file` 타입일 때 필수) |
| link_url | string | No | 북마크에 연결된 URL (`link` 타입일 때 필수) |
| image_url | string | No | 북마크에 연결된 이미지 URL (`link` 타입에서만 선택 사용) |
| emoji | string | No | 북마크의 이모지 |

```json
{
  "display_name": "string",
  "type": "link",
  "link_url": "string",
  "image_url": "string",
  "emoji": "string"
}
```

## Response

### 201 - Channel Bookmark creation successful
생성된 북마크 객체를 반환한다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 3. Update channel bookmark

## 기본 정보
- **기능**: 채널 북마크를 부분 수정(patch)한다.
- **Endpoint**: `PATCH /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}`
- **인증**: Bearer Token 필요
- **권한**: `edit_bookmark_public_channel` 또는 `edit_bookmark_private_channel` (채널 유형에 따름). DM/GM 채널은 비게스트 멤버이면 가능

## 설명
수정할 필드만 담아 보내는 부분 업데이트 방식이다. 생략한 필드는 변경되지 않으며, 본문에 정의되지 않은 필드는 무시된다. 최소 서버 버전 9.5.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| bookmark_id | string | Yes | 북마크 GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| display_name | string | No | 북마크 이름 |
| sort_order | integer | No | 북마크 정렬 순서 |
| type | enum("link"\|"file") | No | `link`: 링크 참조(`link_url` 필수), `file`: 파일 참조(`file_id` 필수) |
| file_id | string | No | 북마크에 연결된 파일 ID (`file` 타입일 때 필수) |
| link_url | string | No | 북마크에 연결된 URL (`link` 타입일 때 필수) |
| image_url | string | No | 북마크에 연결된 이미지 URL |
| emoji | string | No | 북마크의 이모지 |

## Response

### 200 - Channel Bookmark update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| updated | any | 갱신된 북마크 |
| deleted | any | 삭제 처리된 북마크 |

```json
{
  "updated": {},
  "deleted": {}
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 4. Delete channel bookmark

## 기본 정보
- **기능**: 채널 북마크를 삭제(아카이브)한다.
- **Endpoint**: `DELETE /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}`
- **인증**: Bearer Token 필요
- **권한**: `delete_bookmark_public_channel` 또는 `delete_bookmark_private_channel` (채널 유형에 따름). DM/GM 채널은 비게스트 멤버이면 가능

## 설명
북마크를 아카이브한다. 실제로는 데이터베이스에서 `deleteAt`을 현재 타임스탬프로 설정하는 soft delete 방식이다. 최소 서버 버전 9.5.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| bookmark_id | string | Yes | 북마크 GUID |

## Response

### 200 - Channel Bookmark deletion successful
삭제된 북마크 객체를 반환한다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 5. Update channel bookmark's order

## 기본 정보
- **기능**: 채널 북마크의 정렬 순서를 변경한다.
- **Endpoint**: `POST /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}/sort_order`
- **인증**: Bearer Token 필요
- **권한**: `order_bookmark_public_channel` 또는 `order_bookmark_private_channel` (채널 유형에 따름). DM/GM 채널은 비게스트 멤버이면 가능

## 설명
지정한 북마크의 새 정렬 순서를 설정하고, 이에 맞추어 채널의 나머지 북마크 순서도 함께 조정한다. 최소 서버 버전 9.5.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |
| bookmark_id | string | Yes | 북마크 GUID |

### Body
새 정렬 순서 값 (number)

```json
0
```

## Response

### 200 - Channel Bookmark Sort Order update successful
채널의 북마크 배열을 반환한다.

```json
[
  any
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
