# 08-Get workflow for issue type in draft workflow scheme [GET]

`GET /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}`

Returns the issue type-workflow mapping for an issue type in a workflow scheme's draft.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow scheme that the draft belongs to. |
| `issueType` | `string` | `path` | Yes | The ID of the issue type. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueType\":\"10000\",\"workflow\":\"jira\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the workflow scheme or issue type is not found.

