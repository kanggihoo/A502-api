# 01-Scan a file for vulnerabilities. [POST]

`POST /api/v4/projects/{id}/security_scans/sast/{sast_endpoint}`

Scan a file for vulnerabilities.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sast_endpoint` | `any` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "file_path": string (required), // The project relative path of the file to scan
  "content": string (required), // The content of the file to scan
}
```
### Responses

#### 200 - OK

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not Found

