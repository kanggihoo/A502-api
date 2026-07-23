# 24-Move a post (and any posts within that post's thread) [POST]

`POST /api/v4/posts/{post_id}/move`

Move a post/thread to another channel.
THIS IS A BETA FEATURE. The API is subject to change without notice.
##### Permissions
Must have `read_channel` permission for the channel the post is in. Must have `write_post` permission for the channel the post is being moved to.

__Minimum server version__: 9.3


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | The identifier of the post to move |

### Request Body (application/json)

```json
{
  "channel_id": string (required), // The channel identifier of where the post/thread is to be moved
}
```
### Responses

#### 200 - Post moved successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

