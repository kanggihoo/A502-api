# 01-Create external status check service [POST]

`POST /api/v4/projects/{id}/external_status_checks`

Creates an external status check service for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // Display name of external status check
  "shared_secret": string, // HMAC shared secret
  "external_url": string (required), // URL of external status check resource
  "protected_branch_ids": [
    integer
  ], // IDs of protected branches to scope the rule by
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "project_id": integer,
  "external_url": string,
  "protected_branches": [
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
  ],
  "hmac": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

