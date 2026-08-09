# 01-Get project versions paginated [GET]

`GET /rest/api/3/project/{projectIdOrKey}/version`

Returns a [paginated](#pagination) list of all versions in a project. See the [Get project versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full list of versions without pagination.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `description` Sorts by version description.<br> *  `name` Sorts by version name.<br> *  `releaseDate` Sorts by release date, starting with the oldest date. Versions with no release date are listed last.<br> *  `sequence` Sorts by the order of appearance in the user interface.<br> *  `startDate` Sorts by start date, starting with the oldest date. Versions with no start date are listed last. |
| `query` | `string` | `query` | No | Filter the results using a literal string. Versions with matching `name` or `description` are returned (case insensitive). |
| `status` | `string` | `query` | No | A list of status values used to filter the results by version status. This parameter accepts a comma-separated list. The status values are `released`, `unreleased`, and `archived`. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `issuesstatus` Returns the number of issues in each status category for each version.<br> *  `operations` Returns actions that can be performed on the specified version.<br> *  `driver` Returns the Atlassian account ID of the version driver.<br> *  `approvers` Returns a list containing the approvers for this version. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":2,\"nextPage\":\"https://your-domain.atlassian.net/rest/api/3/project/PR/version?startAt=2&maxResults=2\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/PR/version?startAt=0&maxResults=2\",\"startAt\":0,\"total\":7,\"values\":[{\"archived\":false,\"description\":\"An excellent version\",\"id\":\"10000\",\"name\":\"New Version 1\",\"overdue\":true,\"projectId\":10000,\"releaseDate\":\"2010-07-06\",\"released\":true,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10000\",\"userReleaseDate\":\"6/Jul/2010\"},{\"archived\":false,\"description\":\"Minor Bugfix version\",\"id\":\"10010\",\"issuesStatusForFixVersion\":{\"done\":100,\"inProgress\":20,\"toDo\":10,\"unmapped\":0},\"name\":\"Next Version\",\"overdue\":false,\"projectId\":10000,\"released\":false,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10010\"}]}"
```

#### 404 - Returned if the project is not found or the user does not have permission to view it.

