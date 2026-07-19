# 13-Update a URL variable [PUT]

`PUT /api/v4/hooks/{hook_id}/url_variables/{key}`

Updates a URL variable for a specified webhook.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `integer` | `path` | Yes | The ID of the hook |
| `key` | `string` | `path` | Yes | The key of the variable |

### Request Body (application/json)

```json
{
  "value": string (required), // The value of the variable
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

