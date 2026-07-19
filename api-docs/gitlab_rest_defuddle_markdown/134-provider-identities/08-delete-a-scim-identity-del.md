# 08-Delete a SCIM identity [DEL]

`DELETE /api/v4/groups/{id}/scim/{uid}`

Deletes a specified SCIM identity.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `uid` | `string` | `path` | Yes | Current external UID of the user |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "extern_uid": string,
  "user_id": string,
  "active": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

