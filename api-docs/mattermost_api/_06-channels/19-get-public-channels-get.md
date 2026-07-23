# 19-Get public channels [GET]

`GET /api/v4/teams/{team_id}/channels`

Get a page of public channels on a team based on query string parameters - page and per_page.
##### Permissions
Must be authenticated and have the `list_team_channels` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of public channels per page. |

### Responses

#### 200 - Channels retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a channel was created
    "update_at": integer, // The time in milliseconds a channel was last updated
    "delete_at": integer, // The time in milliseconds a channel was deleted
    "team_id": string,
    "type": string,
    "display_name": string,
    "name": string,
    "header": string,
    "purpose": string,
    "last_post_at": integer, // The time in milliseconds of the last post of a channel
    "total_msg_count": integer,
    "extra_update_at": integer, // Deprecated in Mattermost 5.0 release
    "creator_id": string,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

