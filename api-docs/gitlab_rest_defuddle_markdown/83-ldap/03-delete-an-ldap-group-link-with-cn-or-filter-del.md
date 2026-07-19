# 03-Delete an LDAP group link with CN or filter [DEL]

`DELETE /api/v4/groups/{id}/ldap_group_links`

Deletes an LDAP group link using a CN or filter.Deleting by filter is only supported in the Premium tier and above.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `cn` | `string` | `query` | No | The CN of a LDAP group |
| `filter` | `string` | `query` | No | The LDAP filter for the group |
| `provider` | `string` | `query` | Yes | LDAP provider for the LDAP group link |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

