# 08-Schedule repository storage moves for all snippets on a storage shard [POST]

`POST /api/v4/snippet_repository_storage_moves`

Schedules repository storage moves for each snippet repository stored on the source storage shard. This endpoint migrates all snippets at once.

### Request Body (application/json)

```json
{
  "source_storage_name": string (required), // The source storage shard
  "destination_storage_name": string, // The destination storage shard
}
```
### Responses

#### 202 - Accepted

#### 400 - Bad Request

