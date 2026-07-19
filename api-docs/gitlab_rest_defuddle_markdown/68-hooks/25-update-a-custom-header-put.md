# 25-Update a custom header [PUT]

`PUT /api/v4/projects/{id}/hooks/{hook_id}/custom_headers/{key}`

Updates a custom header for a specified webhook.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `integer` | `path` | Yes | The ID of the hook |
| `key` | `string` | `path` | Yes | The name of the custom header |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "value": string (required), // The value of the custom header
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

