# 01-Get all statuses [GET]

`GET /rest/api/3/status`

Returns a list of all statuses associated with active workflows.

This operation can be accessed anonymously.

[Permissions](#permissions) required: *Browse projects* [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) for the project.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"description\":\"The issue is currently being worked on.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/progress.gif\",\"id\":\"10000\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/10000\",\"statusCategory\":{\"colorName\":\"yellow\",\"id\":1,\"key\":\"in-flight\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/1\"}},{\"description\":\"The issue is closed.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/closed.gif\",\"id\":\"5\",\"name\":\"Closed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/5\",\"statusCategory\":{\"colorName\":\"green\",\"id\":9,\"key\":\"completed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/9\"}}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

