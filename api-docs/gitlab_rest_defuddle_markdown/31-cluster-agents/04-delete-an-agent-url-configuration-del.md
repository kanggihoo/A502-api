# 04-Delete an agent URL configuration [DEL]

`DELETE /api/v4/projects/{id}/cluster_agents/{agent_id}/url_configurations/{url_configuration_id}`

Deletes an agent URL configuration. You must have the Maintainer or Owner role to use this endpoint. This feature was introduced in GitLab 17.4.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `agent_id` | `integer` | `path` | Yes | The ID of an agent |
| `url_configuration_id` | `integer` | `path` | Yes | The ID of the agent url configuration |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

