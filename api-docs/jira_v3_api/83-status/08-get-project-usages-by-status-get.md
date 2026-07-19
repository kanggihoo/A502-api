# 08-Get project usages by status [GET]

`GET /rest/api/3/statuses/{statusId}/projectUsages`

Returns a page of projects using a given status.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `statusId` | `string` | `path` | Yes | The statusId to fetch project usages for |
| `nextPageToken` | `string` | `query` | No | The cursor for pagination |
| `maxResults` | `integer` | `query` | No | The maximum number of results to return. Must be an integer between 1 and 200. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"projects\":{\"nextPageToken\":\"eyJvIjoyfQ==\",\"values\":[{\"id\":\"1000\"}]},\"statusId\":\"1000\"}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Invalid format of nextPageToken\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 404 - Returned if the status with the given ID does not exist.

