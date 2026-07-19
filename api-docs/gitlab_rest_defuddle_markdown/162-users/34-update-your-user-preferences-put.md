# 34-Update your user preferences [PUT]

`PUT /api/v4/user/preferences`

Updates your user preferences.

### Request Body (application/json)

```json
{
  "view_diffs_file_by_file": boolean, // Flag indicating the user sees only one file diff per page
  "show_whitespace_in_diffs": boolean, // Flag indicating the user sees whitespace changes in diffs
  "pass_user_identities_to_ci_jwt": boolean, // Flag indicating the user passes their external identities to a CI job as part of a JSON web token.
  "policy_advanced_editor": boolean, // Flag indicating that advanced editor is enabled.
}
```
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

#### 400 - Bad Request

