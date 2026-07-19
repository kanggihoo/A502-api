# 09-Get workflow usages by status [GET]

`GET /rest/api/3/statuses/{statusId}/workflowUsages`

Returns a page of workflows using a given status.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `statusId` | `string` | `path` | Yes | The statusId to fetch workflow usages for |
| `nextPageToken` | `string` | `query` | No | The cursor for pagination |
| `maxResults` | `integer` | `query` | No | The maximum number of results to return. Must be an integer between 1 and 200. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"statusId\":\"1000\",\"workflows\":{\"nextPageToken\":\"eyJvIjoyfQ==\",\"values\":[{\"id\":\"545d80a3-91ff-4949-8b0d-a2bc484e70e5\"}]}}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Invalid format of nextPageToken\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 404 - Returned if the status with the given ID does not exist.

