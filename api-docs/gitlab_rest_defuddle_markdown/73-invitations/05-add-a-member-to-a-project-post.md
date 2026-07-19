# 05-Add a member to a project [POST]

`POST /api/v4/projects/{id}/invitations`

Adds a member to a project. You can specify a user ID or invite a user by email.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |

### Request Body (application/json)

```json
{
  "access_level": enum(10 | 15 | 20 | 25 | 30 | 40 | 50 | 5) (required), // A valid access level (defaults: `30`, developer access level)
  "email": [
    string
  ], // The email address to invite, or multiple emails separated by comma
  "user_id": [
    string
  ], // The user ID of the new member or multiple IDs separated by commas.
  "expires_at": string, // Date string in the format YEAR-MONTH-DAY
  "invite_source": string, // Source that triggered the member creation process
  "member_role_id": integer, // The ID of a member role for the invited user
}
```
### Responses

#### 201 - Created

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

