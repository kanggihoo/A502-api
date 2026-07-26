# 05-Get a custom emoji by name [GET]

`GET /api/v4/emoji/name/{emoji_name}`

Get some metadata for a custom emoji using its name.
##### Permissions
Must be authenticated.

__Minimum server version__: 4.7


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `emoji_name` | `string` | `path` | Yes | Emoji name |

### Responses

#### 200 - Emoji retrieval successful

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

#### 404 - 

#### 501 - 

