# 11-Update a channel [PUT]

`PUT /api/v4/channels/{channel_id}`

Update a channel. The fields that can be updated are listed as parameters. Omitted fields will be treated as blanks.
##### Permissions
If updating a public channel, `manage_public_channel_members` permission is required. If updating a private channel, `manage_private_channel_members` permission is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Request Body (application/json)

```json
{
  "id": string (required), // The channel's id, not updatable
  "name": string, // The unique handle for the channel, will be present in the channel URL
  "display_name": string, // The non-unique UI name for the channel
  "purpose": string, // A short description of the purpose of the channel
  "header": string, // Markdown-formatted text to display in the header of the channel
}
```
### Responses

#### 200 - Channel update successful

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

