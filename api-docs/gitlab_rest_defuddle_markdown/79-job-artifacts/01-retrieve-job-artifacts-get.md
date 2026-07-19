# 01-Retrieve job artifacts [GET]

`GET /api/v4/projects/{id}/jobs/artifacts/{ref_name}/download`

Retrieves the artifacts archive for the latest successful job on a specified branch or tag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `ref_name` | `string` | `path` | Yes | Branch or tag name in repository. `HEAD` or `SHA` references are not supported. |
| `job` | `string` | `query` | Yes | The name of the job. |
| `job_token` | `string` | `query` | No | To be used with triggers for multi-project pipelines, available only on Premium and Ultimate tiers. |
| `search_recent_successful_pipelines` | `boolean` | `query` | No | Search across recent successful pipelines instead of just the latest one. |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

