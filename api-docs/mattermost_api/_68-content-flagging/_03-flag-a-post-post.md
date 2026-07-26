# 03-Flag a post [POST]

`POST /api/v4/content_flagging/post/{post_id}/flag`

Flags a post with a reason and a comment. The user must have access to the channel to which the post belongs to.
An enterprise advanced license is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | The ID of the post to be flagged |

### Request Body (application/json)

```json
{
  "reason": string, // The reason for flagging the post. This must be one of the configured reasons available for selection.
  "comment": string, // Comment from the user flagging the post.
}
```
### Responses

#### 200 - Post flagged successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - Bad request - Invalid input data or missing required fields.

#### 403 - Forbidden - User does not have permission to flag this post.

#### 404 - Post not found or feature is disabled via the feature flag.

#### 500 - Internal server error.

#### 501 - Feature is disabled either via config or an Enterprise Advanced license is not available.

