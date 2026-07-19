# 02-Get project versions [GET]

`GET /rest/api/3/project/{projectIdOrKey}/versions`

Returns all versions in a project. The response is not paginated. Use [Get project versions paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a project with pagination.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts `operations`, which returns actions that can be performed on the version. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"archived\":false,\"description\":\"An excellent version\",\"id\":\"10000\",\"name\":\"New Version 1\",\"overdue\":true,\"projectId\":10000,\"releaseDate\":1278385482288,\"releaseDateSet\":true,\"released\":true,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10000\",\"startDateSet\":false,\"userReleaseDate\":\"6/Jul/2010\"},{\"archived\":false,\"description\":\"Minor Bugfix version\",\"id\":\"10010\",\"issuesStatusForFixVersion\":{\"done\":100,\"inProgress\":20,\"toDo\":10,\"unmapped\":0},\"name\":\"Next Version\",\"overdue\":false,\"projectId\":10000,\"releaseDateSet\":false,\"released\":false,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10010\",\"startDateSet\":false}]"
```

#### 404 - Returned if the project is not found or the user does not have permission to view it.

