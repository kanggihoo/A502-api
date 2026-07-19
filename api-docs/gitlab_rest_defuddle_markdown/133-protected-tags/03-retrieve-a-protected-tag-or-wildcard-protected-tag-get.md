# 03-Retrieve a protected tag or wildcard protected tag [GET]

`GET /api/v4/projects/{id}/protected_tags/{name}`

Retrieves a specified protected tag or wildcard protected tag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `name` | `string` | `path` | Yes | The name of the tag or wildcard |

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

