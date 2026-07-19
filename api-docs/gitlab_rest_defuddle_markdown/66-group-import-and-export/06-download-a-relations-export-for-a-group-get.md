# 06-Download a relations export for a group [GET]

`GET /api/v4/groups/{id}/export_relations/download`

Downloads a group relations export file.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `relation` | `string` | `query` | Yes | Group relation name |
| `batched` | `boolean` | `query` | No | Whether to download in batches |
| `batch_number` | `integer` | `query` | No | Batch number to download |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 503 - Service unavailable

