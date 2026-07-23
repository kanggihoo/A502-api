# Projects API 명세서 (관리자 권한 미필요 API)



## 07. Search on GitLab within a project [GET]

### 기본 정보

- **기능:** 특정 프로젝트 범위 내에서 코드, 이슈, MR 등을 검색한다.
- **Endpoint:** `GET /api/v4/projects/{id}/search`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Request

#### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `scope` | string | Y | 검색 범주 (`issues` \| `merge_requests` \| `wiki_blobs` \| `commits` \| `notes` 등) | `issues` |
| `search` | string | Y | 검색어 키워드 | `fix bug` |

### Response

#### `200 OK`
```json
[
  {
    "id": 101,
    "title": "Fix login bug",
    "project_id": 1234
  }
]
```

---


## 12. List all projects [GET]

### 기본 정보

- **기능:** 현재 인증된 사용자가 접근 가능한 모든 프로젝트 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자

### Request

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `archived` | boolean | N | - | 아카이브 여부 필터 | `false` |
| `visibility` | string | N | - | 공개 범위 (`public` \| `internal` \| `private`) | `private` |
| `search` | string | N | - | 프로젝트 검색어 | `backend` |

---



## 16. Retrieve a project [GET]

### 기본 정보

- **기능:** 특정 프로젝트의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Response

#### `200 OK`
```json
{
  "id": 1234,
  "name": "S15P11A502-api",
  "path_with_namespace": "s15p11a502/s15p11a502-api",
  "default_branch": "main",
  "web_url": "https://lab.ssafy.com/s15p11a502/s15p11a502-api"
}
```

---


## 28. Retrieve programming language usage information [GET]

### 기본 정보

- **기능:** 프로젝트 내 사용 중인 프로그래밍 언어 비중/사용량 통계를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/languages`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Response

#### `200 OK`
```json
{
  "Java": 65.5,
  "TypeScript": 24.0,
  "HTML": 10.5
}
```

---

## 33. List all members of a project [GET]

### 기본 정보

- **기능:** 프로젝트의 멤버 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/members`
- **인증:** Bearer Token 필요

---


## 43. Retrieve the statistics of the last 30 days [GET]

### 기본 정보

- **기능:** 프로젝트의 최근 30일 통계 정보(커밋, 이슈 등)를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/statistics`
- **인증:** Bearer Token 필요

---



## 57 ~ 63. File Uploads & Downloads (GET, POST, DEL)

- **Endpoints:**
  - `POST /api/v4/projects/{id}/uploads/authorize`
  - `POST /api/v4/projects/{id}/uploads`
  - `GET /api/v4/projects/{id}/uploads`
  - `GET /api/v4/projects/{id}/uploads/{upload_id}`
  - `DELETE /api/v4/projects/{id}/uploads/{upload_id}`
  - `GET /api/v4/projects/{id}/uploads/{secret}/{filename}`
  - `DELETE /api/v4/projects/{id}/uploads/{secret}/{filename}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)
- **설명:** 프로젝트 관련 첨부파일 업로드 인증, 업로드, 목록 조회, 다운로드 및 삭제를 처리합니다.


