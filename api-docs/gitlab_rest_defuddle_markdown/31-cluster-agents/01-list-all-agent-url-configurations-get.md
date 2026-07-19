# 01-List all agent URL configurations [GET]

`GET /api/v4/projects/{id}/cluster_agents/{agent_id}/url_configurations`

Lists all agent URL configurations for a specified agent. You must have the Developer, Maintainer, or Owner role to use this endpoint. This feature was introduced in GitLab 17.4.

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
  "agent_id": integer,
  "url": string,
  "public_key": string,
  "client_cert": string,
  "ca_cert": string,
  "tls_host": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

