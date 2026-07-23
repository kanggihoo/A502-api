# 58-Get a user access token [GET]

`GET /api/v4/users/tokens/{token_id}`

Get a user access token. Does not include the actual authentication token.

__Minimum server version__: 4.1

##### Permissions
Must have `read_user_access_token` permission. For non-self requests, must also have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `token_id` | `string` | `path` | Yes | User access token GUID |

### Responses

#### 200 - User access token retrieval successful

Schema (application/json):
```json
{
  "id": string, // Unique identifier for the token
  "user_id": string, // The user the token authenticates for
  "description": string, // A description of the token usage
  "is_active": boolean, // Indicates whether the token is active
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

