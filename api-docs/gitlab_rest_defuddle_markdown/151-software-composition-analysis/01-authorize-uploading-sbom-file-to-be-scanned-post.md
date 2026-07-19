# 01-Authorize uploading SBOM file to be scanned [POST]

`POST /api/v4/jobs/{id}/sbom_scans/authorize`

Authorize uploading SBOM file to be scanned

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Job's ID |

### Request Body (application/json)

```json
{
  "filesize": integer, // Size of artifact file
}
```
### Responses

#### 200 - SBOM Upload allowed

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

#### 413 - File too large

