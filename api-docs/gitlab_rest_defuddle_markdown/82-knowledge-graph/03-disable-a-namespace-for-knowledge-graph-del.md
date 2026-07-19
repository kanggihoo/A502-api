# 03-Disable a namespace for Knowledge Graph [DEL]

`DELETE /api/v4/admin/knowledge_graph/namespaces/{id}`

This endpoint disables Knowledge Graph for a specific namespace

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the namespace |

### Responses

#### 204 - No Content

#### 400 - 400 Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

