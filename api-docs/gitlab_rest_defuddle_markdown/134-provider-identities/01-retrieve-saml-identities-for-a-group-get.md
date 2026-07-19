# 01-Retrieve SAML identities for a group [GET]

`GET /api/v4/groups/{id}/saml/identities`

Retrieves SAML identities for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

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

