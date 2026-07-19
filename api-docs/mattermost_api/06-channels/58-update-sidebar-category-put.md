# 58-Update sidebar category [PUT]

`PUT /api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}`

Updates a single sidebar category for the user on the given team.
__Minimum server version__: 5.26
##### Permissions
Must be authenticated and have the `list_team_channels` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `user_id` | `string` | `path` | Yes | User GUID |
| `category_id` | `string` | `path` | Yes | Category GUID |

### Request Body (application/json)

```json
{
  "id": string,
  "user_id": string,
  "team_id": string,
  "display_name": string,
  "type": enum("channels" | "custom" | "direct_messages" | "favorites"),
}
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

