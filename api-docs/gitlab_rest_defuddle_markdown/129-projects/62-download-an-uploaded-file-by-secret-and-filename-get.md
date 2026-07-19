# 62-Download an uploaded file by secret and filename [GET]

`GET /api/v4/projects/{id}/uploads/{secret}/{filename}`

Downloads an uploaded file with a specified secret and filename. You must have the Guest, Planner, Reporter, Developer, Maintainer, or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `secret` | `string` | `path` | Yes | The 32-character secret of a project upload |
| `filename` | `string` | `path` | Yes | The filename of a project upload |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

