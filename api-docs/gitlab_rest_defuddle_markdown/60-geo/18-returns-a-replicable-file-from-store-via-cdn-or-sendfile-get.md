# 18-Returns a replicable file from store (via CDN or sendfile) [GET]

`GET /api/v4/geo/retrieve/{replicable_name}/{replicable_id}`

Returns a replicable file from store (via CDN or sendfile)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `replicable_name` | `string` | `path` | Yes | The replicable name of a replicator instance |
| `replicable_id` | `integer` | `path` | Yes | The replicable ID of a replicable instance |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 404 - 404 Not found

