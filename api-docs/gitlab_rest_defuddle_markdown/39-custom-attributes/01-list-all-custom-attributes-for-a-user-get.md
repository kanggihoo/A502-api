# 01-List all custom attributes for a user [GET]

`GET /api/v4/users/{id}/custom_attributes`

Lists all custom attributes for a specified user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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

#### 404 - Not Found

