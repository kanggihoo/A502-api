# 25-Activate or deactivate a user [PUT]

`PUT /api/v4/users/{user_id}/active`

Activate or deactivate a user's account. A deactivated user can't log into Mattermost or use it without being reactivated.

__Since server version 4.6, users using a SSO provider to login can be activated or deactivated with this endpoint. However, if their activation status in Mattermost does not reflect their status in the SSO provider, the next synchronization or login by that user will reset the activation status to that of their account in the SSO provider. Server versions 4.5 and before do not allow activation or deactivation of SSO users from this endpoint.__
##### Permissions
User can deactivate themselves.
User with `manage_system` permission can activate or deactivate a user.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "active": boolean (required),
}
```
### Responses

#### 200 - User activation/deactivation update successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

