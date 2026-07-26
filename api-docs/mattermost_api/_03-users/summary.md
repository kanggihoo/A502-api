# 1. Login to Mattermost server

## 기본 정보
- **기능**: Mattermost 서버에 로그인하여 세션을 생성한다.
- **Endpoint**: `POST /api/v4/users/login`
- **인증**: Bearer Token 불필요
- **권한**: 없음 (No permission required)

## 설명
로그인 자격 증명(login_id + password 등)으로 인증하여 세션 토큰을 발급받는다. MFA 사용 시 `token`, 게스트 매직 링크 인증 시 `magic_link_token`을 사용할 수 있다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | No | 사용자 ID |
| login_id | string | No | 로그인 ID (이메일/사용자명 등) |
| token | string | No | MFA 등 토큰 |
| device_id | string | No | 디바이스 ID |
| voip_device_id | string | No | VoIP 푸시 토큰. 제공 시 벨소리형 통화 푸시 알림 활성화 |
| ldap_only | boolean | No | LDAP만으로 인증 |
| password | string | No | 이메일 인증에 사용하는 비밀번호 |
| magic_link_token | string | No | 게스트 무비밀번호 인증용 매직 링크 토큰 (기능 활성화 필요) |

## Response

### 201 - User login successful
User 객체 반환. 핵심 필드: `id`, `username`, `first_name`, `last_name`, `nickname`, `email`, `email_verified`, `auth_service`, `roles`, `locale`, `notify_props`, `timezone`, `mfa_active`, `create_at`/`update_at`/`delete_at`, `terms_of_service_id`, `terms_of_service_create_at`

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 6. Logout from the Mattermost server

## 기본 정보
- **기능**: 현재 세션을 종료(로그아웃)한다.
- **Endpoint**: `POST /api/v4/users/logout`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션만 있으면 됨 (An active session is required)

## 설명
현재 사용자의 활성 세션을 종료한다.

## Response

### 201 - User logout successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 10. Get users

## 기본 정보
- **기능**: 사용자 목록을 페이지 단위로 조회한다.
- **Endpoint**: `GET /api/v4/users`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 + (지정 시) 대상 팀/채널의 멤버십 필요

## 설명
쿼리 파라미터에 따라 팀/채널 소속 사용자, 특정 채널에 없는 사용자 등을 선택 조회한다. `sort`는 팀 기준 조회 시에만 지원된다. `email_verified`, `notify_props` 등 일부 필드는 본인이거나 `manage_system` 권한이 있어야 보인다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| page | integer | No | 페이지 번호 |
| per_page | integer | No | 페이지당 사용자 수 |
| in_team | string | No | 이 팀에 속한 사용자 조회 |
| not_in_team | string | No | 이 팀에 없는 사용자 조회. `in_team`과 병용 불가 |
| in_channel | string | No | 이 채널에 속한 사용자 조회 |
| not_in_channel | string | No | 이 채널에 없는 사용자 조회. `in_channel`과 함께 사용해야 함 |
| in_group | string | No | 이 그룹의 사용자 조회. `manage_system` 권한 필요 |
| group_constrained | boolean | No | `not_in_channel`/`not_in_team`과 함께 사용 시 그룹 제약상 참여 가능한 사용자만 반환 |
| abac_match_only | boolean | No | `not_in_channel`과 함께 사용 시 ABAC 정책을 충족하는 사용자로 제한 (서버 11.8+) |
| without_team | boolean | No | 어떤 팀에도 없는 사용자 조회. 다른 팀/채널 옵션보다 우선 |
| active | boolean | No | 활성 사용자만. `inactive`와 병용 불가 |
| inactive | boolean | No | 비활성 사용자만. `active`와 병용 불가 |
| role | string | No | 해당 role을 가진 사용자 반환 |
| sort | string | No | `in_team`: ""/"last_activity_at"/"create_at", `in_channel`: ""/"status", `in_group`: ""/"display_name" |
| roles | string | No | 시스템 role 목록(콤마 구분)으로 필터 (서버 5.26+) |
| channel_roles | string | No | 채널 role 필터, `in_channel`과 함께만 사용 (서버 5.26+) |
| team_roles | string | No | 팀 role 필터, `in_team`과 함께만 사용 (서버 5.26+) |

