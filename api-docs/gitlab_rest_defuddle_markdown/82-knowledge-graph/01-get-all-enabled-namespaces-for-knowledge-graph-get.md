# 01-Get all enabled namespaces for Knowledge Graph [GET]

`GET /api/v4/admin/knowledge_graph/namespaces`

This endpoint retrieves all namespaces that have Knowledge Graph enabled

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "root_namespace_id": integer,
  "created_at": string,
}
```

#### 400 - 400 Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

