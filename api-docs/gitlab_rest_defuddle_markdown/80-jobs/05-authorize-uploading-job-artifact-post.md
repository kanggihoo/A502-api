# 05-Authorize uploading job artifact [POST]

`POST /api/v4/jobs/{id}/artifacts/authorize`

Authorize uploading job artifact

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Job's ID |

### Request Body (application/json)

```json
{
  "token": string, // Job's authentication token
  "filesize": integer, // Size of artifact file
  "artifact_type": enum("archive" | "metadata" | "trace" | "junit" | "sast" | "dependency_scanning" | "container_scanning" | "dast" | "codequality" | "license_scanning" | "performance" | "metrics" | "metrics_referee" | "network_referee" | "lsif" | "dotenv" | "cobertura" | "terraform" | "accessibility" | "cluster_applications" | "secret_detection" | "requirements" | "coverage_fuzzing" | "browser_performance" | "load_performance" | "api_fuzzing" | "cluster_image_scanning" | "cyclonedx" | "requirements_v2" | "annotations" | "repository_xray" | "jacoco" | "sarif"), // The type of artifact
}
```
### Responses

#### 200 - Upload allowed

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

#### 405 - Artifacts support not enabled

#### 413 - File too large

#### 429 - Too Many Requests

