# 14-Search workflows [GET]

`GET /rest/api/3/workflows/search`

Returns a [paginated](#pagination) list of global and project workflows. If workflow names are specified in the query string, details of those workflows are returned. Otherwise, all workflows are returned.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflows
 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `values.transitions` Returns the transitions that each workflow is associated with. |
| `queryString` | `string` | `query` | No | String used to perform a case-insensitive partial match with workflow name. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `name` Sorts by workflow name.<br> *  `created` Sorts by create time.<br> *  `updated` Sorts by update time. |
| `scope` | `string` | `query` | No | The scope of the workflow. Global for company-managed projects and Project for team-managed projects. |
| `isActive` | `boolean` | `query` | No | Filters active and inactive workflows. |
| `projectId` | `integer` | `query` | No | The ID of the project to filter the workflows by. Only workflows associated with the given project are returned. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":50,\"nextPage\":\"https://your-domain.atlassian.net/rest/api/3/workflows/search?startAt=50\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/workflows/search\",\"startAt\":0,\"statuses\":[{\"description\":\"\",\"id\":\"10003\",\"name\":\"Done\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"DONE\",\"statusReference\":\"10003\"},{\"description\":\"\",\"id\":\"10001\",\"name\":\"To Do\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"TODO\",\"statusReference\":\"10001\"},{\"description\":\"\",\"id\":\"10002\",\"name\":\"In Progress\",\"scope\":{\"type\":\"GLOBAL\"},\"statusCategory\":\"IN_PROGRESS\",\"statusReference\":\"10002\"}],\"total\":100,\"values\":[{\"description\":\"\",\"id\":\"b9ff2384-d3b6-4d4e-9509-3ee19f607168\",\"isEditable\":true,\"name\":\"Workflow 1\",\"scope\":{\"type\":\"GLOBAL\"},\"startPointLayout\":{\"x\":-100.00030899047852,\"y\":-153.00020599365234},\"statuses\":[{\"deprecated\":false,\"layout\":{\"x\":317.0000915527344,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10002\"},{\"deprecated\":false,\"layout\":{\"x\":508.000244140625,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10003\"},{\"deprecated\":false,\"layout\":{\"x\":114.99993896484375,\"y\":-16.0},\"properties\":{},\"statusReference\":\"10001\"}],\"transitions\":[{\"actions\":[],\"description\":\"\",\"id\":\"11\",\"links\":[],\"name\":\"To Do\",\"properties\":{},\"toStatusReference\":\"10001\",\"triggers\":[],\"type\":\"GLOBAL\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"21\",\"links\":[],\"name\":\"In Progress\",\"properties\":{},\"toStatusReference\":\"10002\",\"triggers\":[],\"type\":\"GLOBAL\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"41\",\"links\":[{\"fromPort\":0,\"fromStatusReference\":\"10001\",\"toPort\":1}],\"name\":\"Start work\",\"properties\":{},\"toStatusReference\":\"10002\",\"triggers\":[],\"type\":\"DIRECTED\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"1\",\"links\":[],\"name\":\"Create\",\"properties\":{},\"toStatusReference\":\"10001\",\"triggers\":[],\"type\":\"INITIAL\",\"validators\":[]},{\"actions\":[],\"description\":\"\",\"id\":\"31\",\"links\":[],\"name\":\"Done\",\"properties\":{},\"toStatusReference\":\"10003\",\"triggers\":[],\"type\":\"GLOBAL\",\"validators\":[]}],\"version\":{\"id\":\"f010ac1b-3dd3-43a3-aa66-0ee8a447f76e\",\"versionNumber\":0}}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

