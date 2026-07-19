# 08-Autocomplete custom emoji [GET]

`GET /api/v4/emoji/autocomplete`

Get a list of custom emoji with names starting with or matching the provided name. Returns a maximum of 100 results.
##### Permissions
Must be authenticated.

__Minimum server version__: 4.7


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `query` | Yes | The emoji name to search. |

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