## Response

### 200 - User page retrieval successful
User 객체 배열 반환 (`id`, `username`, `email`, `roles`, `notify_props`, `timezone` 등).

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 12. Get users by ids

## 기본 정보
- **기능**: 사용자 ID 목록으로 사용자들을 조회한다.
- **Endpoint**: `POST /api/v4/users/ids`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 외 별도 권한 불요

## 설명
요청 본문에 전달한 user id 배열에 해당하는 사용자 목록을 반환한다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| since | integer | No | 이 Unix timestamp(ms) 이후 수정된 사용자만 반환 (서버 5.14+) |

### Body
user ID 문자열 배열

```json
["string"]
```

## Response

### 200 - User list retrieval successful
User 객체 배열 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |

---

# 13. Get users by group channels ids

## 기본 정보
- **기능**: 그룹 채널 ID별로 소속 사용자 목록을 조회한다.
- **Endpoint**: `POST /api/v4/users/group_channels`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 외 별도 권한 불요 (본인이 멤버가 아닌 그룹 채널은 응답에서 제외됨)

## 설명
요청한 그룹 채널 ID를 키로, 해당 채널 멤버 사용자 목록을 값으로 갖는 객체를 반환한다. 요청자가 멤버가 아닌 그룹 채널은 응답에서 생략된다. 서버 최소 버전 5.14.

## Request

### Body
그룹 채널 ID 문자열 배열

```json
["string"]
```

## Response

### 200 - User list retrieval successful
`{ "<CHANNEL_ID>": [User, ...] }` 형태의 객체 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |

---

# 14. Get users by usernames

## 기본 정보
- **기능**: username 목록으로 사용자들을 조회한다.
- **Endpoint**: `POST /api/v4/users/usernames`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 외 별도 권한 불요

## 설명
요청 본문에 전달한 username 배열에 해당하는 사용자 목록을 반환한다.

## Request

### Body
username 문자열 배열

```json
["string"]
```

## Response

### 200 - User list retrieval successful
User 객체 배열 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |

---

# 15. Search users

## 기본 정보
- **기능**: 검색 조건으로 사용자를 검색한다.
- **Endpoint**: `POST /api/v4/users/search`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 + 요청 본문에 지정한 채널/팀에 대한 `read_channel` 및/또는 `view_team`

## 설명
username, 전체 이름, 닉네임, 이메일을 대상으로 검색한다(서버 설정에 따라 다를 수 있음). 팀/채널 범위를 좁혀 검색할 수 있다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| term | string | Yes | 검색어 (username/이름/닉네임/이메일 대상) |
| team_id | string | No | 이 팀 내 사용자만 검색 |
| not_in_team_id | string | No | 이 팀에 없는 사용자만 검색 |
| in_channel_id | string | No | 이 채널 내 사용자만 검색 |
| not_in_channel_id | string | No | 이 채널에 없는 사용자만 검색. `team_id` 필수 |
| in_group_id | string | No | 이 그룹 내 검색. `manage_system` 권한 필요 |
| group_constrained | boolean | No | 그룹 제약상 참여 가능한 사용자만 반환 |
| allow_inactive | boolean | No | true면 비활성 사용자 포함 |
| without_team | boolean | No | 팀에 없는 사용자 검색. 다른 팀/채널 옵션보다 우선 |
| limit | integer | No | 최대 반환 수 (서버 5.6+, 기본 100) |

## Response

### 200 - User list retrieval successful
User 객체 배열 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 16. Autocomplete users

## 기본 정보
- **기능**: 검색어 기반 사용자 자동완성 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/autocomplete`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 + 필터에 사용하는 팀/채널에 대한 `view_team`, `read_channel`

## 설명
입력한 검색어로 자동완성용 사용자 목록을 반환한다. `team_id`, `channel_id`를 조합해 결과 범위를 좁힐 수 있다.

## Request

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | No | 팀 ID |
| channel_id | string | No | 채널 ID |
| name | string | Yes | username, 닉네임, 이름 또는 성 |
| limit | integer | No | 각 하위 결과의 최대 수 (서버 5.6+, 기본 100) |

## Response

### 200 - User autocomplete successful
| 필드 | 타입 | 설명 |
|---|---|---|
| users | User[] | 주 검색 결과 사용자 목록 |
| out_of_channel | User[] | 특정 채널에서 자동완성할 때 채널 밖 사용자 목록 (비어 있으면 생략) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 17. Get user IDs of known users

## 기본 정보
- **기능**: 나와 채널을 공유하는(아는) 사용자들의 ID 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/known`
- **인증**: Bearer Token 필요
- **권한**: 인증만 필요 (Must be authenticated)

