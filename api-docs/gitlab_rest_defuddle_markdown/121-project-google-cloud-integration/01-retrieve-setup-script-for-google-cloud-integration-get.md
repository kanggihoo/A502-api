# 01-Retrieve setup script for Google Cloud integration [GET]

`GET /api/v4/projects/{id}/google_cloud/setup/integrations.sh`

Retrieves the setup script for Google Cloud integration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `enable_google_cloud_artifact_registry` | `boolean` | `query` | No | If `true`, indicates the Google Artifact Management integration should be enabled |
| `google_cloud_artifact_registry_project_id` | `string` | `query` | No | Google Cloud Project ID for the Artifact Registry |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

