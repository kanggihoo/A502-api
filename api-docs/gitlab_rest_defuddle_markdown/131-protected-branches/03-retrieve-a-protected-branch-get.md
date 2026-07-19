# 03-Retrieve a protected branch [GET]

`GET /api/v4/groups/{id}/protected_branches/{name}`

Retrieves a specified protected branch. Retrieve multiple branches by using a wildcard in the `name`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of a group |
| `name` | `string` | `path` | Yes | The name of the branch or wildcard |

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