## 설명
DM/그룹 채널을 포함해 어떤 채널이든 공유하는, 직접적인 관계가 있는 사용자들의 ID 목록을 반환한다. 서버 최소 버전 5.23.

## Response

### 200 - Known users' IDs retrieval successful
사용자 ID 목록 반환 (스키마: any).

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 명시되지 않음 |

---

# 18. Get total count of users in the system

## 기본 정보
- **기능**: 시스템 전체 사용자 수를 조회한다.
- **Endpoint**: `GET /api/v4/users/stats`
- **인증**: Bearer Token 필요
- **권한**: 인증만 필요 (Must be authenticated)

## 설명
시스템 내 총 사용자 수를 반환한다.

## Response

### 200 - User stats retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| total_users_count | integer | 전체 사용자 수 |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 20. Get a user

## 기본 정보
- **기능**: 특정 사용자 정보를 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 외 별도 권한 불요

## 설명
사용자 객체를 조회한다. 민감 정보는 제거(sanitize)되어 반환된다. `user_id`에 "me"를 넣으면 현재 사용자를 가리킨다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID. "me"도 가능 (현재 사용자) |

## Response

### 200 - User retrieval successful
User 객체 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 21. Update a user

## 기본 정보
- **기능**: 사용자 정보를 전체 갱신한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 본인으로 로그인 (또는 `edit_other_users` 권한 — 일반 계정은 본인만 가능)

## 설명
사용자 객체 전체를 갱신한다. 요청 본문에 정의된 필드만 갱신 대상이며, 본문에 포함하지 않은 필드는 null이 되거나 기본값으로 되돌아가므로 주의해야 한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| id | string | Yes | 사용자 ID |
| email | string | Yes | 이메일 |
| username | string | Yes | 사용자명 |
| first_name | string | No | 이름 |
| last_name | string | No | 성 |
| nickname | string | No | 닉네임 |
| locale | string | No | 로케일 |
| position | string | No | 직책 |
| timezone | object | No | 타임존 설정 |
| props | object | No | 사용자 정의 속성 |
| notify_props | object | No | 알림 설정 |

## Response

### 200 - User update successful
갱신된 User 객체 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

## 주의 사항
- 본문에 포함하지 않은 필드는 null 또는 기본값으로 초기화된다. 부분 수정은 23번 Patch API 사용 권장.

---

# 23. Patch a user

## 기본 정보
- **기능**: 사용자 정보를 부분 갱신한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}/patch`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 본인으로 로그인 (또는 `edit_other_users` 권한 — 일반 계정은 본인만 가능)

## 설명
갱신하려는 필드만 제공하여 부분 수정한다. 생략한 필드는 변경되지 않는다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| email | string | No | 이메일 |
| username | string | No | 사용자명 |
| first_name | string | No | 이름 |
| last_name | string | No | 성 |
| nickname | string | No | 닉네임 |
| locale | string | No | 로케일 |
| position | string | No | 직책 |
| timezone | object | No | 타임존 설정 |
| props | object | No | 사용자 정의 속성 |
| notify_props | object | No | 알림 설정 |

## Response

### 200 - User patch successful
갱신된 User 객체 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 26. Get user's profile image

## 기본 정보
- **기능**: 사용자의 프로필 이미지를 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/image`
- **인증**: Bearer Token 필요
- **권한**: 로그인만 필요 (Must be logged in)

## 설명
user_id로 지정한 사용자의 프로필 이미지를 반환한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| _ | number | No | 서버에서 사용하지 않음. 캐싱 활용을 위해 마지막 사진 갱신 시각을 전달 가능 |

