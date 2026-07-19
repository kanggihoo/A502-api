# 09-Get raw snippet file contents from the repository [GET]

`GET /api/v4/snippets/{id}/files/{ref}/{file_path}/raw`

Get raw snippet file contents from the repository

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `file_path` | `string` | `path` | Yes | The URL-encoded path to the file, like lib%2Fclass%2Erb |
| `ref` | `string` | `path` | Yes | The name of branch, tag or commit |
| `id` | `string` | `path` | Yes | The ID of a snippet |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not found

