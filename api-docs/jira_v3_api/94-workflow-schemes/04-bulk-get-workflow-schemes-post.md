# 04-Bulk get workflow schemes [POST]

`POST /rest/api/3/workflowscheme/read`

Returns a list of workflow schemes by providing workflow scheme IDs or project IDs.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflow schemes
 *  *Administer projects* project permissions to access project-scoped workflow schemes

### Request Body (application/json)

```json
{
  "projectIds": [
    string
  ], // The list of project IDs to query.
  "workflowSchemeIds": [
    string
  ], // The list of workflow scheme IDs to query.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"defaultWorkflow\":{\"description\":\"This is the default workflow for Software Development projects.\",\"id\":\"3e59db0f-ed6c-47ce-8d50-80c0c4572677\",\"name\":\"Default Software Development Workflow\",\"version\":{\"id\":\"657812fc-bc72-400f-aae0-df8d88db3d9g\",\"versionNumber\":1}},\"description\":\"This is the workflow scheme for the Software Development project type.\",\"id\":\"3g78dg2a-ns2n-56ab-9812-42h5j1464567\",\"name\":\"Software Developer Workflow Scheme\",\"scope\":{\"project\":{\"id\":\"10047\"},\"type\":\"GLOBAL\"},\"taskId\":\"3f83dg2a-ns2n-56ab-9812-42h5j1461629\",\"version\":{\"id\":\"527213fc-bc72-400f-aae0-df8d88db2c8a\",\"versionNumber\":1},\"workflowsForIssueTypes\":[{\"issueTypeIds\":[\"10013\"],\"workflow\":{\"description\":\"This is the workflow for the Software Development bug issue type.\",\"id\":\"5e79ae0f-ed6c-47ce-8d50-80c0c4572745\",\"name\":\"Software Development Bug Workflow\",\"version\":{\"id\":\"897812dc-bc72-400f-aae0-df8d88fe3d8f\",\"versionNumber\":1}}}]}]"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