## Response

### 200 - User's profile image

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 27. Set user's profile image

## 기본 정보
- **기능**: 사용자의 프로필 이미지를 설정한다.
- **Endpoint**: `POST /api/v4/users/{user_id}/image`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 본인으로 로그인 (또는 `edit_other_users` 권한 — 일반 계정은 본인만 가능)

## 설명
multipart/form-data로 이미지를 업로드하여 프로필 이미지를 설정한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Body (multipart/form-data)
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| image | string | Yes | 업로드할 이미지 |

## Response

### 200 - Profile image set successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 28. Delete user's profile image

## 기본 정보
- **기능**: 사용자의 프로필 이미지를 삭제하고 기본 이미지로 되돌린다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/image`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 본인으로 로그인 (또는 `edit_other_users` 권한 — 일반 계정은 본인만 가능)

## 설명
프로필 이미지를 삭제하고 기본(자동 생성) 이미지로 초기화한다. 서버 최소 버전 5.5.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

## Response

### 200 - Profile image reset successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 29. Return user's default (generated) profile image

## 기본 정보
- **기능**: 사용자의 기본(자동 생성) 프로필 이미지를 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/image/default`
- **인증**: Bearer Token 필요
- **권한**: 로그인만 필요 (Must be logged in)

## 설명
user_id에 해당하는 사용자의 기본 생성 프로필 이미지를 반환한다. 서버 최소 버전 5.5.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

## Response

### 200 - Default profile image

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 30. Get a user by username

## 기본 정보
- **기능**: username으로 사용자를 조회한다.
- **Endpoint**: `GET /api/v4/users/username/{username}`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 외 별도 권한 불요

## 설명
username으로 사용자 객체를 조회한다. 민감 정보는 제거되어 반환된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| username | string | Yes | Username |

## Response

### 200 - User retrieval successful
User 객체 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 38. Update a user's password

## 기본 정보
- **기능**: 사용자 비밀번호를 변경한다.
- **Endpoint**: `PUT /api/v4/users/{user_id}/password`
- **인증**: Bearer Token 필요
- **권한**: 비밀번호를 변경할 사용자 본인으로 로그인 (또는 `manage_system` — 일반 계정은 본인만 가능)

## 설명
새 비밀번호는 서버 설정의 비밀번호 정책을 충족해야 한다. 본인 비밀번호를 변경할 때는 현재 비밀번호가 필수다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| current_password | string | No | 현재 비밀번호 (본인 변경 시 필요) |
| new_password | string | Yes | 새 비밀번호 |

## Response

### 200 - User password update successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 40. Get a user by email

## 기본 정보
- **기능**: 이메일로 사용자를 조회한다.
- **Endpoint**: `GET /api/v4/users/email/{email}`
- **인증**: Bearer Token 필요
- **권한**: 활성 세션 + 서버 프라이버시 설정상 다른 사용자의 이메일을 볼 수 있어야 함

## 설명
이메일 주소로 사용자 객체를 조회한다. 민감 정보는 제거되어 반환된다. 서버의 프라이버시 설정에 따라 조회가 제한될 수 있다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| email | string | Yes | User Email |

## Response

### 200 - User retrieval successful
User 객체 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 41. Get user's sessions

## 기본 정보
- **기능**: 사용자의 세션 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/sessions`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 본인으로 로그인 (또는 `edit_other_users` 권한 — 일반 계정은 본인만 가능)

## 설명
user GUID로 세션 목록을 조회한다. 민감 정보는 제거되어 반환된다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

## Response

### 200 - User session retrieval successful
세션 객체 배열 반환. 핵심 필드: `id`, `user_id`, `create_at`, `expires_at`, `last_activity_at`, `device_id`, `voip_device_id`, `is_oauth`, `roles`, `team_members`, `token`, `props`

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 42. Revoke a user session

## 기본 정보
- **기능**: 사용자의 특정 세션을 취소(revoke)한다.
- **Endpoint**: `POST /api/v4/users/{user_id}/sessions/revoke`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 본인으로 로그인 (또는 `edit_other_users` 권한 — 일반 계정은 본인만 가능)

## 설명
user id와 session id를 지정하여 해당 세션을 무효화한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| session_id | string | Yes | 취소할 세션 GUID |

## Response

### 200 - User session revoked successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 46. Get user's audits

## 기본 정보
- **기능**: 사용자의 감사(audit) 로그 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/audits`
- **인증**: Bearer Token 필요
- **권한**: 사용자 본인으로 로그인 (또는 `edit_other_users` 권한 — 일반 계정은 본인만 가능)

