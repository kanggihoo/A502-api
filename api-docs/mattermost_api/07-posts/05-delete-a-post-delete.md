# 05-Delete a post [DELETE]

`DELETE /api/v4/posts/{post_id}`

Soft deletes a post, by marking the post as deleted in the database. Soft deleted posts will not be returned in post queries.
##### Permissions
Must be logged in as the user or have `delete_others_posts` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | ID of the post to delete |

### Responses

#### 200 - Post deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

