# 01-Download snapshot of a Git repository [GET]

`GET /api/v4/projects/{id}/snapshot`

Downloads snapshot of a Git repository.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `wiki` | `boolean` | `query` | No | Set to true to receive the wiki repository |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

