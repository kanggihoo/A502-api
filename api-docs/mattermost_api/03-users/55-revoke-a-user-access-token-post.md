# 55-Revoke a user access token [POST]

`POST /api/v4/users/tokens/revoke`

Revoke a user access token and delete any sessions using the token.

__Minimum server version__: 4.1

##### Permissions
Must have `revoke_user_access_token` permission. For non-self requests, must also have the `edit_other_users` permission.


### Request Body (application/json)

```json
{
  "token_id": string (required), // The user access token GUID to revoke
}
```
### Responses

#### 200 - User access token revoke successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

