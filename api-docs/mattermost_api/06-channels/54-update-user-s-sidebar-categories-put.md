# 54-Update user's sidebar categories [PUT]

`PUT /api/v4/users/{user_id}/teams/{team_id}/channels/categories`

Update any number of sidebar categories for the user on the given team. This can be used to reorder the channels in these categories.
__Minimum server version__: 5.26
##### Permissions
Must be authenticated and have the `list_team_channels` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
[
  {
    "id": string,
    "user_id": string,
    "team_id": string,
    "display_name": string,
    "type": enum("channels" | "custom" | "direct_messages" | "favorites"),
  }
]
```
### Responses

#### 200 - Category update successful

Schema (application/json):
```json
{
  "id": string,
  "user_id": string,
  "team_id": string,
  "display_name": string,
  "type": enum("channels" | "custom" | "direct_messages" | "favorites"),
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

