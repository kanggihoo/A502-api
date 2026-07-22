# 03-Check if a branch exists [HEAD]

`HEAD /api/v4/projects/{id}/repository/branches/{branch}`

Check if a branch exists

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `branch` | `string` | `path` | Yes | The name of the branch |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

