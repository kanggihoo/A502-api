# 01-Get all labels [GET]

`GET /rest/api/3/label`

Returns a [paginated](#pagination) list of labels.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":2,\"startAt\":0,\"total\":100,\"values\":[\"performance\",\"security\"]}"
```

