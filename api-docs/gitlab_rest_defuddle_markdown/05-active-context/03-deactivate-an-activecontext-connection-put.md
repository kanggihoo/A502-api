# 03-Deactivate an ActiveContext connection [PUT]

`PUT /api/v4/admin/active_context/connections/deactivate`

Deactivate an ActiveContext connection

### Request Body (application/json)

```json
{
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
  "adapter_class": string,
  "prefix": string,
  "active": boolean,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

