# 2. Get teams

## 기본 정보

- **기능:** 서버에 존재하는 팀 목록을 조회한다.
- **Endpoint:** `GET /api/v4/teams`
- **인증:** Bearer Token 필요
- **권한:** Must be authenticated. "manage_system" permission is required to show all teams.

## 설명

일반 사용자로 호출하면 open(공개) 팀 목록만 반환된다. `manage_system` 권한을 가진 사용자는 타입에 관계없이 모든 팀을 조회할 수 있다. 결과는 `page`, `per_page` 쿼리 파라미터로 페이징된다.

## Request

### Query parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of teams per page. |
| `include_total_count` | `boolean` | `query` | No | Appends a total count of returned teams inside the response object - ex: `{ "teams": [], "total_count" : 0 }`. |
| `exclude_policy_constrained` | `boolean` | `query` | No | If set to true, teams which are part of a data retention policy will be excluded. The `sysconsole_read_compliance` permission is required to use this parameter. (Minimum server version: 5.35) |

## Response

### 200 - Team list retrieval successful

```json
[
  {
    "id": string,
    "create_at": integer,
    "update_at": integer,
    "delete_at": integer,
    "display_name": string,
    "name": string,
    "description": string,
    "email": string,
    "type": string,
    "allowed_domains": string,
    "invite_id": string,
    "allow_open_invite": boolean,
    "policy_id": string
  }
]
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |

## 주의 사항

일반 사용자(manage_system 미보유)는 open 팀만 조회 가능하다.

---

# 10. Search teams

## 기본 정보

- **기능:** 검색어와 옵션을 기반으로 팀을 검색한다.
- **Endpoint:** `POST /api/v4/teams/search`
- **인증:** Bearer Token 필요
- **권한:** Logged in user only shows open teams / Logged in user with "manage_system" permission shows all teams

## 설명

로그인한 사용자는 open 팀만 검색 결과에 노출되며, `manage_system` 권한 보유자는 모든 팀을 검색할 수 있다. `page`/`per_page`가 모두 전달되지 않으면 페이징되지 않은 배열 형태로 응답한다.

## Request

### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `term` | string | No | The search term to match against the name or display name of teams |
| `page` | string | No | The page number to return, if paginated |
| `per_page` | string | No | The number of entries to return per page, if paginated |
| `allow_open_invite` | boolean | No | Filters results to teams where `allow_open_invite` is true/false (min server version 5.28) |
| `group_constrained` | boolean | No | Filters results to teams where `group_constrained` is true/false (min server version 5.28) |
| `exclude_policy_constrained` | boolean | No | Requires `sysconsole_read_compliance_data_retention` permission (min server version 5.35) |

```json
{
  "term": "string",
  "page": "string",
  "per_page": "string",
  "allow_open_invite": true,
  "group_constrained": true,
  "exclude_policy_constrained": true
}
```

## Response

### 200 - Paginated teams response (non-paginated response is a plain array of teams if page/per_page not both provided)

```json
{
  "teams": [
    {
      "id": string,
      "create_at": integer,
      "update_at": integer,
      "delete_at": integer,
      "display_name": string,
      "name": string,
      "description": string,
      "email": string,
      "type": string,
      "allowed_domains": string,
      "invite_id": string,
      "allow_open_invite": boolean,
      "policy_id": string
    }
  ],
  "total_count": 0
}
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 11. Check if team exists

## 기본 정보

- **기능:** 팀 이름(name)을 기준으로 해당 팀이 존재하는지 확인한다.
- **Endpoint:** `GET /api/v4/teams/name/{team_name}/exists`
- **인증:** Bearer Token 필요
- **권한:** Must be authenticated.

## 설명

팀 이름을 기준으로 존재 여부(boolean)만 반환하는 단순 조회 API다. 별도의 team-level 권한 없이 인증만 되어 있으면 호출 가능하다.

## Request

### Path parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_name` | string | path | Yes | Team Name |

## Response

### 200 - Team retrieval successful

