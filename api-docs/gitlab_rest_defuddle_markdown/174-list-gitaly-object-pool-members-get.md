# 174-List Gitaly object pool members [GET]

`GET /api/v4/internal/gitaly/object_pool_members`

List Gitaly object pool members

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `disk_paths` | `array` | `query` | Yes | The on-disk paths of the pool repositories. Limited to 500 |
| `storage` | `string` | `query` | Yes | The storage shard name |
| `upstream_only` | `boolean` | `query` | No | Return only the upstream repository |

### Responses

#### 200 - OK

#### 400 - Bad Request

