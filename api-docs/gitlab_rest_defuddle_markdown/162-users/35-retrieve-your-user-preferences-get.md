# 35-Retrieve your user preferences [GET]

`GET /api/v4/user/preferences`

Retrieves your user preferences.

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "user_id": string,
  "view_diffs_file_by_file": string,
  "show_whitespace_in_diffs": string,
  "pass_user_identities_to_ci_jwt": string,
  "policy_advanced_editor": string,
}
```

#### 401 - Unauthorized

#### 403 - Forbidden

