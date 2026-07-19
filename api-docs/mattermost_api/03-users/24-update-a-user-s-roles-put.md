# 24-Update a user's roles [PUT]

`PUT /api/v4/users/{user_id}/roles`

Update a user's system-level roles. Valid user roles are "system_user", "system_admin" or both of them. Overwrites any previously assigned system-level roles.
##### Permissions
Must have the `manage_roles` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "roles": string (required),
}
```
### Responses

#### 200 - User roles update successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

