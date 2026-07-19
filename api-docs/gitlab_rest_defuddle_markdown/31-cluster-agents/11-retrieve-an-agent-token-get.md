# 11-Retrieve an agent token [GET]

`GET /api/v4/projects/{id}/cluster_agents/{agent_id}/tokens/{token_id}`

Retrieves a specified agent token. You must have the Developer, Maintainer, or Owner role to use this endpoint. Returns a `404` if the agent token has been revoked.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `agent_id` | `integer` | `path` | Yes | The ID of an agent |
| `token_id` | `integer` | `path` | Yes | The ID of the agent token |

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
  "last_used_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

