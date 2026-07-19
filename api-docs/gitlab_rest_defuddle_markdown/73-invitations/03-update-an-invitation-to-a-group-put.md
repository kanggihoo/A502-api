# 03-Update an invitation to a group [PUT]

`PUT /api/v4/groups/{id}/invitations/{email}`

Updates a pending invitation to a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The group ID |
| `email` | `string` | `path` | Yes | The email address of the invitation |

### Request Body (application/json)

```json
{
  "access_level": enum(10 | 15 | 20 | 25 | 30 | 40 | 50), // A valid access level (defaults: `30`, developer access level)
  "expires_at": string, // Date string in ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`)
  "member_role_id": integer, // The ID of a member role for the invited user
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "access_level": string,
  "created_at": string,
  "expires_at": string,
  "invite_email": string,
  "invite_token": string,
  "user_name": string,
  "created_by_name": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

