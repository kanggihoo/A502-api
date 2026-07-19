# 03-Reuse sbom scan results if scans for sboms with given digest already exist [POST]

`POST /api/v4/jobs/{id}/sbom_scans/{sbom_digest}`

Reuse sbom scan results if scans for sboms with given digest already exist

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Job's ID |
| `sbom_digest` | `string` | `path` | Yes | The sbom digest that identifies an sbom scan uniquely |

### Request Body (application/json)

```json
{
  "purl_types": [
    any
  ] (required), // The list of purl_types that are valid for given sbom digest
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

#### 404 - Not found

#### 410 - Result no longer available

