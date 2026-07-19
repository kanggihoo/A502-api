# 04-List all files in an artifacts archive [GET]

`GET /api/v4/projects/{id}/jobs/{job_id}/artifacts/tree`

Lists all files in a specified artifacts archive without extracting them.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `job_id` | `integer` | `path` | Yes | ID of a job |
| `path` | `string` | `query` | No | Path to browse in the artifacts archive. Defaults to root directory. |
| `recursive` | `boolean` | `query` | No | If `true`, return all entries recursively. |
| `job_token` | `string` | `query` | No | CI/CD job token for multi-project pipelines. Premium and Ultimate only. |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "path": string,
  "type": string,
  "size": integer,
  "mode": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

