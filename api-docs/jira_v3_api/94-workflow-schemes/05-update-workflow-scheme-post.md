# 05-Update workflow scheme [POST]

`POST /rest/api/3/workflowscheme/update`

Updates company-managed and team-managed project workflow schemes. This API doesn't have a concept of draft, so any changes made to a workflow scheme are immediately available. When changing the available statuses for issue types, an [asynchronous task](#async) migrates the issues as defined in the provided mappings.

**[Permissions](#permissions) required:**

 *  *Administer Jira* project permission to update all, including global-scoped, workflow schemes.
 *  *Administer projects* project permission to update project-scoped workflow schemes.

### Request Body (application/json)

```json
{
  "defaultWorkflowId": string, // The ID of the workflow for issue types without having a mapping defined in this workflow scheme. Only used in global-scoped workflow schemes. If the `defaultWorkflowId` isn't specified, this is set to *Jira Workflow (jira)*.
  "description": string (required), // The new description for this workflow scheme.
  "id": string (required), // The ID of this workflow scheme.
  "name": string (required), // The new name for this workflow scheme.
  "statusMappingsByIssueTypeOverride": [
    {
      "issueTypeId": string,
      "statusMappings": [
        {
          "newStatusId": string,
          "oldStatusId": string,
        }
      ],
    }
  ], // Overrides, for the selected issue types, any status mappings provided in `statusMappingsByWorkflows`. Status mappings are required when the new workflow for an issue type doesn't contain all statuses that the old workflow has. Status mappings can be provided by a combination of `statusMappingsByWorkflows` and `statusMappingsByIssueTypeOverride`.
  "statusMappingsByWorkflows": [
    {
      "newWorkflowId": string (required), // The ID of the new workflow.
      "oldWorkflowId": string (required), // The ID of the old workflow.
      "statusMappings": [
        {
          "newStatusId": string,
          "oldStatusId": string,
        }
      ] (required), // The list of status mappings.
    }
  ], // The status mappings by workflows. Status mappings are required when the new workflow for an issue type doesn't contain all statuses that the old workflow has. Status mappings can be provided by a combination of `statusMappingsByWorkflows` and `statusMappingsByIssueTypeOverride`.
  "version": {
    "id": string, // The version UUID.
    "versionNumber": integer, // The version number.
  } (required),
  "workflowsForIssueTypes": [
    {
      "issueTypeIds": [
        string
      ] (required), // The issue types assigned to the workflow.
      "workflowId": string (required), // The ID of the workflow.
    }
  ], // Mappings from workflows to issue types.
}
```
### Responses

#### 200 - Returned if the request is successful and there is no asynchronous task.

Schema (application/json):
```json
any
```

#### 303 - Returned if the request is successful and there is an asynchronous task for the migrations.

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

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 409 - Returned if another workflow configuration update task is ongoing.

