# 02-Upload an SBOM file to be scanned [POST]

`POST /api/v4/jobs/{id}/sbom_scans`

Upload an SBOM file to be scanned

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Job's ID |

### Request Body (multipart/form-data)

```json
{
  "file": string (required), // The sbom file to upload
  "sbom_digest": string, // Digest corresponding to uploaded SBOM
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "download_url": string,
  "throttled": boolean,
  "project_throttling_resets_in": integer,
  "advisory_db_state": string,
}
```

#### 400 - Bad request

#### 403 - Forbidden

#### 404 - Not Found

#### 413 - File too large