```json
{
  "exists": true
}
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 12. Get a user's teams

## 기본 정보

- **기능:** 특정 사용자가 속한 팀 목록을 조회한다.
- **Endpoint:** `GET /api/v4/users/{user_id}/teams`
- **인증:** Bearer Token 필요
- **권한:** Must be authenticated as the user or have the `manage_system` permission.

## 설명

호출자가 조회 대상 사용자 본인일 경우 별도의 권한 없이 자신이 속한 팀 목록을 조회할 수 있다. 타인의 팀 목록을 조회하려면 `manage_system` 권한이 필요하다.

## Request

### Path parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | Yes | User GUID |

## Response

### 200 - Team list retrieval successful

```json
[
  {
    "id": string,
    "create_at": integer,
    "update_at": integer,
    "delete_at": integer,
    "display_name": string,
    "name": string,
    "description": string,
    "email": string,
    "type": string,
    "allowed_domains": string,
    "invite_id": string,
    "allow_open_invite": boolean,
    "policy_id": string
  }
]
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

## 주의 사항

본인(`user_id`가 자기 자신)에 대해서만 별도 권한 없이 사용 가능하며, 타인의 팀 목록 조회는 `manage_system` 권한이 필요해 일반 학생 계정으로는 불가능하다.

---

# 14. Add user to team

## 기본 정보

- **기능:** 사용자를 팀에 멤버로 추가한다.
- **Endpoint:** `POST /api/v4/teams/{team_id}/members`
- **인증:** Bearer Token 필요
- **권한:** Must be authenticated and team be open to add self. For adding another user, authenticated user must have the `add_user_to_team` permission.

## 설명

팀이 open(공개) 상태인 경우 인증된 사용자가 자기 자신을 해당 팀에 추가(가입)할 수 있다. 자신이 아닌 다른 사용자를 팀에 추가하려면 `add_user_to_team` 권한이 필요하다.

## Request

### Path parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | string | path | Yes | Team GUID |

### Body

```json
{
  "team_id": "string",
  "user_id": "string"
}
```

## Response

### 201 - Team member creation successful

```json
{
  "team_id": string,
  "user_id": string,
  "roles": string,
  "delete_at": integer,
  "scheme_user": boolean,
  "scheme_admin": boolean,
  "explicit_roles": string
}
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

## 주의 사항

일반 학생 계정은 "open 팀에 자기 자신을 추가(자진 가입)"하는 용도로만 사용 가능하며, 타인을 팀에 추가하려면 `add_user_to_team` 권한이 필요해 이 경우는 사용할 수 없다.

---

# 15. Add user to team from invite

## 기본 정보

- **기능:** 초대 링크의 invite id 또는 hash/data 쌍을 이용해 사용자를 팀에 추가한다.
- **Endpoint:** `POST /api/v4/teams/members/invite`
- **인증:** Bearer Token 필요
- **권한:** Must be authenticated.

## 설명

이메일 초대 링크에 포함된 토큰(invite id 또는 hash/data)을 이용해 인증된 사용자를 해당 팀에 가입시킨다. 별도의 team-level 권한 없이 인증만 되어 있으면 호출 가능하다.

## Request

### Query parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `token` | string | query | Yes | Token id from the invitation |

## Response

### 201 - Team member creation successful

```json
{
  "team_id": string,
  "user_id": string,
  "roles": string,
  "delete_at": integer,
  "scheme_user": boolean,
  "scheme_admin": boolean,
  "explicit_roles": string
}
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

---

# 17. Get team members for a user

## 기본 정보

- **기능:** 특정 사용자가 속한 팀들에서의 멤버 정보(팀 ID, 역할 등) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/users/{user_id}/teams/members`
- **인증:** Bearer Token 필요
- **권한:** Must be logged in as the user or have the `edit_other_users` permission.

## 설명

사용자가 속한 팀들의 ID와 해당 팀에서의 역할(role)을 확인하는 데 유용하다. 호출자가 조회 대상 본인일 경우 별도 권한 없이 사용 가능하며, 타인을 조회하려면 `edit_other_users` 권한이 필요하다.

## Request

### Path parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | Yes | User GUID |

## Response

### 200 - Team members retrieval successful

```json
[
  {
    "team_id": string,
    "user_id": string,
    "roles": string,
    "delete_at": integer,
    "scheme_user": boolean,
    "scheme_admin": boolean,
    "explicit_roles": string
  }
]
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

