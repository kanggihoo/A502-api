# 12-Assign a content reviewer to a flagged post [POST]

`POST /api/v4/content_flagging/post/{post_id}/assign/{content_reviewer_id}`

Assigns a content reviewer to a specific flagged post for review. The user must be a content reviewer of the team to which the post belongs to.
An enterprise advanced license is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | The ID of the post to assign a content reviewer to |
| `content_reviewer_id` | `string` | `path` | Yes | The ID of the user to be assigned as the content reviewer for the post |

### Responses

#### 200 - Content reviewer assigned successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - Bad request - Invalid input data or missing required fields.

#### 403 - Forbidden - User does not have permission to assign a reviewer to this post.

#### 404 - Post or user not found, or feature is disabled via the feature flag.

#### 500 - Internal server error.

#### 501 - Feature is disabled either via config or an Enterprise Advanced license is not available.

