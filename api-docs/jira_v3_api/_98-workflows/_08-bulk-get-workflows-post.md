# 08-Bulk get workflows [POST]

`POST /rest/api/3/workflows`

Returns a list of workflows and related statuses by providing workflow names, workflow IDs, or project and issue types.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflows
 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows

### Request Body (application/json)

```json
{
  "projectAndIssueTypes": [
    {
      "issueTypeId": string (required), // The ID of the issue type.
      "projectId": string (required), // The ID of the project.
    }
  ], // The list of projects and issue types to query.
  "workflowIds": [
    string
  ], // The list of workflow IDs to query.
  "workflowNames": [
    string
  ], // The list of workflow names to query.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"statuses\":[{\"description\":\"\",\"id\":\"10003\",\"name\":\"Done\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"DONE\",\"statusReference\":\"10003\"},{\"description\":\"\",\"id\":\"10001\",\"name\":\"To Do\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"TODO\",\"statusReference\":\"10001\"},{\"description\":\"\",\"id\":\"10002\",\"name\":\"In Progress\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"IN_PROGRESS\",\"statusReference\":\"10002\"}],\"workflows\":[{\"description\":\"\",\"id\":\"b9ff2384-d3b6-4d4e-9509-3ee19f607168\",\"isEditable\":true,\"name\":\"Workflow 1\",\"scope\":{\"type\":\"GLOBAL\"},\"startPointLayout\":{\"x\":-100.00030899047852,\"y\":-153.00020599365234},\"statuses\":[{\"deprecated\":false,\"layout\":{\"x\":317.0000915527344,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10002\"},{\"deprecated\":false,\"layout\":{\"x\":508.000244140625,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10003\"},{\"deprecated\":false,\"layout\":{\"x\":114.99993896484375,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10001\"}],\"transitions\":[{\"actions\":[],\"description\":\"\",\"id\":\"11\",\"links\":[],\"name\":\"To Do\",\"properties\":{},\"toStatusReference\":\"10001\",\"triggers\":[],\"type\":\"GLOBAL\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"21\",\"links\":[],\"name\":\"In Progress\",\"properties\":{},\"toStatusReference\":\"10002\",\"triggers\":[],\"type\":\"GLOBAL\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"41\",\"links\":[{\"fromPort\":0,\"fromStatusReference\":\"10001\",\"toPort\":1}],\"name\":\"Start work\",\"properties\":{},\"toStatusReference\":\"10002\",\"triggers\":[],\"type\":\"DIRECTED\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"1\",\"links\":[],\"name\":\"Create\",\"properties\":{},\"toStatusReference\":\"10001\",\"triggers\":[],\"type\":\"INITIAL\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"31\",\"links\":[],\"name\":\"Done\",\"properties\":{},\"toStatusReference\":\"10003\",\"triggers\":[],\"type\":\"GLOBAL\",\"validators\":[]}],\"version\":{\"id\":\"f010ac1b-3dd3-43a3-aa66-0ee8a447f76e\",\"versionNumber\":0}}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

