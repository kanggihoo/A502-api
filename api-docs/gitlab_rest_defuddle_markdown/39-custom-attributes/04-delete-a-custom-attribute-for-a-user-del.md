# 04-Delete a custom attribute for a user [DEL]

`DELETE /api/v4/users/{id}/custom_attributes/{key}`

Deletes a specified custom attribute for a user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `path` | Yes | The key of the custom attribute |
| `id` | `integer` | `path` | Yes | The ID of the user |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

