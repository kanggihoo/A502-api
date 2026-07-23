# 42-Revoke a user session [POST]

`POST /api/v4/users/{user_id}/sessions/revoke`

Revokes a user session from the provided user id and session id strings.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "session_id": string (required), // The session GUID to revoke.
}
```
### Responses

#### 200 - User session revoked successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

