# 1. Create a custom emoji

## 기본 정보
- **기능**: 팀용 커스텀 이모지를 생성한다.
- **Endpoint**: `POST /api/v4/emoji`
- **인증**: Bearer Token 필요
- **권한**: 인증만 필요 (실측 권한 `create_emojis` 보유)

## 설명
커스텀 이모지를 생성하는 API이다. multipart/form-data로 이미지 파일과 이모지 메타데이터(JSON)를 함께 전송한다.

## Request

### Headers
Content-Type: multipart/form-data

### Body (multipart/form-data)
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| image | file | Yes | 업로드할 이미지 파일 |
| emoji | string | Yes | 이모지 이름(`name`)과 인증된 사용자 ID(`creator_id`)를 담은 JSON 객체 |

## Response

### 201 - Emoji creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 이모지 ID |
| creator_id | string | 이모지를 만든 사용자 ID |
| name | string | 이모지 이름 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 413 | 요청 본문이 너무 큼 |
| 501 | 기능 미구현/비활성화 |

---

# 2. Get a list of custom emoji

## 기본 정보
- **기능**: 시스템의 커스텀 이모지 메타데이터를 페이지 단위로 조회한다.
- **Endpoint**: `GET /api/v4/emoji`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
시스템에 등록된 커스텀 이모지의 메타데이터를 페이지 단위로 조회하는 API이다. 서버 버전 4.7부터 `sort` query parameter로 정렬할 수 있다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 조회할 페이지 |
| per_page | integer | No | - | 페이지당 이모지 수 |
| sort | string | No | (빈 값) | 빈 값이면 정렬 없음, "name"이면 이모지 이름 기준 정렬 (최소 서버 버전 4.7) |

## Response

### 200 - Emoji list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 이모지 ID |
| creator_id | string | 이모지를 만든 사용자 ID |
| name | string | 이모지 이름 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능 미구현/비활성화 |

---

# 3. Get a custom emoji

## 기본 정보
- **기능**: 커스텀 이모지의 메타데이터를 조회한다.
- **Endpoint**: `GET /api/v4/emoji/{emoji_id}`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
이모지 ID로 커스텀 이모지의 메타데이터를 조회하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| emoji_id | string | Yes | 이모지 GUID |

## Response

### 200 - Emoji retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 이모지 ID |
| creator_id | string | 이모지를 만든 사용자 ID |
| name | string | 이모지 이름 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 이모지 없음 |
| 501 | 기능 미구현/비활성화 |

---

# 4. Delete a custom emoji

## 기본 정보
- **기능**: 커스텀 이모지를 삭제한다.
- **Endpoint**: `DELETE /api/v4/emoji/{emoji_id}`
- **인증**: Bearer Token 필요
- **권한**: 본인이 생성한 이모지 (또는 `manage_team`/`manage_system` — 미보유)

## 설명
커스텀 이모지를 삭제하는 API이다. `manage_team` 또는 `manage_system` 권한이 있거나, 해당 이모지를 생성한 사용자 본인이어야 한다. 일반 멤버 계정은 본인이 생성한 이모지만 삭제할 수 있다 (실측 권한 `delete_emojis` 보유).

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| emoji_id | string | Yes | 이모지 GUID |

## Response

### 200 - Emoji delete successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 이모지 ID |
| creator_id | string | 이모지를 만든 사용자 ID |
| name | string | 이모지 이름 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능 미구현/비활성화 |

## 주의 사항
일반 멤버 계정은 본인이 생성한 이모지만 삭제 가능하다.

---

# 5. Get a custom emoji by name

## 기본 정보
- **기능**: 이름으로 커스텀 이모지의 메타데이터를 조회한다.
- **Endpoint**: `GET /api/v4/emoji/name/{emoji_name}`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
이모지 이름으로 커스텀 이모지의 메타데이터를 조회하는 API이다. 최소 서버 버전은 4.7이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| emoji_name | string | Yes | 이모지 이름 |

## Response

### 200 - Emoji retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 이모지 ID |
| creator_id | string | 이모지를 만든 사용자 ID |
| name | string | 이모지 이름 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 404 | 이모지 없음 |
| 501 | 기능 미구현/비활성화 |

---

# 6. Get custom emoji image

## 기본 정보
- **기능**: 커스텀 이모지의 이미지를 가져온다.
- **Endpoint**: `GET /api/v4/emoji/{emoji_id}/image`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
커스텀 이모지의 이미지 파일을 조회하는 API이다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| emoji_id | string | Yes | 이모지 GUID |

## Response

### 200 - Emoji image retrieval successful
이모지 이미지가 반환된다.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 이모지 없음 |
| 500 | 서버 오류 |
| 501 | 기능 미구현/비활성화 |

---

# 7. Search custom emoji

## 기본 정보
- **기능**: 이름 기준으로 커스텀 이모지를 검색한다.
- **Endpoint**: `POST /api/v4/emoji/search`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
Request body의 검색 조건으로 커스텀 이모지를 이름 기준으로 검색하는 API이다. 최대 200개의 결과가 반환된다. 최소 서버 버전은 4.7이다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| term | string | Yes | 이모지 이름과 매칭할 검색어 |
| prefix_only | string | No | 설정 시 검색어로 시작하는 이름만 검색 |

```json
{
  "term": "string",
  "prefix_only": "string"
}
```

## Response

### 200 - Emoji list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 이모지 ID |
| creator_id | string | 이모지를 만든 사용자 ID |
| name | string | 이모지 이름 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능 미구현/비활성화 |

---

# 8. Autocomplete custom emoji

## 기본 정보
- **기능**: 입력한 이름으로 시작하거나 일치하는 커스텀 이모지를 자동완성 조회한다.
- **Endpoint**: `GET /api/v4/emoji/autocomplete`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
제공한 이름으로 시작하거나 일치하는 커스텀 이모지 목록을 조회하는 API이다. 최대 100개의 결과가 반환된다. 최소 서버 버전은 4.7이다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| name | string | Yes | - | 검색할 이모지 이름 |

## Response

### 200 - Emoji list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 이모지 ID |
| creator_id | string | 이모지를 만든 사용자 ID |
| name | string | 이모지 이름 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 마지막 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 501 | 기능 미구현/비활성화 |

---

# 9. Get custom emojis by name

## 기본 정보
- **기능**: 이모지 이름 목록으로 커스텀 이모지들을 조회한다.
- **Endpoint**: `POST /api/v4/emoji/names`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
제공한 이모지 이름 목록을 기반으로 커스텀 이모지 목록을 조회하는 API이다. 최대 200개의 결과가 반환된다. 최소 서버 버전은 9.2이다.

## Request

### Body
이모지 이름 문자열 배열을 전송한다.

```json
[
  "string"
]
```

## Response

### 200 - Emoji list retrieval successful
객체 배열이 반환된다. (원본 문서의 응답 스키마에는 id, create_at, update_at, delete_at, username, notify_props, timezone 등 사용자 형태의 필드가 나열되어 있다.)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 501 | 기능 미구현/비활성화 |

---
