# 10-Get dashboard item property keys [GET]

`GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties`

Returns the keys of all properties for a dashboard item.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** The user must have read permission of the dashboard or have the dashboard shared with them.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `dashboardId` | `string` | `path` | Yes | The ID of the dashboard. |
| `itemId` | `string` | `path` | Yes | The ID of the dashboard item. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"keys\":[{\"key\":\"issue.support\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

#### 404 - Returned if the dashboard or dashboard item is not found, or the dashboard is not owned by or shared with the user.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

