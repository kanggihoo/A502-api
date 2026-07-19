# 01-List all protected tags [GET]

`GET /api/v4/projects/{id}/protected_tags`

Lists all protected tags for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

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

