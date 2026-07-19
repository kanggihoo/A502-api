# 01-Lists SAML group links [GET]

`GET /api/v4/groups/{id}/saml_group_links`

Get SAML group links for a group

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the group |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "access_level": integer,
  "member_role_id": integer,
  "provider": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

