# 2. Get an upload session

## 기본 정보
- **기능**: 이전에 생성된 업로드 세션 정보를 조회한다.
- **Endpoint**: `GET /api/v4/uploads/{upload_id}`
- **인증**: Bearer Token 필요
- **권한**: 업로드 세션을 생성한 사용자 본인이어야 함 (별도의 이름있는 권한 불요)

## 설명
이전에 생성된 업로드 세션을 조회한다. 업로드 세션을 생성한 사용자 본인으로 로그인되어 있어야 조회할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| upload_id | string | Yes | 조회할 업로드 세션의 ID |

## Response

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 3. Perform a file upload

## 기본 정보
- **기능**: 파일 업로드를 시작하거나 중단된 업로드를 재개한다.
- **Endpoint**: `POST /api/v4/uploads/{upload_id}`
- **인증**: Bearer Token 필요
- **권한**: 업로드 세션을 생성한 사용자 본인이어야 함 (별도의 이름있는 권한 불요)

## 설명
파일 업로드를 시작하거나, 완료되지 않은 기존 업로드를 재개한다. 업로드를 재개하는 경우 업로드 세션 객체에 명시된 offset부터 데이터를 전송해야 한다. 요청 본문은 바이너리 파일 내용을 스트리밍하는 방식과 multipart/form-data 방식 중 하나를 사용할 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| upload_id | string | Yes | 업로드할 데이터가 속한 업로드 세션의 ID |

### Body
application/octet-stream 형식의 바이너리 파일 데이터 (string으로 표현됨)

```json
"string"
```

## Response

### 201 - Upload successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 파일의 고유 식별자 |
| user_id | string | 파일을 업로드한 사용자의 ID |
| post_id | string | 이 파일이 게시물에 첨부된 경우, 해당 게시물의 ID |
| create_at | integer | 파일이 생성된 시간 (밀리초) |
| update_at | integer | 파일이 마지막으로 수정된 시간 (밀리초) |
| delete_at | integer | 파일이 삭제된 시간 (밀리초) |
| name | string | 파일 이름 |
| extension | string | 파일 이름 끝의 확장자 |
| size | integer | 파일 크기 (바이트) |
| mime_type | string | 파일의 MIME 타입 |
| width | integer | 이미지 파일인 경우, 파일의 너비 |
| height | integer | 이미지 파일인 경우, 파일의 높이 |
| has_preview_image | boolean | 이미지 파일인 경우, 미리보기 이미지 존재 여부 |

```json
{
  "id": "string",
  "user_id": "string",
  "post_id": "string",
  "create_at": 0,
  "update_at": 0,
  "delete_at": 0,
  "name": "string",
  "extension": "string",
  "size": 0,
  "mime_type": "string",
  "width": 0,
  "height": 0,
  "has_preview_image": true
}
```

### 204 - Upload incomplete

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 413 | 명시되지 않음 |
| 501 | 명시되지 않음 |
