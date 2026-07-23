# 62-Search tokens [POST]

`POST /api/v4/users/tokens/search`

Get a list of tokens based on search criteria provided in the request body. Searches are done against the token id, user id and username.

__Minimum server version__: 4.7

##### Permissions
Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "term": string (required), // The search term to match against the token id, user id or username.
}
```
### Responses

#### 200 - Personal access token search successful

Schema (application/json):
```json
[
  {
    "id": string, // Unique identifier for the token
    "user_id": string, // The user the token authenticates for
    "description": string, // A description of the token usage
    "is_active": boolean, // Indicates whether the token is active
  }
]
```

