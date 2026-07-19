# 52-Create a user access token [POST]

`POST /api/v4/users/{user_id}/tokens`

Generate a user access token that can be used to authenticate with the Mattermost REST API.

__Minimum server version__: 4.1

##### Permissions
Must have `create_user_access_token` permission. For non-self requests, must also have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "description": string (required), // A description of the token usage
}
```
### Responses

#### 201 - User access token creation successful

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

