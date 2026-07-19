# 02-Download a project avatar [GET]

`GET /api/v4/projects/{id}/avatar`

Downloads a project avatar. You can access this endpoint without authentication if the project is publicly accessible. This feature was introduced in GitLab 16.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

