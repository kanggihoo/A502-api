# 01-Get all shared channels for team. [GET]

`GET /api/v4/sharedchannels/{team_id}`

Get all shared channels for a team.

__Minimum server version__: 5.50

##### Permissions
Must be authenticated and have the `view_team` permission for the team.
Results are restricted to channels the user is a member of unless the user has
`manage_shared_channels`.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team Id |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of sharedchannels per page. |

### Responses

#### 200 - Shared channels fetch successful. Result may be empty.

Schema (application/json):
```json
[
  {
    "id": string, // Channel id of the shared channel
    "team_id": string,
    "home": boolean, // Is this the home cluster for the shared channel
    "readonly": boolean, // Is this shared channel shared as read only
    "name": string, // Channel name as it is shared (may be different than original channel name)
    "display_name": string, // Channel display name as it appears locally
    "purpose": string,
    "header": string,
    "creator_id": string, // Id of the user that shared the channel
    "create_at": integer, // Time in milliseconds that the channel was shared
    "update_at": integer, // Time in milliseconds that the shared channel record was last updated
    "remote_id": string, // Id of the remote cluster where the shared channel is homed
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

