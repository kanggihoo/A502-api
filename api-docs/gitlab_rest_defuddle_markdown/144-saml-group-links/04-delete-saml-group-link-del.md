# 04-Delete SAML group link [DEL]

`DELETE /api/v4/groups/{id}/saml_group_links/{saml_group_name}`

Deletes a SAML group link for the group

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the group |
| `saml_group_name` | `string` | `path` | Yes | Name of a SAML group |
| `provider` | `string` | `query` | No | Provider string to disambiguate when multiple links exist with same name |

### Responses

#### 204 - No Content

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

#### 404 - Not found

#### 422 - Multiple links found, provider parameter required

