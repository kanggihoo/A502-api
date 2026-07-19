# 16-Authorize Debian package upload [PUT]

`PUT /api/v4/projects/{id}/packages/debian/{file_name}/authorize`

This feature was introduced in GitLab 13.5

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `file_name` | `string` | `path` | Yes | The filename |

### Request Body (application/json)

```json
{
  "distribution": string, // The Debian Codename or Suite
  "component": string (required), // The Debian Component
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

