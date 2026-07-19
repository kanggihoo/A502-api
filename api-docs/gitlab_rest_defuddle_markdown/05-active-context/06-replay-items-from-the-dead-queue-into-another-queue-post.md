# 06-Replay items from the dead queue into another queue [POST]

`POST /api/v4/admin/active_context/dead_queue/replay`

Replay items from the dead queue into another queue

### Request Body (application/json)

```json
{
  "queue": string (required), // Target queue name (e.g. retry_queue, code, code_backfill)
}
```
### Responses

#### 201 - Created

#### 400 - 400 Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

