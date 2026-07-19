# 17-Pin a post to the channel [POST]

`POST /api/v4/posts/{post_id}/pin`

Pin a post to a channel it is in based from the provided post id string.
##### Permissions
Must be authenticated and have the `read_channel` permission to the channel the post is in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | Post GUID |

### Responses

#### 200 - Pinned post successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

