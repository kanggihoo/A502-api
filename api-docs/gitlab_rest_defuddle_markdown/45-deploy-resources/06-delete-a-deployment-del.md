# 06-Delete a deployment [DEL]

`DELETE /api/v4/projects/{id}/deployments/{deployment_id}`

Deletes a specified deployment that is not currently the last deployment for an environment or in a `running` state.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `deployment_id` | `integer` | `path` | Yes | The ID of the deployment |

### Responses

#### 204 - Deployment destroyed

#### 400 - "Cannot destroy running deployment" or "Deployment currently deployed to environment"

#### 403 - Forbidden

#### 404 - Not Found

