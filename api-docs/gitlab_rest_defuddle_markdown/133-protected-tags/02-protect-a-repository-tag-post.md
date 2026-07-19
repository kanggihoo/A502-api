# 02-Protect a repository tag [POST]

`POST /api/v4/projects/{id}/protected_tags`

Protects a specified repository tag using a wildcard protected tag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the protected tag
  "create_access_level": enum(30 | 40 | 60 | 0), // Access levels allowed to create (defaults: `40`, maintainer access level)
  "allowed_to_create": [
    {}
  ], // Array of users, groups, deploy keys, or access levels allowed to create protected branches
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "name": string,
  "create_access_levels": [
    {
      "id": integer,
      "access_level": integer,
      "access_level_description": string,
      "deploy_key_id": integer,
      "user_id": integer,
      "group_id": integer,
      "member_role_id": integer,
      "member_role_name": string,
    }
  ],
}
```

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

#### 422 - Unprocessable entity

