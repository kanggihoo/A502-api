# 07-List all LDAP groups by provider [GET]

`GET /api/v4/ldap/{provider}/groups`

Lists all LDAP groups for the specified provider. Limited to 20 results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `search` | `string` | `query` | No | Search for a specific LDAP group |
| `provider` | `any` | `path` | Yes |  |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "cn": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

