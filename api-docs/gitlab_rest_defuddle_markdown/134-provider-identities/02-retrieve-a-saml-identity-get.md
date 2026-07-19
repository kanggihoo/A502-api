# 02-Retrieve a SAML identity [GET]

`GET /api/v4/groups/{id}/saml/{uid}`

Retrieves a specified SAML identity.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `uid` | `string` | `path` | Yes | External UID of the user |

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

