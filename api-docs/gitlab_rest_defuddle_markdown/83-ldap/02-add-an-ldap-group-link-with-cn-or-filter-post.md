# 02-Add an LDAP group link with CN or filter [POST]

`POST /api/v4/groups/{id}/ldap_group_links`

Adds an LDAP group link using a CN or filter.Adding a group link by filter is only supported in the Premium tier and above.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "cn": string, // The CN of a LDAP group
  "filter": string, // The LDAP filter for the group
  "group_access": enum(5 | 10 | 15 | 20 | 25 | 30 | 40 | 50) (required), // Access level for members of the LDAP group
  "provider": string (required), // LDAP provider for the LDAP group link
  "member_role_id": integer, // The ID of the Member Role for members of the LDAP group
}
```
### Responses

#### 201 - Created

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

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

