# 06-Get required status mappings for workflow scheme update [POST]

`POST /rest/api/3/workflowscheme/update/mappings`

Gets the required status mappings for the desired changes to a workflow scheme. The results are provided per issue type and workflow. When updating a workflow scheme, status mappings can be provided per issue type, per workflow, or both.

**[Permissions](#permissions) required:**

 *  *Administer Jira* permission to update all, including global-scoped, workflow schemes.
 *  *Administer projects* project permission to update project-scoped workflow schemes.

### Request Body (application/json)

```json
{
  "defaultWorkflowId": string, // The ID of the new default workflow for this workflow scheme. Only used in global-scoped workflow schemes. If it isn't specified, is set to *Jira Workflow (jira)*.
  "id": string (required), // The ID of the workflow scheme.
  "workflowsForIssueTypes": [
    {
      "issueTypeIds": [
        string
      ] (required), // The issue types assigned to the workflow.
      "workflowId": string (required), // The ID of the workflow.
    }
  ] (required), // The new workflow to issue type mappings for this workflow scheme.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"statusMappingsByIssueTypes\":[{\"issueTypeId\":\"10000\",\"statusIds\":[\"10000\",\"10001\"]}],\"statusMappingsByWorkflows\":[{\"sourceWorkflowId\":\"10000\",\"statusIds\":[\"10000\",\"10001\"],\"targetWorkflowId\":\"10001\"}],\"statuses\":[{\"category\":\"TODO\",\"id\":\"10000\",\"name\":\"To Do\"}],\"statusesPerWorkflow\":[{\"initialStatusId\":\"10000\",\"statuses\":[\"10000\",\"10001\"],\"workflowId\":\"10000\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