## 주의 사항

본인 조회에 한해 별도 권한 없이 사용 가능하다. 타인 조회는 `edit_other_users` 권한이 필요해 일반 학생 계정으로는 불가능하다.

---

# 19. Remove user from team

## 기본 정보

- **기능:** 팀 멤버 객체를 삭제하여 사용자를 팀에서 제거한다.
- **Endpoint:** `DELETE /api/v4/teams/{team_id}/members/{user_id}`
- **인증:** Bearer Token 필요
- **권한:** Must be logged in as the user or have the `remove_user_from_team` permission.

## 설명

호출자가 제거 대상 본인일 경우 별도 권한 없이 스스로 팀을 탈퇴할 수 있다. 타인을 제거하려면 `remove_user_from_team` 권한이 필요하다.

## Request

### Path parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | string | path | Yes | Team GUID |
| `user_id` | string | path | Yes | User GUID |

## Response

### 200 - Team member deletion successful

```json
{
  "status": "string"
}
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |

## 주의 사항

본인의 팀 탈퇴 목적으로만 별도 권한 없이 사용 가능하다. 타인을 팀에서 제거하려면 `remove_user_from_team` 권한이 필요해 일반 학생 계정으로는 불가능하다.

---

# 24. Get the team icon

## 기본 정보

- **기능:** 팀 아이콘 이미지를 조회한다.
- **Endpoint:** `GET /api/v4/teams/{team_id}/image`
- **인증:** Bearer Token 필요
- **권한:** User must be authenticated. In addition, team must be open or the user must have the `view_team` permission.

## 설명

대상 팀이 open(공개) 상태이면 인증된 사용자 누구나 팀 아이콘을 조회할 수 있다. 팀이 open이 아니면 `view_team` 권한이 필요하다. (Minimum server version: 4.9)

## Request

### Path parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | string | path | Yes | Team GUID |

## Response

### 200 - Team icon retrieval successful

(응답 스키마 명시되지 않음)

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 404 | 명시되지 않음 |
| 501 | 명시되지 않음 |

## 주의 사항

open 팀에 한해 별도 권한 없이 사용 가능하다. open이 아닌 팀은 `view_team` 권한이 필요해 일반 학생 계정으로는 불가능할 수 있다.

---

# 29. Get team unreads for a user

## 기본 정보

- **기능:** 사용자가 속한 팀들에서의 읽지 않은 메시지/멘션 수를 조회한다.
- **Endpoint:** `GET /api/v4/users/{user_id}/teams/unread`
- **인증:** Bearer Token 필요
- **권한:** Must be logged in.

## 설명

사용자가 멤버로 있는 각 팀에 대한 읽지 않은 메시지 수(`msg_count`)와 멘션 수(`mention_count`)를 반환한다. 로그인만 되어 있으면 별도의 team-level 권한 없이 호출 가능하다.

## Request

### Path parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | Yes | User GUID |

### Query parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `exclude_team` | string | query | Yes | Optional team id to be excluded from the results |
| `include_collapsed_threads` | boolean | query | No | Boolean to determine whether the collapsed threads should be included or not |

## Response

### 200 - Team unreads retrieval successful

```json
[
  {
    "team_id": string,
    "msg_count": integer,
    "mention_count": integer
  }
]
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 35. Get invite info for a team

## 기본 정보

- **기능:** 팀 초대 id(invite_id)를 이용해 팀의 `id`, `name`, `display_name`, `description`을 조회한다.
- **Endpoint:** `GET /api/v4/teams/invite/{invite_id}`
- **인증:** 불필요
- **권한:** No authentication required.

## 설명

이메일 초대 링크 등에 포함된 invite id만으로 팀의 기본 정보를 조회할 수 있는 공개 API다. 인증 토큰이 전혀 필요하지 않다. (Minimum server version: 4.0)

## Request

### Path parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `invite_id` | string | path | Yes | Invite id for a team |

## Response

### 200 - Team invite info retrieval successful

```json
{
  "id": string,
  "name": string,
  "display_name": string,
  "description": string
}
```

## Errors

| 상태 코드 | 설명 |
| --- | --- |
| 400 | 명시되지 않음 |
