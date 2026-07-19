# 04-Delete LDAP group link [DEL]

`DELETE /api/v4/groups/{id}/ldap_group_links/{cn}`

Deletes an LDAP group link. Deprecated. Scheduled for removal in a future release.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `cn` | `string` | `path` | Yes | The CN of a LDAP group |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

