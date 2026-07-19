# 37-Start a task to recalculate repository size for a project [POST]

`POST /api/v4/projects/{id}/repository_size`

This feature was introduced in GitLab 15.0.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Unauthenticated

#### 404 - Not Found

