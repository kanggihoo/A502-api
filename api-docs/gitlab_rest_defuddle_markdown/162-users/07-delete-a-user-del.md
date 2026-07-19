# 07-Delete a user [DEL]

`DELETE /api/v4/users/{id}`

Deletes a user. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |
| `hard_delete` | `boolean` | `query` | No | Whether to remove a user's contributions |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": string,
  "email": string,
  "confirmed_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

