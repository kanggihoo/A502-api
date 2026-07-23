# 55-Get user's sidebar category order [GET]

`GET /api/v4/users/{user_id}/teams/{team_id}/channels/categories/order`

Returns the order of the sidebar categories for a user on the given team as an array of IDs.
__Minimum server version__: 5.26
##### Permissions
Must be authenticated and have the `list_team_channels` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Order retrieval successful

Schema (application/json):
```json
[
  string
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

