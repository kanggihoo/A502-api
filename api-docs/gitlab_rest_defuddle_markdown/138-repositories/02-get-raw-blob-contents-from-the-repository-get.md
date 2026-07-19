# 02-Get raw blob contents from the repository [GET]

`GET /api/v4/projects/{id}/repository/blobs/{sha}/raw`

Get raw blob contents from the repository

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `path` | Yes | The commit hash |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

