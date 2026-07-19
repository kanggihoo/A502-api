# 02-Add SAML group link [POST]

`POST /api/v4/groups/{id}/saml_group_links`

Add a SAML group link for a group

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "saml_group_name": string (required), // The name of a SAML group
  "access_level": enum(5 | 10 | 15 | 20 | 25 | 30 | 40 | 50) (required), // Level of permissions for the linked SA group
  "member_role_id": integer, // The ID of the Member Role for the linked SA group
  "provider": string, // Provider string that must match for this group link to be applied
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "name": string,
  "access_level": integer,
  "member_role_id": integer,
  "provider": string,
}
```

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

