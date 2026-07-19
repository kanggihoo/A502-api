# 04-Get all the indexed namespaces for this node [GET]

`GET /api/v4/admin/zoekt/shards/{node_id}/indexed_namespaces`

Get all the indexed namespaces for this node

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `node_id` | `integer` | `path` | Yes | The id of the Search::Zoekt::Node |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "zoekt_shard_id": integer,
  "zoekt_node_id": integer,
  "namespace_id": integer,
  "number_of_replicas_override": integer,
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

