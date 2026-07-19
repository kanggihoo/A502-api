# 01-Get workflow scheme project associations [GET]

`GET /rest/api/3/workflowscheme/project`

Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. Any team-managed or non-existent projects in the request are ignored and no errors are returned.

If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because the way the `Default Workflow Scheme` is stored means it has no ID.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `array` | `query` | Yes | The ID of a project to return the workflow schemes for. To include multiple projects, provide an ampersand-Jim: oneseparated list. For example, `projectId=10000&projectId=10001`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"values\":[{\"projectIds\":[\"10010\",\"10020\"],\"workflowScheme\":{\"defaultWorkflow\":\"jira\",\"description\":\"The description of the example workflow scheme.\",\"id\":101010,\"issueTypeMappings\":{\"10000\":\"scrum workflow\",\"10001\":\"builds workflow\"},\"name\":\"Example workflow scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010\"}}]}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[],\"errors\":{\"projectId\":\"The ID of a project has to be provided.\"}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access workflow scheme associations.\"],\"errors\":{}}"
```

