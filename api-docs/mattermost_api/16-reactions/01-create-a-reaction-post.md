# 01-Create a reaction [POST]

`POST /api/v4/reactions`

Create a reaction.
##### Permissions
Must have `read_channel` permission for the channel the post is in.


### Request Body (application/json)

```json
{
  "user_id": string, // The ID of the user that made this reaction
  "post_id": string, // The ID of the post to which this reaction was made
  "emoji_name": string, // The name of the emoji that was used for this reaction
  "create_at": integer, // The time in milliseconds this reaction was made
}
```
### Responses

#### 201 - Reaction creation successful

Schema (application/json):
```json
{
  "user_id": string, // The ID of the user that made this reaction
  "post_id": string, // The ID of the post to which this reaction was made
  "emoji_name": string, // The name of the emoji that was used for this reaction
  "create_at": integer, // The time in milliseconds this reaction was made
}
```

#### 400 - 

#### 403 - 

