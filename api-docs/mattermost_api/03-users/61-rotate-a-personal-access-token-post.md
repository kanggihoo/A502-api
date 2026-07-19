# 61-Rotate a personal access token [POST]

`POST /api/v4/users/tokens/rotate`

Generate a new secret for an existing personal access token, immediately invalidating the old secret and any sessions that used it. The response includes the new token secret (shown once, like token creation).

__Minimum server version__: 10.10

##### Permissions
Must have `create_user_access_token` permission. For non-self requests, must also have the `edit_other_users` permission. To rotate a token belonging to a system admin, must also have the `manage_system` permission. OAuth sessions cannot use this endpoint.


### Request Body (application/json)

```json
{
  "token_id": string (required), // The personal access token GUID to rotate
  "expires_at": integer, // New expiry for the token as a Unix timestamp in milliseconds. Use 0 for no expiry (subject to server policy). 
}
```
### Responses

#### 200 - Personal access token rotation successful; response includes the new secret

Schema (application/json):
```json
{
  "id": string, // Unique identifier for the token
  "token": string, // The token used for authentication
  "user_id": string, // The user the token authenticates for
  "description": string, // A description of the token usage
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

