# Members API 명세서 (관리자 권한 미필요 API)

본 문서는 `_91-members` 디렉토리 내의 GitLab Members (프로젝트 및 그룹의 팀원 목록 조회, 신규 멤버 초청, 권한 레벨 변경, 멤버 탈퇴/제명) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버(Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 23개)

---

## 03. List all members of a group [GET]

### 기본 정보

- **기능:** 특정 그룹 및 상위 그룹으로부터 상속받은 모든 멤버 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/members/all`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Guest 이상)

### 설명

지정한 그룹의 직속 멤버뿐만 아니라 상위 조직 그룹으로부터 권한을 상속받은 모든 구성원 목록을 가져옵니다. 각 멤버의 사용자 계정 메타데이터 및 그룹 역할 권한 레벨(`access_level`: 10:Guest, 20:Reporter, 30:Developer, 40:Maintainer, 50:Owner), 권한 만료일(`expires_at`)을 확인할 수 있습니다.

### Request

#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 URL 인코딩 경로 | `s15p11a502` |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `query` | string | N | - | 멤버 사용자 이름/아이디 검색어 | `kkh` |
| `user_ids` | array | N | - | 특정 유저 ID 배열로 필터링 | `[12, 15]` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

### Response

#### `200 OK`
```json
[
  {
    "id": 12,
    "username": "kkh_ssafy",
    "name": "강기후",
    "state": "active",
    "access_level": 40,
    "created_at": "2026-07-23T10:00:00Z",
    "expires_at": null
  }
]
```

---

## 02. Add a member to a group [POST]

### 기본 정보

- **기능:** 그룹에 새로운 팀원 계정을 추가하고 역할 권한을 부여한다.
- **Endpoint:** `POST /api/v4/groups/{id}/members`
- **인증:** Bearer Token 필요
- **권한:** 그룹 Maintainer / Owner

### 설명

SSAFY 팀 프로젝트 확정 시 팀원들의 유저 ID(`user_id`)를 지정하여 그룹 멤버로 초청하거나 직접 추가합니다.

### Request

#### Body
| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `user_id` | string/integer | Y | - | 추가할 유저 ID 또는 username | `12` |
| `access_level` | integer | Y | 10\|20\|30\|40\|50 | 부여할 권한 레벨 (30:Developer, 40:Maintainer) | `30` |
| `expires_at` | string | N | YYYY-MM-DD | 권한 자동 만료 날짜 | `2026-12-31` |

```json
{
  "user_id": 12,
  "access_level": 30
}
```

### Response

#### `201 Created`
```json
{
  "id": 12,
  "username": "kkh_ssafy",
  "access_level": 30
}
```

---

## 05, 06. Group Member Update & Removal (PUT, DEL)

- **Endpoints:**
  - `PUT /api/v4/groups/{id}/members/{user_id}`: 기존 그룹 멤버의 역할 권한 레벨(`access_level`) 또는 만료일 수정
  - `DELETE /api/v4/groups/{id}/members/{user_id}`: 그룹에서 해당 멤버 제명/삭제

---

## 10. List all members of a project [GET]

### 기본 정보

- **기능:** 특정 프로젝트의 전체 멤버 목록(그룹 상속 멤버 포함)을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/members/all`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

---

## 09. Add a member to a project [POST]

### 기본 정보

- **기능:** 프로젝트 저장소에 새로운 팀원을 멤버로 추가한다.
- **Endpoint:** `POST /api/v4/projects/{id}/members`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### Request

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `user_id` | string/integer | Y | 대상 유저 ID | `12` |
| `access_level` | integer | Y | 권한 레벨 (30:Developer, 40:Maintainer) | `40` |

---

## 12, 13. Project Member Update & Removal (PUT, DEL)

- **Endpoints:**
  - `PUT /api/v4/projects/{id}/members/{user_id}`: 프로젝트 멤버의 권한 레벨(`access_level`) 변경
  - `DELETE /api/v4/projects/{id}/members/{user_id}`: 프로젝트에서 해당 멤버 삭제/제명
