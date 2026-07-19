# 02-Create group repository storage moves for a storage shard [POST]

`POST /api/v4/group_repository_storage_moves`

Creates repository storage moves for all groups on a specified storage shard.

### Request Body (application/json)

```json
{
  "source_storage_name": string (required), // The source storage shard
  "destination_storage_name": string, // The destination storage shard
}
```
### Responses

#### 202 - 202 Accepted

#### 400 - Bad Request

