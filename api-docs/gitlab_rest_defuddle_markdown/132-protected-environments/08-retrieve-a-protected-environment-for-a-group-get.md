# 08-Retrieve a protected environment for a group [GET]

`GET /api/v4/groups/{id}/protected_environments/{name}`

Retrieves a specified protected environment for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group maintained by the authenticated user |
| `name` | `string` | `path` | Yes | The deployment tier of the protected environment. One of `production`, `staging`, `testing`, `development`, or `other` |

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

