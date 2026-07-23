# 04-Update a protected branch [PATCH]

`PATCH /api/v4/groups/{id}/protected_branches/{name}`

Updates a protected branch for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of a group |
| `name` | `string` | `path` | Yes | The name of the branch |

### Request Body (application/json)

```json
{
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

#### 200 - OK

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
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 404 - 404 ProtectedBranch Not Found

#### 422 - Push access levels access level has already been taken

