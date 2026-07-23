# Groups API 명세서 (관리자 권한 미필요 API)

본 문서는 `_67-groups` 디렉토리 내의 GitLab Groups (그룹 목록 조회, 생성, 수정, 그룹 내 프로젝트/서브그룹 조회, 이슈 통계, 그룹 런너 및 그룹 토큰 관리) 관련 API 중 일반 사용자 및 그룹 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 40개)

> **관리자(Admin) 전용 API 제외 목록 (2개)**
> - `17-reset-the-runner-registration-token-for-the-instance-post.md`: 인스턴스 레벨 런너 등록 토큰 초기화 (Admin 전용)
> - `33-transfer-a-project-to-a-group-post.md`: 프로젝트를 타 그룹으로 강제 이관 (`POST /api/v4/groups/user/...` - Admin 전용)

---

## 19. List all groups [GET]

### 기본 정보

- **기능:** GitLab 인스턴스의 접근 가능한 모든 그룹 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자

### 설명

현재 로그인한 유저가 접근할 수 있는 최상위 그룹 및 서브그룹 목록을 가져옵니다. `search` 키워드로 그룹 이름/슬러그를 검색할 수 있으며, `min_access_level` 파라미터를 사용해 본인의 역할(Developer, Maintainer 등) 이상의 그룹만 필터링할 수 있습니다.

### Request

#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `search` | string | N | - | 그룹 이름/경로 검색어 | `s15p11a502` |
| `min_access_level` | integer | N | - | 최소 권한 레벨 (10:Guest, 20:Reporter, 30:Developer, 40:Maintainer, 50:Owner) | `30` |
| `top_level_only` | boolean | N | `false` | 최상위 그룹만 포함 | `true` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

### Response

#### `200 OK`
```json
[
  {
    "id": 105,
    "name": "S15P11A502",
    "path": "s15p11a502",
    "description": "SSAFY A502 Team Workspace",
    "visibility": "private",
    "web_url": "https://lab.ssafy.com/groups/s15p11a502"
  }
]
```

---

## 20. Create a group [POST]

### 기본 정보

- **기능:** 신규 그룹 또는 서브그룹(Subgroup)을 생성한다.
- **Endpoint:** `POST /api/v4/groups`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자 (그룹 생성 권한 보유 유저)

### Request

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `name` | string | Y | 그룹 표시 이름 | `S15P11A502` |
| `path` | string | Y | 그룹 URL 경로 | `s15p11a502` |
| `parent_id` | integer | N | 서브그룹 생성 시 상위 그룹 ID | `105` |
| `visibility` | string | N | 공개 범위 (`private` \| `internal` \| `public`) | `private` |

```json
{
  "name": "S15P11A502",
  "path": "s15p11a502",
  "visibility": "private"
}
```

### Response

#### `201 Created`
```json
{
  "id": 105,
  "name": "S15P11A502",
  "path": "s15p11a502",
  "visibility": "private"
}
```

---

## 22. Retrieve a group [GET]

### 기본 정보

- **기능:** 특정 그룹의 상세 프로필, 서브그룹 및 프로젝트 정보를 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Guest 이상)

### Response

#### `200 OK`
```json
{
  "id": 105,
  "name": "S15P11A502",
  "path": "s15p11a502",
  "projects": [
    {
      "id": 1234,
      "name": "A502-api",
      "path_with_namespace": "s15p11a502/A502-api"
    }
  ]
}
```

---

## 29. List all projects in a group [GET]

### 기본 정보

- **기능:** 특정 그룹에 속한 모든 프로젝트 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/projects`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Guest 이상)

### Request

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 URL 인코딩 경로 | `s15p11a502` |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `archived` | boolean | N | 아카이브된 프로젝트 포함 여부 | `false` |
| `include_subgroups` | boolean | N | 하위 서브그룹 내 프로젝트 포함 여부 | `true` |

### Response

#### `200 OK`
```json
[
  {
    "id": 1234,
    "name": "A502-api",
    "ssh_url_to_repo": "git@lab.ssafy.com:s15p11a502/A502-api.git",
    "http_url_to_repo": "https://lab.ssafy.com/s15p11a502/A502-api.git"
  }
]
```

---

## 31. List all subgroups [GET]

### 기본 정보

- **기능:** 특정 그룹 바로 하위에 직속된 서브그룹 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/subgroups`
- **인증:** Bearer Token 필요

---

## 11, 12. Group Issues & Statistics (GET, GET)

- **Endpoints:**
  - `GET /api/v4/groups/{id}/issues`: 그룹 산하 전체 프로젝트의 이슈통합 목록 조회
  - `GET /api/v4/groups/{id}/issues_statistics`: 그룹 산하 이슈 개수 상태별(`opened`, `closed`, `all`) 통계 조회

---

## 21, 23~26, 35. Group Lifecycle & Management (PUT, DEL, POST Archive/Unarchive/Restore/Transfer)

- **Endpoints:**
  - `PUT /api/v4/groups/{id}`: 그룹 속성(이름, 바너, 설명, 접근 정책) 수정 (Owner/Admin)
  - `DELETE /api/v4/groups/{id}`: 그룹 삭제 스케줄링 (Owner)
  - `POST /api/v4/groups/{id}/archive`: 그룹 아카이브 처리
  - `POST /api/v4/groups/{id}/unarchive`: 그룹 아카이브 해제
  - `POST /api/v4/groups/{id}/restore`: 삭제 대기 중인 그룹 복구
  - `POST /api/v4/groups/{id}/transfer`: 그룹 이동 (부모 그룹 변경 또는 독립 최상위 그룹 변환)

---

## 16, 18. Group Runners (GET, POST)

- **Endpoints:**
  - `GET /api/v4/groups/{id}/runners`: 그룹 소속 GitLab Runner 목록 조회
  - `POST /api/v4/groups/{id}/runners/reset_registration_token`: 그룹 런너 등록 토큰 초기화 (Owner/Admin)

---

## 04~10. Group File Uploads (POST Workhorse, POST Upload, GET List, GET Download, DEL Delete)

- **Endpoints:**
  - `POST /api/v4/groups/{id}/uploads`: 그룹 위키 및 이슈 첨부 파일 업로드
  - `GET /api/v4/groups/{id}/uploads`: 그룹 업로드 파일 목록 조회
  - `DELETE /api/v4/groups/{id}/uploads/{upload_id}`: 업로드된 파일 삭제
