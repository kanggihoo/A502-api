# 04-Retrieve file metadata [HEAD]

`HEAD /api/v4/projects/{id}/repository/files/{file_path}`

Retrieves metadata for a specified file in a repository.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `file_path` | `string` | `path` | Yes | The URL-encoded path to the file. |

### Request Body (application/json)

```json
{
  "ref": string (required), // The name of branch, tag or commit
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

