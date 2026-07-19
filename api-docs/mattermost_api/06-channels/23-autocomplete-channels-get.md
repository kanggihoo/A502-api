# 23-Autocomplete channels [GET]

`GET /api/v4/teams/{team_id}/channels/autocomplete`

Autocomplete public channels on a team based on the search term provided in the request URL.

__Minimum server version__: 4.7

##### Permissions
Must have the `list_team_channels` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `name` | `string` | `query` | Yes | Name or display name |

### Responses

#### 200 - Channels autocomplete successful

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

