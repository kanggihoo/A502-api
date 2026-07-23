# 69-Delete an issue [DEL]

`DELETE /api/v4/projects/{id}/issues/{issue_iid}`

Deletes a specified issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of a project issue |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

