# 03-Get workflows paginated [GET]

`GET /rest/api/3/workflow/search`

This will be removed on [June 1, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-2569); use [Search workflows](#api-rest-api-3-workflows-search-get) instead.

Returns a [paginated](#pagination) list of published classic workflows. When workflow names are specified, details of those workflows are returned. Otherwise, all published classic workflows are returned.

This operation does not return next-gen workflows.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `workflowName` | `array` | `query` | No | The name of a workflow to return. To include multiple workflows, provide an ampersand-separated list. For example, `workflowName=name1&workflowName=name2`. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `transitions` For each workflow, returns information about the transitions inside the workflow.<br> *  `transitions.rules` For each workflow transition, returns information about its rules. Transitions are included automatically if this expand is requested.<br> *  `transitions.properties` For each workflow transition, returns information about its properties. Transitions are included automatically if this expand is requested.<br> *  `statuses` For each workflow, returns information about the statuses inside the workflow.<br> *  `statuses.properties` For each workflow status, returns information about its properties. Statuses are included automatically if this expand is requested.<br> *  `default` For each workflow, returns information about whether this is the default workflow.<br> *  `schemes` For each workflow, returns information about the workflow schemes the workflow is assigned to.<br> *  `projects` For each workflow, returns information about the projects the workflow is assigned to, through workflow schemes.<br> *  `hasDraftWorkflow` For each workflow, returns information about whether the workflow has a draft version.<br> *  `operations` For each workflow, returns information about the actions that can be undertaken on the workflow. |
| `queryString` | `string` | `query` | No | String used to perform a case-insensitive partial match with workflow name. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `name` Sorts by workflow name.<br> *  `created` Sorts by create time.<br> *  `updated` Sorts by update time. |
| `isActive` | `boolean` | `query` | No | Filters active and inactive workflows. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":1,\"startAt\":0,\"total\":5,\"values\":[{\"id\":{\"name\":\"SCRUM Workflow\",\"entityId\":\"5ed312c5-f7a6-4a78-a1f6-8ff7f307d063\"},\"description\":\"A workflow used for Software projects in the SCRUM methodology\",\"transitions\":[{\"id\":\"5\",\"name\":\"In Progress\",\"description\":\"Start working on the issue.\",\"from\":[\"10\",\"13\"],\"to\":\"14\",\"type\":\"directed\",\"screen\":{\"id\":\"10000\",\"name\":\"Issue screen\"},\"rules\":{\"conditionsTree\":{\"nodeType\":\"compound\",\"operator\":\"AND\",\"conditions\":[{\"nodeType\":\"simple\",\"type\":\"PermissionCondition\",\"configuration\":{\"permissionKey\":\"WORK_ON_ISSUES\"}},{\"nodeType\":\"simple\",\"type\":\"PermissionCondition\",\"configuration\":{\"permissionKey\":\"RESOLVE_ISSUES\"}}]},\"validators\":[{\"type\":\"FieldRequiredValidator\",\"configuration\":{\"errorMessage\":\"A custom error message\",\"fields\":[\"description\",\"assignee\"],\"ignoreContext\":true}}],\"postFunctions\":[{\"type\":\"UpdateIssueStatusFunction\"},{\"type\":\"GenerateChangeHistoryFunction\"},{\"type\":\"FireIssueEventFunction\"}]},\"properties\":{\"jira.fieldscreen.id\":1}}],\"statuses\":[{\"id\":\"3\",\"name\":\"In Progress\",\"properties\":{\"issueEditable\":false,\"jira.issue.editable\":\"false\"}}],\"isDefault\":false,\"schemes\":[{\"id\":\"10001\",\"name\":\"Test Workflow Scheme\"}],\"projects\":[{\"avatarUrls\":{\"16x16\":\"secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"secure/projectavatar?size=small&pid=10000\",\"32x32\":\"secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"Project category description\",\"id\":\"10000\",\"name\":\"A project category\"},\"projectTypeKey\":\"ProjectTypeKey{key='software'}\",\"self\":\"project/EX\",\"simplified\":false}],\"hasDraftWorkflow\":true,\"operations\":{\"canEdit\":true,\"canDelete\":false},\"created\":\"2018-12-10T16:30:15.000+0000\",\"updated\":\"2018-12-11T11:45:13.000+0000\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access workflows.\"],\"errors\":{}}"
```

