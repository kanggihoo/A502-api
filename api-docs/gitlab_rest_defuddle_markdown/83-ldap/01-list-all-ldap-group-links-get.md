# 01-List all LDAP group links [GET]

`GET /api/v4/groups/{id}/ldap_group_links`

Lists all LDAP group links.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "cn": string,
  "group_access": integer,
  "provider": string,
  "filter": string,
  "member_role_id": integer,
}
```

#### 400 - Bad Request

#### 404 - Not Found

