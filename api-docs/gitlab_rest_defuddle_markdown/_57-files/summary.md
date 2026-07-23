# Files API 명세서 (관리자 권한 미필요 API)

본 문서는 `_57-files` 디렉토리 내의 GitLab Repository Files (저장소 파일 조회, Base64/Raw 다운로드, Blame 이력 조회, 파일 생성/수정/삭제 커밋) 관련 API 중 일반 사용자 및 프로젝트 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 8개)

---



## 02. Retrieve file blame history from a repository [GET]

### 기본 정보

- **기능:** 저장소 특정 파일의 라인별 Blame(작성자 및 최신 커밋 이력) 히스토리를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/files/{file_path}/blame`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

저장소의 특정 파일 경로(`file_path`)에 대해 소스코드 각 라인 그룹별 작성자, 커밋 SHA, 작성 시각, 변경 메시지 등 git blame 정보를 조회합니다. `ref` 파라미터로 브랜치나 커밋 SHA를 지정할 수 있습니다.

### Request

#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |
| `file_path` | string | Y | URL 인코딩된 파일 상대 경로 | `src%2Fmain%2FApp.java` |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ref` | string | Y | - | 브랜치명, 태그명 또는 커밋 SHA | `main` |

#### Body
없음

### Response

#### `200 OK`
```json
[
  {
    "commit": {
      "id": "a1b2c3d4...",
      "title": "feat: add user login API",
      "author_name": "강기후",
      "authored_date": "2026-07-23T10:00:00Z"
    },
    "lines": [
      "public class App {",
      "    public static void main(String[] args) {",
      "    }",
      "}"
    ]
  }
]
```

---

## 03. Retrieve a raw file from a repository [GET]

### 기본 정보

- **기능:** 저장소 특정 파일의 원본 텍스트/바이너리(Raw) 데이터를 다운로드한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/files/{file_path}/raw`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

파일 메타데이터 JSON 래핑 없이 소스코드나 이미지 등의 원본 파일 내용 자체를 다운로드 스트림으로 반환합니다.

### Request

#### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `ref` | string | Y | 브랜치명 또는 커밋 SHA | `main` |

### Response

#### `200 OK`
원본 파일 데이터 반환 (`Content-Type: text/plain` 등)

---


