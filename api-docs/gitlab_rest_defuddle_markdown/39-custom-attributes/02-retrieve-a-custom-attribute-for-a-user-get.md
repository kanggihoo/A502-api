# 02-Retrieve a custom attribute for a user [GET]

`GET /api/v4/users/{id}/custom_attributes/{key}`

Retrieves a specified custom attribute for a user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `path` | Yes | The key of the custom attribute |
| `id` | `integer` | `path` | Yes | The ID of the user |

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

