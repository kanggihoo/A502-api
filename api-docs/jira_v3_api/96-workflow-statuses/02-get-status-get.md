# 02-Get status [GET]

`GET /rest/api/3/status/{idOrName}`

Returns a status. The status must be associated with an active workflow to be returned.

If a name is used on more than one status, only the status found first is returned. Therefore, identifying the status by its ID may be preferable.

This operation can be accessed anonymously.

[Permissions](#permissions) required: *Browse projects* [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `idOrName` | `string` | `path` | Yes | The ID or name of the status. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"The issue is currently being worked on.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/progress.gif\",\"id\":\"10000\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/10000\",\"statusCategory\":{\"colorName\":\"yellow\",\"id\":1,\"key\":\"in-flight\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/1\"}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the status is not found.
 *  the status is not associated with a workflow.
 *  the user does not have the required permissions.

