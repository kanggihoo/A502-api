# 53-Get user access tokens [GET]

`GET /api/v4/users/{user_id}/tokens`

Get a list of user access tokens for a user. Does not include the actual authentication tokens. Use query parameters for paging.

__Minimum server version__: 4.1

##### Permissions
Must have `read_user_access_token` permission. For non-self requests, must also have the `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of tokens per page. |

### Responses

#### 200 - User access tokens retrieval successful

Schema (application/json):
```json
[
  {
    "id": string, // Unique identifier for the token
    "user_id": string, // The user the token authenticates for
    "description": string, // A description of the token usage
    "is_active": boolean, // Indicates whether the token is active
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

