# 02-Protect an environment for a project [POST]

`POST /api/v4/projects/{id}/protected_environments`

Protects a specified environment for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the environment
  "required_approval_count": integer, // [DEPRECATED] The number of approvals required to deploy to this environment
  "deploy_access_levels": [
    {
      "user_id": integer, // The ID of a user with access to the project
      "group_id": integer, // The ID of a group with access to the project
      "group_inheritance_type": enum(0 | 1), // Specify whether to take inherited group membership into account. Use `0` for direct group membership or `1` for all inherited groups. Default is `0`
      "access_level": enum(40 | 30 | 20 | 60), // The access levels allowed to deploy
    }
  ] (required), // Array of access levels allowed to deploy, with each described by a hash. One of `user_id`, `group_id` or `access_level`. They take the form of `{user_id: integer}`, `{group_id: integer}` or `{access_level: integer}` respectively.
  "approval_rules": [
    {
      "user_id": integer, // The ID of a user with access to the project
      "group_id": integer, // The ID of a group with access to the project
      "group_inheritance_type": enum(0 | 1), // Specify whether to take inherited group membership into account. Use `0` for direct group membership or `1` for all inherited groups. Default is `0`
      "id": integer, // The ID of the approval rule to update
      "_destroy": boolean, // Deletes the object when true
      "access_level": enum(40 | 30 | 20 | 60), // The access levels allowed to approve
      "required_approvals": integer, // The number of approvals required for this rule
    }
  ], // Array of access levels allowed to approve, with each described by a hash. One of `user_id`, `group_id` or `access_level`. They take the form of `{user_id: integer}`, `{group_id: integer}` or `{access_level: integer}` respectively. You can also specify the number of required approvals from the specified entity with `required_approvals` field.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "name": string,
  "deploy_access_levels": {
    "id": integer,
    "access_level": integer,
    "access_level_description": string,
    "deploy_key_id": integer,
    "user_id": integer,
    "group_id": integer,
    "member_role_id": integer,
    "member_role_name": string,
    "group_inheritance_type": integer,
  },
  "required_approval_count": integer,
  "approval_rules": {
    "id": integer,
    "user_id": integer,
    "group_id": integer,
    "access_level": integer,
    "access_level_description": string,
    "required_approvals": integer,
    "group_inheritance_type": integer,
  },
}
```

#### 400 - Bad Request

#### 404 - Not found

#### 409 - Conflict

#### 422 - Unprocessable entity

