# 01-List all protected environments for a project [GET]

`GET /api/v4/projects/{id}/protected_environments`

Lists all protected environments for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

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

