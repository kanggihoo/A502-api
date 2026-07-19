# 05-Retrieve a file from a repository [GET]

`GET /api/v4/projects/{id}/repository/files/{file_path}`

Retrieves information about a specified file in a repository. This includes information like the name, size, and the file contents. File content is Base64 encoded.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `file_path` | `string` | `path` | Yes | The URL-encoded path to the file. |
| `ref` | `string` | `query` | Yes | The name of branch, tag or commit |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

