# 06-Delete a pipeline trigger token [DEL]

`DELETE /api/v4/projects/{id}/triggers/{trigger_id}`

Deletes a pipeline trigger token for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `trigger_id` | `integer` | `path` | Yes | The trigger token ID |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 412 - Precondition Failed

