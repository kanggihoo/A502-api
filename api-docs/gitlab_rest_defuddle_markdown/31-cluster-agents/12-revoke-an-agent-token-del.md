# 12-Revoke an agent token [DEL]

`DELETE /api/v4/projects/{id}/cluster_agents/{agent_id}/tokens/{token_id}`

Revokes an agent token. You must have the Maintainer or Owner role to use this endpoint.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `agent_id` | `integer` | `path` | Yes | The ID of an agent |
| `token_id` | `integer` | `path` | Yes | The ID of the agent token |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

