# 30-Share a project with a group [POST]

`POST /api/v4/projects/{id}/share`

Shares a specified project with a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "group_id": integer (required), // The ID of a group
  "group_access": enum(10 | 15 | 20 | 25 | 30 | 40 | 50) (required), // The group access level
  "expires_at": string, // Share expiration date
  "member_role_id": integer, // The ID of the Member Role to be assigned to the group
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "group_id": integer,
  "group_access": integer,
  "expires_at": string,
  "member_role_id": integer,
}
```

#### 400 - Bad request

#### 403 - Unauthenticated

#### 404 - Not found

