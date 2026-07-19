# 60-Enable personal access token [POST]

`POST /api/v4/users/tokens/enable`

Re-enable a personal access token that has been disabled.

__Minimum server version__: 4.4

##### Permissions
Must have `create_user_access_token` permission. For non-self requests, must also have the `edit_other_users` permission.


### Request Body (application/json)

```json
{
  "token_id": string (required), // The personal access token GUID to enable
}
```
### Responses

#### 200 - Personal access token enable successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

