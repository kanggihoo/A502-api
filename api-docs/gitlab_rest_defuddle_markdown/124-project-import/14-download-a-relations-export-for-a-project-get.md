# 14-Download a relations export for a project [GET]

`GET /api/v4/projects/{id}/export_relations/download`

Downloads a project relations export file.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `relation` | `string` | `query` | Yes | Project relation name |
| `batched` | `boolean` | `query` | No | Whether to download in batches |
| `batch_number` | `integer` | `query` | No | Batch number to download |

### Responses

#### 200 - OK

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 500 - Internal Server Error

#### 503 - Service unavailable

