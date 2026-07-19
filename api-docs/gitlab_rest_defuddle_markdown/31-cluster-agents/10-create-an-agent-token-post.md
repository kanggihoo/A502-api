# 10-Create an agent token [POST]

`POST /api/v4/projects/{id}/cluster_agents/{agent_id}/tokens`

Creates a token for an agent. You must have the Maintainer or Owner role to use this endpoint. An agent can have only two active tokens at one time.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `agent_id` | `integer` | `path` | Yes | The ID of an agent |

### Request Body (application/json)

```json
{
  "name": string (required), // The name for the token
  "description": string, // The description for the token
}
```
### Responses

#### 201 - Created

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
  "token": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

