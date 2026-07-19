# 04-Get issue type schemes for projects [GET]

`GET /rest/api/3/issuetypescheme/project`

Returns a [paginated](#pagination) list of issue type schemes and, for each issue type scheme, a list of the projects that use it.

Only issue type schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `projectId` | `array` | `query` | Yes | The list of project IDs. To include multiple project IDs, provide an ampersand-separated list. For example, `projectId=10000&projectId=10001`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":3,\"values\":[{\"issueTypeScheme\":{\"id\":\"10000\",\"name\":\"Default Issue Type Scheme\",\"description\":\"Default issue type scheme is the list of global issue types. All newly created issue types will automatically be added to this scheme.\",\"defaultIssueTypeId\":\"10003\",\"isDefault\":true},\"projectIds\":[\"10000\",\"10001\"]},{\"issueTypeScheme\":{\"id\":\"10001\",\"name\":\"SUP: Kanban Issue Type Scheme\",\"description\":\"A collection of issue types suited to use in a kanban style project.\"},\"projectIds\":[\"10002\"]},{\"issueTypeScheme\":{\"id\":\"10002\",\"name\":\"HR: Scrum issue type scheme\",\"description\":\"\",\"defaultIssueTypeId\":\"10004\",\"issueTypes\":{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":1,\"values\":[{\"description\":\"Improvement Issue Type\",\"hierarchyLevel\":-1,\"iconUrl\":\"www.example.com\",\"id\":\"1000L\",\"name\":\"Improvements\",\"subtask\":true}]}},\"projectIds\":[\"10003\",\"10004\",\"10005\"]}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

