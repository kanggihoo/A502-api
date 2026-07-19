# 04-Delete external status check service [DEL]

`DELETE /api/v4/projects/{id}/external_status_checks/{check_id}`

Deletes a specified external status check service for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `check_id` | `integer` | `path` | Yes | ID of an external status check |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

