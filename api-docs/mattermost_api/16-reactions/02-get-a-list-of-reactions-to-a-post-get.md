# 02-Get a list of reactions to a post [GET]

`GET /api/v4/posts/{post_id}/reactions`

Get a list of reactions made by all users to a given post.
##### Permissions
Must have `read_channel` permission for the channel the post is in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | ID of a post |

### Responses

#### 200 - List reactions retrieve successful

Schema (application/json):
```json
[
  {
    "user_id": string, // The ID of the user that made this reaction
    "post_id": string, // The ID of the post to which this reaction was made
    "emoji_name": string, // The name of the emoji that was used for this reaction
    "create_at": integer, // The time in milliseconds this reaction was made
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

