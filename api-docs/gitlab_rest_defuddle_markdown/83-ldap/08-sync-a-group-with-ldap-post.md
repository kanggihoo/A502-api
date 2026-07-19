# 08-Sync a group with LDAP [POST]

`POST /api/v4/groups/{id}/ldap_sync`

Syncs a specified group with its linked LDAP group. You must be an administrator or have the Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

