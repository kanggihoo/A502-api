# 02-Update the number of replicas override for an enabled namespace [PATCH]

`PATCH /api/v4/admin/zoekt/namespaces/{id}`

Update the number of replicas override for an enabled namespace

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the namespace |

### Request Body (application/json)

```json
{
  "number_of_replicas_override": integer, // The number of replicas override to set (nil to unset)
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

#### 400 - 400 Bad Request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Not found

