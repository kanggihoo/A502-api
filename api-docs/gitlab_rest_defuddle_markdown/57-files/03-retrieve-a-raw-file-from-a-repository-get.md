# 03-Retrieve a raw file from a repository [GET]

`GET /api/v4/projects/{id}/repository/files/{file_path}/raw`

Retrieves the raw file contents for a specified file in a repository.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `file_path` | `string` | `path` | Yes | The URL-encoded path to the file. |
| `ref` | `string` | `query` | No | The name of branch, tag or commit |
| `lfs` | `boolean` | `query` | No | Retrieve binary data for a file that is an lfs pointer |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

