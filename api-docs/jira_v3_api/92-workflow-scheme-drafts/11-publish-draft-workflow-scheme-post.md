# 11-Publish draft workflow scheme [POST]

`POST /rest/api/3/workflowscheme/{id}/draft/publish`

Publishes a draft workflow scheme.

Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to update issues with the original workflow status to the new workflow status.

This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow scheme that the draft belongs to. |
| `validateOnly` | `boolean` | `query` | No | Whether the request only performs a validation. |

### Request Body (application/json)

```json
{
  "statusMappings": [
    {
      "issueTypeId": string (required), // The ID of the issue type.
      "newStatusId": string (required), // The ID of the new status.
      "statusId": string (required), // The ID of the status.
    }
  ], // Mappings of statuses to new statuses for issue types.
}
```
### Responses

#### 204 - Returned if the request is only for validation and is successful.

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
"{\"errorMessages\":[\"Issue type with ID '2','4' is missing the mappings required for statuses with IDs 10004.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if any of these are true:

 *  The workflow scheme is not found.
 *  The workflow scheme does not have a draft.
 *  A new status in the draft workflow scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"Draft workflow scheme was not found.\"],\"errors\":{}}"
```

