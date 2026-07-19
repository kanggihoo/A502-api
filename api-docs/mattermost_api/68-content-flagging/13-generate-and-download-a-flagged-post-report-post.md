# 13-Generate and download a flagged post report [POST]

`POST /api/v4/content_flagging/post/{post_id}/report`

Generates a ZIP archive containing the flagged post, its edit history, content review details, post metadata, and any associated file attachments, then streams the archive back to the caller as a download. All other content reviewers of the post's team are notified that a report has been generated.
The user must be a content reviewer of the team to which the post belongs to, and the post must be flagged.
An enterprise advanced license is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | The ID of the flagged post to generate the report for |

### Request Body (application/json)

```json
{
  "comment": string, // Optional comment from the reviewer to be included in the generated report.
}
```
### Responses

#### 200 - Report generated successfully. The response body is a ZIP archive containing the flagged post report.

Schema (application/zip):
```json
string
```

#### 400 - Bad request - Invalid post ID.

#### 403 - Forbidden - User does not have permission to access this post, or is not a reviewer of the post's team.

#### 404 - Post not found or post is not flagged.

#### 500 - Internal server error.

#### 501 - Feature is disabled either via config or an Enterprise Advanced license is not available.

