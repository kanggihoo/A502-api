# 08-Delete priority [DELETE]

`DELETE /rest/api/3/priority/{id}`

Deletes an issue priority.

This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue priority. |

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

#### 400 - Returned if the request isn't valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The newPriority has to be provided.\"],\"errors\":{}}"
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

#### 404 - Returned if the issue priority isn't found.

Example (application/json):
```json
"{\"errorMessages\":[\"Priority with ID 10000 not found.\"],\"errors\":{}}"
```

#### 409 - Returned if a task to delete the issue priority is already running.

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

