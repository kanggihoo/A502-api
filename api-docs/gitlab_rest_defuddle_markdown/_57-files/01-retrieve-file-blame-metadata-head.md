# 01-Retrieve file blame metadata [HEAD]

`HEAD /api/v4/projects/{id}/repository/files/{file_path}/blame`

Retrieves blame metadata for lines in a specified file.

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

