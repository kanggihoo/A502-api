# 06-Get projects using a given workflow [GET]

`GET /rest/api/3/workflow/{workflowId}/projectUsages`

Returns a page of projects using a given workflow.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `workflowId` | `string` | `path` | Yes | The workflow ID |
| `nextPageToken` | `string` | `query` | No | The cursor for pagination |
| `maxResults` | `integer` | `query` | No | The maximum number of results to return. Must be an integer between 1 and 200. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"projects\":{\"nextPageToken\":\"eyJvIjoyfQ==\",\"values\":[{\"id\":\"1003\"}]},\"workflowId\":\"fb759d53-a3a4-45ff-9de4-547c4b638dde\"}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Invalid format of nextPageToken\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 404 - Returned if the workflow with the given ID does not exist.

