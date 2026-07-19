# 06-List all LDAP groups [GET]

`GET /api/v4/ldap/groups`

Lists all LDAP groups on the GitLab instance. Limited to 20 results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `search` | `string` | `query` | No | Search for a specific LDAP group |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "cn": string,
}
```

#### 400 - Bad Request

