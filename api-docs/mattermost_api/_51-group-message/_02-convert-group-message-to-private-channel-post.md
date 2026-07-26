# 02-Convert group message to private channel [POST]

`POST /api/v4/channels/{channel_id}/convert_to_channel`

Converts a group message channel into a private channel in the specified team.
##### Permissions
Must have `create_private_channel` permission in the destination team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Group message channel ID |

### Request Body (application/json)

```json
{
  "channel_id": string (required),
  "team_id": string (required),
}
```
### Responses

#### 200 - Conversion successful

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

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

