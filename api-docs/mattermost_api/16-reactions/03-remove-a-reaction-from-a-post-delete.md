# 03-Remove a reaction from a post [DELETE]

`DELETE /api/v4/users/{user_id}/posts/{post_id}/reactions/{emoji_name}`

Deletes a reaction made by a user from the given post.
##### Permissions
Must be user or have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | ID of the user |
| `post_id` | `string` | `path` | Yes | ID of the post |
| `emoji_name` | `string` | `path` | Yes | emoji name |

### Responses

#### 200 - Reaction deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

