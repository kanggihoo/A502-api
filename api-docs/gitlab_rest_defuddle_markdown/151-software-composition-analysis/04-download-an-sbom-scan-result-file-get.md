# 04-Download an SBOM scan result file [GET]

`GET /api/v4/jobs/{id}/sbom_scans/{sbom_digest}`

Download an SBOM scan result file

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Job's ID |
| `sbom_scan_id` | `integer` | `path` | Yes | SBOM Scan's ID |

### Responses

#### 200 - OK

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

#### 202 - Sbom Scan in progress

#### 400 - Bad request

#### 403 - Forbidden

#### 404 - Not Found

#### 410 - Sbom Scan failed

