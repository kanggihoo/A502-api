# 06-Remove a namespace from a node for Zoekt indexing [DEL]

`DELETE /api/v4/admin/zoekt/shards/{node_id}/indexed_namespaces/{namespace_id}`

Remove a namespace from a node for Zoekt indexing

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `node_id` | `integer` | `path` | Yes | The id of the Search::Zoekt::Node |
| `namespace_id` | `integer` | `path` | Yes | The id of the namespace you want to remove from this node |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

