# Avatars API 명세서 (관리자 권한 미필요 API)

본 문서는 `_15-avatars` 디렉토리 내의 GitLab Avatars (사용자/프로젝트/그룹 아바타 프로필 이미지 업로드 및 다운로드) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 4개)

---

## 01. Upload an avatar [PUT]

### 기본 정보

- **기능:** 현재 인증된 사용자의 프로필 아바타 이미지를 업로드한다.
- **Endpoint:** `PUT /api/v4/user/avatar`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자

### 설명

현재 액세스 토큰을 보유한 사용자의 프로필 아바타 이미지 파일을 업로드하고 변경합니다. 요청 본문은 `multipart/form-data` 형식으로 전송해야 하며, 성공 시 변경된 아바타의 URL(`avatar_url`)을 반환합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `multipart/form-data` |

#### Path parameters

없음

#### Query parameters

없음

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `avatar` | file/binary | Y | 이미지 파일 (PNG/JPG 등) | 업로드할 이미지 바이너리 파일 데이터 | `avatar.png` |

```json
{
  "avatar": "binary data"
}
```

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `avatar_url` | string | 업로드 완료된 사용자 아바타 이미지 URL | `https://gitlab.com/uploads/-/system/user/avatar/12/avatar.png` |

```json
{
  "avatar_url": "https://gitlab.com/uploads/-/system/user/avatar/12/avatar.png"
}
```

---

## 02. Download a project avatar [GET]

### 기본 정보

- **기능:** 특정 프로젝트의 아바타 프로필 이미지를 다운로드한다.
- **Endpoint:** `GET /api/v4/projects/{id}/avatar`
- **인증:** Bearer Token 필요 / 공개 프로젝트의 경우 불필요
- **권한:** 프로젝트 멤버 (Guest 이상) 또는 공개 프로젝트 사용자

### 설명

지정한 프로젝트의 아바타 바이너리 이미지 파일 스트림을 가져옵니다. 공개(Public) 프로젝트의 경우 인증 토큰 없이도 접근하여 이미지 데이터를 다운로드할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | 액세스 토큰 (공개 프로젝트 시 불필요) | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

#### Query parameters

없음

#### Body

없음

### Response

#### `200 OK`

아바타 이미지 바이너리 데이터 스트림 반환 (`Content-Type: image/png` 등)

---

## 03. Download a group avatar [GET]

### 기본 정보

- **기능:** 특정 그룹의 아바타 프로필 이미지를 다운로드한다.
- **Endpoint:** `GET /api/v4/groups/{id}/avatar`
- **인증:** Bearer Token 필요 / 공개 그룹의 경우 불필요
- **권한:** 그룹 멤버 (Guest 이상) 또는 공개 그룹 사용자

### 설명

지정한 그룹에 설정된 아바타 프로필 이미지를 바이너리 스트림 형태로 가져옵니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | 액세스 토큰 (공개 그룹 시 불필요) | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 URL 인코딩 경로 | `my-group` |

#### Query parameters

없음

#### Body

없음

### Response

#### `200 OK`

아바타 이미지 바이너리 데이터 스트림 반환

---

## 04. Return avatar url for a user [GET]

### 기본 정보

- **기능:** 공개 이메일 주소를 기반으로 사용자의 Gravatar/아바타 이미지 URL을 조회한다.
- **Endpoint:** `GET /api/v4/avatar`
- **인증:** Bearer Token 불필요 / 선택 사항
- **권한:** 없음

### 설명

사용자의 공개 이메일주소(`email`)를 전송하여 해당 유저의 아바타 이미지 접근 URL을 얻습니다. 원하는 픽셀 크기(`size`)를 옵션으로 지정할 수 있습니다.

### Request

#### Headers

없음

#### Path parameters

없음

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `email` | string | Y | - | 사용자의 공개 이메일 주소 | `user@example.com` |
| `size` | integer | N | - | 아바타 이미지 픽셀 크기 (가로/세로) | `80` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `avatar_url` | string | 사용자의 아바타 URL | `https://www.gravatar.com/avatar/ab12cd34...?s=80` |

```json
{
  "avatar_url": "https://www.gravatar.com/avatar/ab12cd34...?s=80"
}
```
