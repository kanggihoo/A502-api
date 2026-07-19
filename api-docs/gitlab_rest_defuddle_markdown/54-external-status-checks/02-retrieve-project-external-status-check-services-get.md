# 02-Retrieve project external status check services [GET]

`GET /api/v4/projects/{id}/external_status_checks`

Retrieves information on external status check services for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

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

