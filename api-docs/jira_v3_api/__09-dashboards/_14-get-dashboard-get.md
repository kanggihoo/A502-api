# 14-Get dashboard [GET]

`GET /rest/api/3/dashboard/{id}`

Returns a dashboard.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

However, to get a dashboard, the dashboard must be shared with the user or the user must own it. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the dashboard. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"10000\",\"isFavourite\":false,\"name\":\"System Dashboard\",\"popularity\":1,\"self\":\"https://your-domain.atlassian.net/rest/api/3/dashboard/10000\",\"sharePermissions\":[{\"type\":\"global\"}],\"view\":\"https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000\"}"
```

#### 400 - 400 response

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

#### 404 - Returned if the dashboard is not found or the dashboard is not owned by or shared with the user.

