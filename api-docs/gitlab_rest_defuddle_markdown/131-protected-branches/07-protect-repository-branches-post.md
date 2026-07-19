# 07-Protect repository branches [POST]

`POST /api/v4/projects/{id}/protected_branches`

Protects a specified repository branch or several project repository branches using a wildcard protected branch.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the protected branch
  "push_access_level": enum(30 | 40 | 60 | 0), // Access levels allowed to push (defaults: `40`, maintainer access level)
  "merge_access_level": enum(30 | 40 | 60 | 0), // Access levels allowed to merge (defaults: `40`, maintainer access level)
  "allow_force_push": boolean, // Allow force push for all users with push access.
  "unprotect_access_level": enum(30 | 40 | 60), // Access levels allowed to unprotect (defaults: `40`, maintainer access level)
  "allowed_to_push": [
    {}
  ], // Array of users, groups, deploy keys, or access levels allowed to push to protected branches
  "allowed_to_merge": [
    {}
  ], // Array of users, groups, or access levels allowed to merge protected branches
  "allowed_to_unprotect": [
    {}
  ], // Array of users, groups, or access levels allowed to unprotect protected branches
  "code_owner_approval_required": boolean, // Prevent pushes to this branch if it matches an item in CODEOWNERS
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "push_access_levels": [
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
  "merge_access_levels": [
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
  "allow_force_push": boolean,
  "unprotect_access_levels": [
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
  "code_owner_approval_required": boolean,
  "inherited": boolean,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 404 - 404 Project Not Found

#### 409 - Protected branch 'main' already exists

#### 422 - name is missing

