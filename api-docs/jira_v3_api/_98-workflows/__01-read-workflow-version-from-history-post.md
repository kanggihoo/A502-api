# 01-Read workflow version from history [POST]

`POST /rest/api/3/workflow/history`

Returns a workflow and related statuses for a specified workflow id and version number.

**Note:** Stored workflow data expires after 60 days. Additionally, no data from before the 30th of October 2025 is available.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflows
 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows

### Request Body (application/json)

```json
{
  "version": integer,
  "workflowId": string,
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"statuses\":[{\"description\":\"An example status description.\",\"id\":\"10003\",\"name\":\"To Do\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"To Do Category\",\"statusReference\":\"10003\"}],\"workflows\":[{\"created\":\"2025-10-20 02:32:12.410331\",\"description\":\"An example workflow description.\",\"id\":\"c5ef565c-1b1e-427e-bc3b-e677b0dc027c\",\"lastUpdateAuthorAAID\":\"123456789\",\"name\":\"Example Workflow\",\"scope\":{\"type\":\"GLOBAL\"},\"startPointLayout\":{\"x\":20.0,\"y\":40.0},\"statuses\":[{\"deprecated\":false,\"layout\":{\"x\":10.0,\"y\":20.0},\"properties\":{},\"statusReference\":\"10003\"}],\"transitions\":[],\"updated\":\"2025-11-21 03:20:39.15096\",\"version\":{\"id\":\"93a7cb12-c503-442a-9e09-654eb7f4dfe2\",\"versionNumber\":4}}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

