# 01-Bulk pin or unpin issue panel to projects [POST]

`POST /rest/api/3/forge/panel/action/bulk/async`

Bulk pin or unpin an issue panel (added by a Forge app) to or from multiple projects.

The operation runs asynchronously. The response includes a task ID - use the [Get task](#api-rest-api-3-task-taskId-get) endpoint to check progress.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "moduleId": string (required), // The moduleId of the Forge panel in the format `ari:cloud:ecosystem::extension/{app-id}/{environment-id}/static/{module-key}`
  "projectList": [
    {
      "action": enum("PIN" | "UNPIN") (required), // The action to perform: PIN or UNPIN.
      "projectIdOrKey": string (required), // The project ID or key.
    }
  ] (required), // The list of projects to pin or unpin the issue panel to or from.
}
```
### Responses

#### 202 - Accepted. Returns the task ID for polling progress.

Schema (application/json):
```json
{
  "taskId": string,
}
```

#### 400 - Returned if the request body is invalid.

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

#### 403 - Returned if the user does not have permission to administer Jira.

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

#### 500 - Returned if the task could not be submitted (server error).

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

