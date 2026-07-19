# 05-List all agents [GET]

`GET /api/v4/projects/{id}/cluster_agents`

Lists all agents registered for the project. You must have the Developer, Maintainer, or Owner role to use this endpoint.

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
  "id": integer,
  "name": string,
  "config_project": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
  },
  "created_at": string,
  "created_by_user_id": integer,
  "is_receptive": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

