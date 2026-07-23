# 54-Get user access tokens [GET]

`GET /api/v4/users/tokens`

Get a page of user access tokens for users on the system. Does not include the actual authentication tokens. Use query parameters for paging.

__Minimum server version__: 4.7

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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

