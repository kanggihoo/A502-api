# 08-Keep a flagged post [PUT]

`PUT /api/v4/content_flagging/post/{post_id}/keep`

Marks a flagged post as reviewed and keeps it in the system without any changes. This action is typically performed by content reviewers after they have reviewed the flagged content and determined that it does not violate any guidelines.
The user must be a content reviewer of the team to which the post belongs to.
An enterprise advanced license is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | The ID of the post to be kept |

### Responses

#### 200 - Post marked to be kept successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - Forbidden - User does not have permission to keep this post.

#### 404 - Post not found or feature is disabled via the feature flag.

#### 500 - Internal server error.

#### 501 - Feature is disabled either via config or an Enterprise Advanced license is not available.

