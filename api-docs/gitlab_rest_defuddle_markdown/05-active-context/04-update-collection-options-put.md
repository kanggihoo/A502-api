# 04-Update collection options [PUT]

`PUT /api/v4/admin/active_context/collections/{id}`

Update collection options

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | Collection name or ID |

### Request Body (application/json)

```json
{
  "queue_shard_count": integer, // Number of queue shards
  "queue_shard_limit": integer, // Queue shard limit
  "connection_id": integer, // Connection ID (defaults to active connection)
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "connection_id": integer,
  "options": {},
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

#### 422 - 422 Unprocessable entity

