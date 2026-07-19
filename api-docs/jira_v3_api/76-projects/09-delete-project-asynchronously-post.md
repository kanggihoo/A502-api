# 09-Delete project asynchronously [POST]

`POST /rest/api/3/project/{projectIdOrKey}/delete`

Deletes a project asynchronously.

This operation is:

 *  transactional, that is, if part of the delete fails the project is not deleted.
 *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |

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

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the project is not found or the user does not have the necessary permission.

