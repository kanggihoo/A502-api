# 33-Update a user's MFA [PUT]

`PUT /api/v4/users/{user_id}/mfa`

Activates multi-factor authentication for the user if `activate` is true and a valid `code` is provided. If activate is false, then `code` is not required and multi-factor authentication is disabled for the user.
##### Permissions
Must be logged in as the user being updated or have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "activate": boolean (required), // Use `true` to activate, `false` to deactivate
  "code": string, // The code produced by your MFA client. Required if `activate` is true
}
```
### Responses

#### 200 - User MFA update successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

