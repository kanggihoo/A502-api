# 07-Associate security scheme to project [PUT]

`PUT /rest/api/3/issuesecurityschemes/project`

Associates an issue security scheme with a project and remaps security levels of issues to the new levels, if provided.

This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "oldToNewSecurityLevelMappings": [
    {
      "newLevelId": string (required), // The new issue security level ID. Providing null will clear the assigned old level from issues.
      "oldLevelId": string (required), // The old issue security level ID. Providing null will remap all issues without any assigned levels.
    }
  ], // The list of scheme levels which should be remapped to new levels of the issue security scheme.
  "projectId": string (required), // The ID of the project.
  "schemeId": string (required), // The ID of the issue security scheme. Providing null will clear the association with the issue security scheme.
}
```
### Responses

#### 303 - Returned if the request is successful.

Schema (application/json):
```json
{
  "description": string, // The description of the task.
  "elapsedRuntime": integer (required), // The execution time of the task, in milliseconds.
  "finished": integer, // A timestamp recording when the task was finished.
  "id": string (required), // The ID of the task.
  "lastUpdate": integer (required), // A timestamp recording when the task progress was last updated.
  "message": string, // Information about the progress of the task.
  "progress": integer (required), // The progress of the task, as a percentage complete.
  "result": any, // The result of the task execution.
  "self": string (required), // The URL of the task.
  "started": integer, // A timestamp recording when the task was started.
  "status": enum("ENQUEUED" | "RUNNING" | "COMPLETE" | "FAILED" | "CANCEL_REQUESTED" | "CANCELLED" | "DEAD") (required), // The status of the task.
  "submitted": integer (required), // A timestamp recording when the task was submitted.
  "submittedBy": integer (required), // The ID of the user who submitted the task.
}
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"some-wrong-string is not a valid value. The issue security scheme ID must be a positive integer.\"],\"errors\":{}}"
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

#### 403 - Returned if the user doesn't have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"You are not authorized to perform this action. Administrator privileges are required.\"],\"errors\":{}}"
```

#### 404 - Returned if the security scheme isn't found.

Example (application/json):
```json
"{\"errorMessages\":[\"Issue security scheme with ID 10000 not found.\"],\"errors\":{}}"
```

#### 409 - Returned if a task to remove the issue security level is already running.

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

