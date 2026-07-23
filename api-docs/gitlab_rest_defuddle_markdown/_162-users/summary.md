# Users API 명세서 (관리자 권한 미필요 API)

본 문서는 `_162-users` 디렉토리 내의 GitLab Users (사용자 정보, 본인 프로필 관리, 상태 메시지 설정, 팔로우 및 이메일 관리) 관련 API 중 일반 사용자 및 인증된 유저 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 23개)

> **관리자(Admin) 전용 API 제외 목록 (20개)**
> - `01-retrieve-a-support-pin-for-a-user-get.md`: 타 유저 서포트 PIN 조회 (Admin 전용)
> - `02-revoke-a-support-pin-for-a-user-post.md`: 타 유저 서포트 PIN 폐기 (Admin 전용)
> - `04-create-a-user-post.md`: 신규 사용자 계정 생성 (`POST /api/v4/users` - Admin 전용)
> - `06-update-a-user-put.md`: 임의의 사용자 정보 수정 (`PUT /api/v4/users/{id}` - Admin 전용)
> - `07-delete-a-user-del.md`: 사용자 계정 삭제 (`DELETE /api/v4/users/{id}` - Admin 전용)
> - `13-disable-two-factor-authentication-for-a-user-patch.md`: 타 유저 2FA 강제 해제 (Admin 전용)
> - `14-delete-authentication-identity-from-a-user-del.md`: 인증 식별자 삭제 (Admin 전용)
> - `15-add-an-email-address-for-a-user-post.md`: 타 유저 이메일 추가 (Admin 전용)
> - `16-list-all-email-addresses-for-a-user-get.md`: 타 유저 이메일 목록 조회 (Admin 전용)
> - `17-delete-an-email-address-for-a-user-del.md`: 타 유저 이메일 삭제 (Admin 전용)
> - `18~25번`: 유저 재활성화, 승인/거절, 비활성화, 차단(Block/Unblock), 차단(Ban/Unban) (Admin 전용)
> - `26-list-all-project-and-group-memberships-for-a-user-get.md`: 전체 멤버십 조회 (Admin 전용)
> - `31-update-a-user-s-credit-card-validation-put.md`: 신용카드 검증 정보 수정 (Admin 전용)

---

## 03. List all users [GET]

### 기본 정보

- **기능:** GitLab 인스턴스의 사용자 목록을 검색하고 조회한다.
- **Endpoint:** `GET /api/v4/users`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자

### 설명

이름 또는 아이디(`search`), 활성화 상태(`active`, `blocked`), 사용자 역할 등을 지정하여 전체 유저 목록을 조회합니다. SSAFY 워크스페이스에서 팀원 검색 및 프로필 연동 시 주로 활용됩니다.

### Request

#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `search` | string | N | - | 사용자 이름 또는 username 검색어 | `kkh` |
| `username` | string | N | - | 정확한 username 매칭 | `kkh_ssafy` |
| `active` | boolean | N | - | 활성화된 사용자만 필터링 | `true` |
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
    "avatar_url": "https://lab.ssafy.com/uploads/-/system/user/avatar/12/avatar.png",
    "web_url": "https://lab.ssafy.com/kkh_ssafy"
  }
]
```





## 28. Retrieve current user details [GET]

### 기본 정보

- **기능:** 현재 인증된 사용자 본인의 전체 프로필 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/user`
- **인증:** Bearer Token 필요
- **권한:** 인증된 본인 사용자

### 설명

액세스 토큰의 소유자(본인) 사용자 계정의 모든 정체성 정보, 권한(`can_create_group`, `can_create_project`), 이메일, 작성 커밋 이메일, 테마 설정 등을 상세히 조회합니다. API 인증 확인 및 사용자 식별에 가장 기본적으로 사용됩니다.

### Response

#### `200 OK`
```json
{
  "id": 12,
  "username": "kkh_ssafy",
  "email": "kkh@ssafy.com",
  "name": "강기후",
  "state": "active",
  "can_create_group": true,
  "can_create_project": true,
  "two_factor_enabled": false,
  "commit_email": "kkh@ssafy.com"
}
```

---


## 38. List all activity for a user [GET]

### 기본 정보

- **기능:** 특정 사용자의 최신 활동 내역(커밋, 이슈, MR 생성 등)을 조회한다.
- **Endpoint:** `GET /api/v4/users/{id}/activities`
- **인증:** Bearer Token 필요


