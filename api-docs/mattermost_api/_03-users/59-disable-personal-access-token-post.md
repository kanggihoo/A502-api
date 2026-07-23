# 59-Disable personal access token [POST]

`POST /api/v4/users/tokens/disable`

Disable a personal access token and delete any sessions using the token. The token can be re-enabled using `/users/tokens/enable`.

__Minimum server version__: 4.4

##### Permissions
Must have `revoke_user_access_token` permission. For non-self requests, must also have the `edit_other_users` permission.


### Request Body (application/json)

```json
{
  "token_id": string (required), // The personal access token GUID to disable
}
```
### Responses

#### 200 - Personal access token disable successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

