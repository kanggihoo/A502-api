# 01-Create a custom emoji [POST]

`POST /api/v4/emoji`

Create a custom emoji for the team.
##### Permissions
Must be authenticated.


### Request Body (multipart/form-data)

```json
{
  "image": string (required), // A file to be uploaded
  "emoji": string (required), // A JSON object containing a `name` field with the name of the emoji and a `creator_id` field with the id of the authenticated user.
}
```
### Responses

#### 201 - Emoji creation successful

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

#### 413 - 

#### 501 - 