## 설명
user GUID로 해당 사용자의 감사 기록 목록을 조회한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

## Response

### 200 - User audits retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 감사 기록 ID |
| create_at | integer | 생성 시각 (밀리초) |
| user_id | string | 사용자 ID |
| action | string | 수행한 동작 |
| extra_info | string | 부가 정보 |
| ip_address | string | IP 주소 |
| session_id | string | 세션 ID |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 50. Switch login method

## 기본 정보
- **기능**: 로그인 방식을 전환한다 (email ↔ OAuth2/SAML/LDAP).
- **Endpoint**: `POST /api/v4/users/login/switch`
- **인증**: 원칙적으로 불필요 (OAuth2/SAML → email 전환 시에만 현재 인증 필요)
- **권한**: 없음 (OAuth2/SAML에서 email로 전환할 때만 현재 인증 필요)

## 설명
이메일 인증에서 OAuth2/SAML/LDAP로, 혹은 그 반대로 로그인 방식을 전환한다. OAuth2/SAML로 전환하는 경우 응답의 링크를 따라 제공자 측 절차를 완료해야 전환이 완료된다. 전환 방향에 따라 필요한 필드 조합이 다르며, MFA가 활성화된 계정은 `mfa_code`를 함께 보내야 한다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| current_service | string | Yes | 현재 사용 중인 로그인 서비스 |
| new_service | string | Yes | 전환할 로그인 서비스 |
| email | string | No | 사용자 이메일 |
| password | string | No | 현재 서비스의 비밀번호 |
| mfa_code | string | No | 현재 서비스의 MFA 코드 |
| ldap_id | string | No | 사용자의 LDAP/AD id |

## Response

### 200 - Login method switch or request successful
| 필드 | 타입 | 설명 |
|---|---|---|
| follow_link | string | 로그인 또는 전환 완료를 위해 사용자가 따라갈 링크 |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 52. Create a user access token

## 기본 정보
- **기능**: REST API 인증에 사용할 사용자 액세스 토큰을 생성한다.
- **Endpoint**: `POST /api/v4/users/{user_id}/tokens`
- **인증**: Bearer Token 필요
- **권한**: `create_user_access_token` 필요. 타인 대상 요청은 `edit_other_users`도 필요 (일반 계정은 본인 대상만 가능)

## 설명
Mattermost REST API 인증에 사용할 수 있는 사용자 액세스 토큰을 발급한다. 서버 최소 버전 4.1.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| description | string | Yes | 토큰 용도 설명 |

## Response

### 201 - User access token creation successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 토큰 고유 식별자 |
| token | string | 인증에 사용하는 실제 토큰 |
| user_id | string | 토큰이 인증하는 사용자 |
| description | string | 토큰 용도 설명 |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 53. Get user access tokens

