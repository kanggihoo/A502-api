# Groups API 명세서 (관리자 권한 미필요 API)



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

