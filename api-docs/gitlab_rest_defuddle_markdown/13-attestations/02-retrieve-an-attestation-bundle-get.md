# 02-Retrieve an attestation bundle [GET]

`GET /api/v4/projects/{id}/attestations/{attestation_iid}/download`

This feature was introduced in GitLab 18.7

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `attestation_iid` | `any` | `path` | Yes | The iid of the attestation |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Artifact SHA-256 not found

