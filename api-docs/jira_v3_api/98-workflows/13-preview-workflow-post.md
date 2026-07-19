# 13-Preview workflow [POST]

`POST /rest/api/3/workflows/preview`

Returns a requested workflow within a given project. The response provides a read-only preview of the workflow, omitting full configuration details.

**[Permissions](#permissions) required:**

 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions

### Request Body (application/json)

```json
{
  "issueTypeIds": [
    string
  ], // The list of issue type IDs. At most 25 issue type IDs can be specified.
  "projectId": string (required), // The projectId parameter is required and will be used for permission checks. In addition, you must supply at least one of the following lookup terms: *workflowNames*, *workflowIds*, or *issueTypeIds*. The specified workflows must be associated with the given project.
  "workflowIds": [
    string
  ], // The list of workflow IDs to be returned. At most 25 workflow IDs can be specified.
  "workflowNames": [
    string
  ], // The list of workflow names to be returned. At most 25 workflow names can be specified.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"statuses\":[{\"description\":\"The initial status for tasks\",\"id\":\"1\",\"name\":\"Zrobic\",\"rawName\":\"To Do\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"TODO\",\"statusReference\":\"1\"},{\"description\":\"Work is actively being done on this task\",\"id\":\"2\",\"name\":\"W toku\",\"rawName\":\"In Progress\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"IN_PROGRESS\",\"statusReference\":\"2\"},{\"description\":\"The task has been completed\",\"id\":\"3\",\"name\":\"Zrobione\",\"rawName\":\"Done\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"DONE\",\"statusReference\":\"3\"}],\"workflows\":[{\"description\":\"A sample workflow for demonstration purposes\",\"id\":\"b9ff2384-d3b6-4d4e-9509-3ee19f607168\",\"name\":\"Sample Workflow\",\"queryContext\":[{\"issueTypes\":[\"10001\",\"10002\"],\"project\":\"10000\"}],\"scope\":{\"type\":\"GLOBAL\"},\"startPointLayout\":{\"x\":30.0,\"y\":40.0},\"statuses\":[{\"deprecated\":false,\"layout\":{\"x\":100.0,\"y\":200.0},\"statusReference\":\"1\"},{\"deprecated\":false,\"layout\":{\"x\":300.0,\"y\":200.0},\"statusReference\":\"2\"},{\"deprecated\":false,\"layout\":{\"x\":500.0,\"y\":200.0},\"statusReference\":\"3\"}],\"transitions\":[{\"actions\":[],\"description\":\"Creates the issue\",\"id\":\"1\",\"links\":[],\"name\":\"Create\",\"toStatusReference\":\"1\",\"triggers\":[],\"type\":\"INITIAL\",\"validators\":[]},{\"actions\":[],\"description\":\"Begin work on the issue\",\"id\":\"21\",\"links\":[{\"fromPort\":0,\"fromStatusReference\":\"1\",\"toPort\":0}],\"name\":\"Start Progress\",\"toStatusReference\":\"2\",\"triggers\":[],\"type\":\"DIRECTED\",\"validators\":[]},{\"actions\":[],\"description\":\"Complete the issue\",\"id\":\"31\",\"links\":[{\"fromPort\":0,\"fromStatusReference\":\"2\",\"toPort\":0}],\"name\":\"Done\",\"toStatusReference\":\"3\",\"triggers\":[],\"type\":\"DIRECTED\",\"validators\":[]}],\"version\":{\"id\":\"f010ac1b-3dd3-43a3-aa66-0ee8a447f76e\",\"versionNumber\":1}}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

#### 404 - Returned if one or more previews are not found.

