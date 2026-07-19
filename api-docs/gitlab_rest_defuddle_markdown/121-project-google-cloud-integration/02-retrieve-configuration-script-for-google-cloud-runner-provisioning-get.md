# 02-Retrieve configuration script for Google Cloud runner provisioning [GET]

`GET /api/v4/projects/{id}/google_cloud/setup/runner_deployment_project.sh`

Retrieves the configuration script for Google Cloud runner provisioning.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `google_cloud_project_id` | `string` | `query` | Yes | ID of the Google Cloud project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

