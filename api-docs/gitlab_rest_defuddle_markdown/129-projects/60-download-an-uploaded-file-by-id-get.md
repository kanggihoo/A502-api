# 60-Download an uploaded file by ID [GET]

`GET /api/v4/projects/{id}/uploads/{upload_id}`

Downloads an uploaded file with a specified ID. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `upload_id` | `integer` | `path` | Yes | The ID of a project upload |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

