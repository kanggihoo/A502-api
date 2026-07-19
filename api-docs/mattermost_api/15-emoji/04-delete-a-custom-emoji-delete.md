# 04-Delete a custom emoji [DELETE]

`DELETE /api/v4/emoji/{emoji_id}`

Delete a custom emoji.
##### Permissions
Must have the `manage_team` or `manage_system` permissions or be the user who created the emoji.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `emoji_id` | `string` | `path` | Yes | Emoji GUID |

### Responses

#### 200 - Emoji delete successful

Schema (application/json):
```json
{
  "id": string, // The ID of the emoji
  "creator_id": string, // The ID of the user that made the emoji
  "name": string, // The name of the emoji
  "create_at": integer, // The time in milliseconds the emoji was made
  "update_at": integer, // The time in milliseconds the emoji was last updated
  "delete_at": integer, // The time in milliseconds the emoji was deleted
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

