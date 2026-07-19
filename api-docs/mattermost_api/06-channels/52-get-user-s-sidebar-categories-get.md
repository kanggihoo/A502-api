# 52-Get user's sidebar categories [GET]

`GET /api/v4/users/{user_id}/teams/{team_id}/channels/categories`

Get a list of sidebar categories that will appear in the user's sidebar on the given team, including a list of channel IDs in each category.
__Minimum server version__: 5.26
##### Permissions
Must be authenticated and have the `list_team_channels` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Category retrieval successful

Schema (application/json):
```json
[
  {
    "order": [
      string
    ],
    "categories": [
      {
        "id": string,
        "user_id": string,
        "team_id": string,
        "display_name": string,
        "type": enum("channels" | "custom" | "direct_messages" | "favorites"),
        "channel_ids": [
          string
        ],
      }
    ],
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

