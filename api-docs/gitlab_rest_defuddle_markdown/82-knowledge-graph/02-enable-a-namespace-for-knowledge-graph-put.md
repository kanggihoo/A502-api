# 02-Enable a namespace for Knowledge Graph [PUT]

`PUT /api/v4/admin/knowledge_graph/namespaces/{id}`

This endpoint enables Knowledge Graph for a specific namespace

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the namespace |

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

#### 404 - 404 Not found

