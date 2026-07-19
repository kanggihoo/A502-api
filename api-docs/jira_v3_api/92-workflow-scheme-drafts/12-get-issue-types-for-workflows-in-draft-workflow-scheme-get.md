# 12-Get issue types for workflows in draft workflow scheme [GET]

`GET /rest/api/3/workflowscheme/{id}/draft/workflow`

Returns the workflow-issue type mappings for a workflow scheme's draft.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow scheme that the draft belongs to. |
| `workflowName` | `string` | `query` | No | The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultMapping\":false,\"issueTypes\":[\"10000\",\"10001\"],\"workflow\":\"jira\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if either the workflow scheme or workflow (if specified) is not found. session.

