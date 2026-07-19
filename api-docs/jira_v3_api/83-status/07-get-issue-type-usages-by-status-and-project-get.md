# 07-Get issue type usages by status and project [GET]

`GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages`

Returns a page of issue types in a project using a given status.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `statusId` | `string` | `path` | Yes | The statusId to fetch issue type usages for |
| `projectId` | `string` | `path` | Yes | The projectId to fetch issue type usages for |
| `nextPageToken` | `string` | `query` | No | The cursor for pagination |
| `maxResults` | `integer` | `query` | No | The maximum number of results to return. Must be an integer between 1 and 200. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueTypes\":{\"nextPageToken\":\"eyJvIjoyfQ==\",\"values\":[{\"id\":\"1000\"}]},\"projectId\":\"2000\",\"statusId\":\"1000\"}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Invalid format of nextPageToken\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 404 - Returned if the status with the given ID does not exist.

