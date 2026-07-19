# 06-Create an agent [POST]

`POST /api/v4/projects/{id}/cluster_agents`

Creates an agent for the project. You must have the Maintainer or Owner role to use this endpoint.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the agent
}
```
### Responses

#### 201 - Created

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