## 기본 정보
- **기능**: 특정 사용자의 액세스 토큰 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/tokens`
- **인증**: Bearer Token 필요
- **권한**: `read_user_access_token` 필요. 타인 대상 요청은 `edit_other_users`도 필요 (일반 계정은 본인 대상만 가능)

## 설명
사용자의 액세스 토큰 목록을 페이징으로 조회한다. 실제 인증 토큰 값은 포함되지 않는다. 서버 최소 버전 4.1.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| page | integer | No | 페이지 번호 |
| per_page | integer | No | 페이지당 토큰 수 |

## Response

### 200 - User access tokens retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 토큰 고유 식별자 |
| user_id | string | 토큰이 인증하는 사용자 |
| description | string | 토큰 용도 설명 |
| is_active | boolean | 토큰 활성 여부 |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 58. Get a user access token

## 기본 정보
- **기능**: 액세스 토큰 하나의 정보를 조회한다.
- **Endpoint**: `GET /api/v4/users/tokens/{token_id}`
- **인증**: Bearer Token 필요
- **권한**: `read_user_access_token` 필요. 타인 대상 요청은 `edit_other_users`도 필요 (일반 계정은 본인 토큰만 가능)

## 설명
토큰 ID로 사용자 액세스 토큰 정보를 조회한다. 실제 인증 토큰 값은 포함되지 않는다. 서버 최소 버전 4.1.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| token_id | string | Yes | User access token GUID |

## Response

### 200 - User access token retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 토큰 고유 식별자 |
| user_id | string | 토큰이 인증하는 사용자 |
| description | string | 토큰 용도 설명 |
| is_active | boolean | 토큰 활성 여부 |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 64. Records user action when they accept or decline custom terms of service

## 기본 정보
- **기능**: 커스텀 서비스 약관 동의/거부 행동을 기록한다.
- **Endpoint**: `POST /api/v4/users/{user_id}/terms_of_service`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 본인으로 로그인 (Must be logged in as the user being acted on)

## 설명
사용자가 커스텀 서비스 약관을 수락/거부한 행동을 감사(audit) 테이블에 기록한다. 수락한 경우 사용자의 마지막 수락 약관 ID를 갱신한다. 서버 최소 버전 5.4.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| serviceTermsId | string | Yes | 대상 서비스 약관 ID |
| accepted | string | Yes | true/false, 수락 여부 |

## Response

### 200 - Terms of service action recorded successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 65. Fetches user's latest terms of service action if the latest action was for acceptance

## 기본 정보
- **기능**: 사용자의 최근 약관 수락 기록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/terms_of_service`
- **인증**: Bearer Token 필요
- **권한**: 대상 사용자 본인으로 로그인 (Must be logged in as the user being acted on)

## 설명
사용자의 최근 서비스 약관 행동이 '수락'인 경우 해당 기록을 반환한다. v6.0에서 deprecated 예정. 서버 최소 버전 5.6.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

## Response

### 200 - User's accepted terms of service action
| 필드 | 타입 | 설명 |
|---|---|---|
| user_id | string | 행동을 수행한 사용자 ID |
| terms_of_service_id | string | 대상 약관 ID |
| create_at | integer | 행동 수행 시각 (밀리초) |

### 404 - 사용자가 행동한 적이 없거나 최근 행동이 거부인 경우
| 필드 | 타입 | 설명 |
|---|---|---|
| status_code | integer | 상태 코드 |
| id | string | 에러 ID |
| message | string | 에러 메시지 |
| request_id | string | 요청 ID |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 404 | 행동 기록 없음 또는 최근 행동이 거부 |

---

# 67. Publish a user typing websocket event

## 기본 정보
- **기능**: 채널에 "사용자가 입력 중" websocket 이벤트를 발행한다.
- **Endpoint**: `POST /api/v4/users/{user_id}/typing`
- **인증**: Bearer Token 필요
- **권한**: 본인 이외 사용자로 발행하려면 `manage_system` 필요 (본인 대상은 일반 계정 가능)

## 설명
지정한 채널의 사용자들에게 해당 사용자가 입력 중임을 websocket으로 알린다. `parent_id`를 지정하면 스레드 대상으로 발행된다. 서버 최소 버전 5.26.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User GUID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 타이핑 이벤트를 보낼 채널 ID |
| parent_id | string | No | 답글 중인 스레드의 루트 게시물 ID. 없으면 채널 전체 대상 |

## Response

### 200 - User typing websocket event accepted for publishing.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 68. Get uploads for a user

## 기본 정보
- **기능**: 사용자의 업로드 세션 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/uploads`
- **인증**: Bearer Token 필요
- **권한**: 업로드 세션을 생성한 사용자 본인으로 로그인

## 설명
해당 사용자가 소유한 모든 업로드 세션을 반환한다. 서버 최소 버전 5.28.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"도 가능 (현재 사용자) |

## Response

### 200 - User's uploads retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 업로드 고유 식별자 |
| type | enum | "attachment" 또는 "import" |
| create_at | integer | 생성 시각 (밀리초) |
| user_id | string | 업로드를 수행한 사용자 ID |
| channel_id | string | 업로드 대상 채널 ID |
| filename | string | 업로드할 파일 이름 |
| file_size | integer | 파일 크기 (바이트) |
| file_offset | integer | 업로드된 데이터 양 (바이트) |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 69. Get all channel members from all teams for a user

## 기본 정보
- **기능**: 모든 팀에 걸친 사용자의 채널 멤버십을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/channel_members`
- **인증**: Bearer Token 필요
- **권한**: 사용자 본인으로 로그인 (또는 `edit_other_users` 권한 — 일반 계정은 본인만 가능)

