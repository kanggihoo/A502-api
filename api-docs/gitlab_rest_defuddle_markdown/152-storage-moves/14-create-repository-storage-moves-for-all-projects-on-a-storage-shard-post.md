# 14-Create repository storage moves for all projects on a storage shard [POST]

`POST /api/v4/project_repository_storage_moves`

Creates repository storage moves for each project repository stored on the source storage shard. This endpoint migrates all projects at once.

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

