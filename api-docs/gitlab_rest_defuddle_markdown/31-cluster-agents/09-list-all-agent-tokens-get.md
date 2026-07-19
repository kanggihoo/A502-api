# 09-List all agent tokens [GET]

`GET /api/v4/projects/{id}/cluster_agents/{agent_id}/tokens`

Lists all active tokens for an agent. You must have the Developer, Maintainer, or Owner role to use this endpoint.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `agent_id` | `integer` | `path` | Yes | The ID of an agent |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "description": string,
  "agent_id": integer,
  "status": string,
  "created_at": string,
  "created_by_user_id": integer,
}
```

#### 400 - Bad Request

#### 404 - Not Found

