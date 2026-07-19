# 05-Add a namespace to a node for Zoekt indexing [PUT]

`PUT /api/v4/admin/zoekt/shards/{node_id}/indexed_namespaces/{namespace_id}`

Add a namespace to a node for Zoekt indexing

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `node_id` | `integer` | `path` | Yes | The id of the Search::Zoekt::Node |
| `namespace_id` | `integer` | `path` | Yes | The id of the namespace you want to index in this node |

### Request Body (application/json)

```json
{
  "search": boolean, // Whether or not an indexed namespace should be enabled for searching
}
```
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

