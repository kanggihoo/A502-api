# 07-Search custom emoji [POST]

`POST /api/v4/emoji/search`

Search for custom emoji by name based on search criteria provided in the request body. A maximum of 200 results are returned.
##### Permissions
Must be authenticated.

__Minimum server version__: 4.7


### Request Body (application/json)

```json
{
  "term": string (required), // The term to match against the emoji name.
  "prefix_only": string, // Set to only search for names starting with the search term.
}
```
### Responses

#### 200 - Emoji list retrieval successful

Schema (application/json):
```json
[
  {
    "id": string, // The ID of the emoji
    "creator_id": string, // The ID of the user that made the emoji
    "name": string, // The name of the emoji
    "create_at": integer, // The time in milliseconds the emoji was made
    "update_at": integer, // The time in milliseconds the emoji was last updated
    "delete_at": integer, // The time in milliseconds the emoji was deleted
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

