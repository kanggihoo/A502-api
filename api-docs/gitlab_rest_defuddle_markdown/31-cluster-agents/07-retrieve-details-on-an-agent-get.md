# 07-Retrieve details on an agent [GET]

`GET /api/v4/projects/{id}/cluster_agents/{agent_id}`

Retrieves details on a specified agent. You must have the Developer, Maintainer, or Owner role to use this endpoint.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `agent_id` | `integer` | `path` | Yes | The ID of an agent |

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

