# 02-Create workflow scheme [POST]

`POST /rest/api/3/workflowscheme`

Creates a workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "defaultWorkflow": string, // The name of the default workflow for the workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira. If `defaultWorkflow` is not specified when creating a workflow scheme, it is set to *Jira Workflow (jira)*.
  "description": string, // The description of the workflow scheme.
  "draft": boolean, // Whether the workflow scheme is a draft or not.
  "id": integer, // The ID of the workflow scheme.
  "issueTypeMappings": {}, // The issue type to workflow mappings, where each mapping is an issue type ID and workflow name pair. Note that an issue type can only be mapped to one workflow in a workflow scheme.
  "issueTypes": {}, // The issue types available in Jira.
  "lastModified": string, // The date-time that the draft workflow scheme was last modified. A modification is a change to the issue type-project mappings only. This property does not apply to non-draft workflows.
  "lastModifiedUser": any, // The user that last modified the draft workflow scheme. A modification is a change to the issue type-project mappings only. This property does not apply to non-draft workflows.
  "name": string, // The name of the workflow scheme. The name must be unique. The maximum length is 255 characters. Required when creating a workflow scheme.
  "originalDefaultWorkflow": string, // For draft workflow schemes, this property is the name of the default workflow for the original workflow scheme. The default workflow has *All Unassigned Issue Types* assigned to it in Jira.
  "originalIssueTypeMappings": {}, // For draft workflow schemes, this property is the issue type to workflow mappings for the original workflow scheme, where each mapping is an issue type ID and workflow name pair. Note that an issue type can only be mapped to one workflow in a workflow scheme.
  "self": string,
  "updateDraftIfNeeded": boolean, // Whether to create or update a draft workflow scheme when updating an active workflow scheme. An active workflow scheme is a workflow scheme that is used by at least one project. The following examples show how this property works:   *  Update an active workflow scheme with `updateDraftIfNeeded` set to `true`: If a draft workflow scheme exists, it is updated. Otherwise, a draft workflow scheme is created.  *  Update an active workflow scheme with `updateDraftIfNeeded` set to `false`: An error is returned, as active workflow schemes cannot be updated.  *  Update an inactive workflow scheme with `updateDraftIfNeeded` set to `true`: The workflow scheme is updated, as inactive workflow schemes do not require drafts to update.  Defaults to `false`.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultWorkflow\":\"jira\",\"description\":\"The description of the example workflow scheme.\",\"draft\":false,\"id\":101010,\"issueTypeMappings\":{\"10000\":\"scrum workflow\",\"10001\":\"builds workflow\"},\"name\":\"Example workflow scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010\"}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

