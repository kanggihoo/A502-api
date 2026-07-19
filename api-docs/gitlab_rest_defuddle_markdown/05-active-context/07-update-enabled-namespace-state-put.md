# 07-Update enabled namespace state [PUT]

`PUT /api/v4/admin/active_context/code/enabled_namespaces`

Update enabled namespace state

### Request Body (application/json)

```json
{
  "namespace_id": any (required),
  "state": enum("pending" | "ready") (required), // State (pending or ready)
  "connection_id": integer, // Connection ID (defaults to active connection)
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "namespace_id": integer,
  "connection_id": integer,
  "state": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

