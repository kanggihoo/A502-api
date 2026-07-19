# 03-Switch workflow scheme for project [POST]

`POST /rest/api/3/workflowscheme/project/switch`

Switches a workflow scheme for a project.

Workflow schemes can only be assigned to classic projects.

**Calculating required mappings:** If statuses from the current workflow scheme won't exist in the target workflow scheme, you must provide `mappingsByIssueTypeOverride` to specify how issues with those statuses should be migrated. Use [the required workflow scheme mappings API](#api-rest-api-3-workflowscheme-update-mappings-post) to determine which statuses and issue types require mappings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "mappingsByIssueTypeOverride": [
    {
      "issueTypeId": string,
      "statusMappings": [
        {
          "newStatusId": string,
          "oldStatusId": string,
        }
      ],
    }
  ], // The mappings for migrating issues from old statuses to new statuses when switching from one workflow scheme to another. This field is required if any statuses in the current project's workflows would no longer exist in the target workflow scheme. Each mapping defines how to update issues from an old status to the corresponding new status in the issue’s new workflow.
  "projectId": string, // The ID of the project to switch the workflow scheme for
  "targetSchemeId": string, // The ID of the target workflow scheme to switch to
}
```
### Responses

#### 303 - Returned if the request is successful and the task has been started.

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

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 409 - Returned if a conflicting task is already running.

Example (application/json):
```json
"{\"errorMessages\":[\"Another task is currently running, please try again later.\"],\"errors\":{\"conflictingTaskId\":\"10000\"}}"
```

