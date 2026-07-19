# 01-Get a list of remote clusters. [GET]

`GET /api/v4/remotecluster`

Get a list of remote clusters.

##### Permissions
`manage_secure_connections` or `manage_shared_channels`


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select |
| `per_page` | `integer` | `query` | No | The number of remote clusters per page |
| `exclude_offline` | `boolean` | `query` | No | Exclude offline remote clusters |
| `in_channel` | `string` | `query` | No | Select remote clusters in channel |
| `not_in_channel` | `string` | `query` | No | Select remote clusters not in this channel |
| `only_confirmed` | `boolean` | `query` | No | Select only remote clusters already confirmed |
| `only_plugins` | `boolean` | `query` | No | Select only remote clusters that belong to a plugin |
| `exclude_plugins` | `boolean` | `query` | No | Select only remote clusters that don't belong to a plugin |
| `include_deleted` | `boolean` | `query` | No | Include those remote clusters that have been deleted |

### Responses

#### 200 - Remote clusters fetch successful. Result might be empty.

Schema (application/json):
```json
[
  {
    "remote_id": string,
    "remote_team_id": string,
    "name": string,
    "display_name": string,
    "site_url": string, // URL of the remote cluster
    "default_team_id": string, // The team where channels from invites are created
    "create_at": integer, // Time in milliseconds that the remote cluster was created
    "delete_at": integer, // Time in milliseconds that the remote cluster record was deleted
    "last_ping_at": integer, // Time in milliseconds when the last ping to the remote cluster was run
    "token": string,
    "remote_token": string,
    "topics": string,
    "creator_id": string,
    "plugin_id": string,
    "options": integer, // A bitmask with a set of option flags
  }
]
```

#### 401 - 

#### 403 - 