## 설명
모든 팀의 모든 채널에 대한 해당 사용자의 채널 멤버 목록을 페이징으로 반환한다. 서버 최소 버전 6.2.0.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 ID. "me"도 가능 (현재 사용자) |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| page | integer | No | 반환할 결과 페이지 |
| per_page | integer | No | 반환 결과 청크 크기 |

## Response

### 200 - 조회 성공
채널 멤버 배열 반환 (스키마: any 배열).

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 72. Upsert synced draft

## 기본 정보
- **기능**: 현재 사용자의 동기화 초안(draft)을 생성/갱신한다.
- **Endpoint**: `POST /api/v4/drafts`
- **인증**: Bearer Token 필요
- **권한**: 인증 + 해당 채널의 게시물 작성 권한 + 동기화 초안 기능 활성화 필요

## 설명
현재 사용자의 동기화 초안을 생성하거나 갱신한다. `message`를 빈 문자열로 보내면 초안이 삭제된다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 ID |
| root_id | string | No | 스레드 루트 게시물 ID |
| message | string | Yes | 초안 메시지. 빈 문자열이면 초안 삭제 |
| type | string | No | 타입 |
| props | object | No | 속성 |
| file_ids | string[] | No | 첨부 파일 ID 목록 |
| priority | object | No | 우선순위 설정 (priority: ""/"important"/"urgent", requested_ack, persistent_notifications) |

## Response

### 201 - Draft upsert successful
초안 객체 반환. 빈 메시지로 초안을 삭제한 경우 `null` 반환.

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 73. Get synced drafts for a team

## 기본 정보
- **기능**: 특정 팀에서 현재 사용자의 동기화 초안 목록을 조회한다.
- **Endpoint**: `GET /api/v4/users/{user_id}/teams/{team_id}/drafts`
- **인증**: Bearer Token 필요
- **권한**: 해당 팀에 대한 `view_team` + 동기화 초안 기능 활성화 필요

## 설명
현재 사용자의 팀 내 동기화 초안들을 조회한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User ID |
| team_id | string | Yes | Team ID |

## Response

### 200 - Drafts retrieval successful
초안 객체 배열 반환. 핵심 필드: `user_id`, `channel_id`, `root_id`, `message`, `type`, `props`, `file_ids`, `metadata`(embeds/emojis/files/images/reactions/priority/acknowledgements), `priority`, `create_at`/`update_at`/`delete_at`(deprecated, 초안은 hard-delete됨)

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 74. Delete synced draft

## 기본 정보
- **기능**: 채널의 동기화 초안을 삭제한다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/channels/{channel_id}/drafts`
- **인증**: Bearer Token 필요
- **권한**: 초안 소유자 본인으로 인증 + 동기화 초안 기능 활성화 필요

## 설명
지정한 채널의 동기화 초안을 삭제한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User ID |
| channel_id | string | Yes | Channel ID |

## Response

### 200 - Draft deletion successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 75. Delete synced thread draft

## 기본 정보
- **기능**: 채널 스레드의 동기화 초안을 삭제한다.
- **Endpoint**: `DELETE /api/v4/users/{user_id}/channels/{channel_id}/drafts/{thread_id}`
- **인증**: Bearer Token 필요
- **권한**: 초안 소유자 본인으로 인증 + 동기화 초안 기능 활성화 필요

## 설명
지정한 채널의 특정 스레드에 대한 동기화 초안을 삭제한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | User ID |
| channel_id | string | Yes | Channel ID |
| thread_id | string | Yes | 스레드의 루트 게시물 ID |

## Response

### 200 - Thread draft deletion successful
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" |

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |
