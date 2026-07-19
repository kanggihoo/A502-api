# 02-Download the artifacts archive from a job [GET]

`GET /api/v4/projects/{id}/jobs/{job_id}/artifacts`

This feature was introduced in GitLab 8.5

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `job_id` | `integer` | `path` | Yes | The ID of a job |
| `job_token` | `string` | `query` | No | To be used with triggers for multi-project pipelines, available only on Premium and Ultimate tiers. |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

