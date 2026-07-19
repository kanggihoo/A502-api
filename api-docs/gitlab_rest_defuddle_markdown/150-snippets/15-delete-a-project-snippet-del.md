# 15-Delete a project snippet [DEL]

`DELETE /api/v4/projects/{id}/snippets/{snippet_id}`

Delete a project snippet

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `snippet_id` | `integer` | `path` | Yes | The ID of a project snippet |

### Responses

#### 204 - No Content

#### 400 - Validation error

#### 404 - Not found

