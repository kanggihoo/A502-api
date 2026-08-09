# 11-Get all statuses for project [GET]

`GET /rest/api/3/project/{projectIdOrKey}/statuses`

Returns the valid statuses for a project. The statuses are grouped by issue type, as each project has a set of valid issue types and each issue type has a set of valid statuses.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"id\":\"3\",\"name\":\"Task\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/3\",\"statuses\":[{\"description\":\"The issue is currently being worked on.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/progress.gif\",\"id\":\"10000\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/10000\"},{\"description\":\"The issue is closed.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/closed.gif\",\"id\":\"5\",\"name\":\"Closed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/5\"}],\"subtask\":false}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the project is not found or the user does not have permission to view it.

