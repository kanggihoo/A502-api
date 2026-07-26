# 02-Get a list of custom emoji [GET]

`GET /api/v4/emoji`

Get a page of metadata for custom emoji on the system. Since server version 4.7, sort using the `sort` query parameter.
##### Permissions
Must be authenticated.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of emojis per page. |
| `sort` | `string` | `query` | No | Either blank for no sorting or "name" to sort by emoji names. Minimum server version for sorting is 4.7. |

### Responses

#### 200 - Emoji list retrieval successful

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

