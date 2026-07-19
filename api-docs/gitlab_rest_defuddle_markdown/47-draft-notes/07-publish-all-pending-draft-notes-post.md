# 07-Publish all pending draft notes [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/draft_notes/bulk_publish`

Publishes all pending draft notes for the current user on the specified merge request. Optionally sets the reviewer state and posts a summary note.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `merge_request_iid` | `integer` | `path` | Yes | The ID of a merge request |

### Request Body (application/json)

```json
{
  "reviewer_state": enum("requested_changes" | "reviewed"), // Set reviewer review state after publishing. Does not record a formal approval
  "note": string, // Summary note body to post on the merge request
  "internal": boolean, // If true, the summary note is internal
}
```
### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

