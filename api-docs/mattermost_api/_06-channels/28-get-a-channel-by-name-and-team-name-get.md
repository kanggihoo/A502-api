# 28-Get a channel by name and team name [GET]

`GET /api/v4/teams/name/{team_name}/channels/name/{channel_name}`

Gets a channel from the provided team name and channel name strings.
##### Permissions
`read_channel` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_name` | `string` | `path` | Yes | Team Name |
| `channel_name` | `string` | `path` | Yes | Channel Name |
| `include_deleted` | `boolean` | `query` | No | Defines if deleted channels should be returned or not (Mattermost Server 5.26.0+) |

### Responses

#### 200 - Channel retrieval successful

Schema (application/json):
```json
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
```

#### 401 - 

#### 403 - 

#### 404 - 

