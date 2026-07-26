# 01-Get channel bookmarks for Channel [GET]

`GET /api/v4/channels/{channel_id}/bookmarks`

__Minimum server version__: 9.5


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `bookmarks_since` | `number` | `query` | No | Timestamp to filter the bookmarks with. If set, the<br>endpoint returns bookmarks that have been added, updated<br>or deleted since its value<br> |

### Responses

#### 200 - Channel Bookmarks retrieval successful

Schema (application/json):
```json
[
  any
]
```

#### 400 - 

#### 401 - 

#### 403 - 

