# 16-Get issue types for workflows in workflow scheme [GET]

`GET /rest/api/3/workflowscheme/{id}/workflow`

Returns the workflow-issue type mappings for a workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow scheme. |
| `workflowName` | `string` | `query` | No | The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow. |
| `returnDraftIfExists` | `boolean` | `query` | No | Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultMapping\":false,\"issueTypes\":[\"10000\",\"10001\"],\"workflow\":\"jira\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if either the workflow scheme or workflow is not found.

