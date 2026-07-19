# 13-Get workflow for issue type in workflow scheme [GET]

`GET /rest/api/3/workflowscheme/{id}/issuetype/{issueType}`

Returns the issue type-workflow mapping for an issue type in a workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow scheme. |
| `issueType` | `string` | `path` | Yes | The ID of the issue type. |
| `returnDraftIfExists` | `boolean` | `query` | No | Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueType\":\"10000\",\"workflow\":\"jira\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the workflow scheme or issue type is not found.

