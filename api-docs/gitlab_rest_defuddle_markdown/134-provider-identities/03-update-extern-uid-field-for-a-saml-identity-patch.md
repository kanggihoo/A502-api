# 03-Update `extern_uid` field for a SAML identity [PATCH]

`PATCH /api/v4/groups/{id}/saml/{uid}`

Updates the `extern_uid` field for a specified SAML identity.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `uid` | `string` | `path` | Yes | Current external UID of the user |

### Request Body (application/json)

```json
{
  "extern_uid": string (required), // Desired/new external UID of the user
}
```
### Responses

#### 200 - OK

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

