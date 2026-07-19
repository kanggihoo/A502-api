# 28-Update the scheme-derived roles of a team member. [PUT]

`PUT /api/v4/teams/{team_id}/members/{user_id}/schemeRoles`

Update a team member's scheme_admin/scheme_user properties. Typically this should either be `scheme_admin=false, scheme_user=true` for ordinary team member, or `scheme_admin=true, scheme_user=true` for a team admin.

__Minimum server version__: 5.0

##### Permissions
Must be authenticated and have the `manage_team_roles` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "scheme_admin": boolean (required),
  "scheme_user": boolean (required),
}
```
### Responses

#### 200 - Team member's scheme-derived roles updated successfully.

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

