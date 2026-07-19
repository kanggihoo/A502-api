# 10-Retrieve a custom attribute for a group [GET]

`GET /api/v4/groups/{id}/custom_attributes/{key}`

Retrieves a specified custom attribute for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `path` | Yes | The key of the custom attribute |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "value": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

