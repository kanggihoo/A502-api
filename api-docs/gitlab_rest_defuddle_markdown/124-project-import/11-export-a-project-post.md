# 11-Export a project [POST]

`POST /api/v4/projects/{id}/export`

Exports a project. Use the `upload` hash parameter to upload the exported project to a web server or any S3-compatible platform.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "description": string, // Override the project description
  "upload": {
    "url": string, // The URL to upload the project
    "http_method": enum("PUT" | "POST"), // HTTP method to upload the exported project
  }, // Object that contains information on the upload
  "excluded_relations": [
    string
  ], // List of project relation names to exclude from the export (e.g. ["merge_requests", "issues"])
}
```
### Responses

#### 202 - Accepted

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 429 - Too many requests

#### 503 - Service unavailable

