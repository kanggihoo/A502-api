# 01-Get all issue type schemes [GET]

`GET /rest/api/3/issuetypescheme`

Returns a [paginated](#pagination) list of issue type schemes.

Only issue type schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No | The list of issue type schemes IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `name` Sorts by issue type scheme name.<br> *  `id` Sorts by issue type scheme ID. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `projects` For each issue type schemes, returns information about the projects the issue type scheme is assigned to.<br> *  `issueTypes` For each issue type schemes, returns information about the issueTypes the issue type scheme have. |
| `queryString` | `string` | `query` | No | String used to perform a case-insensitive partial match with issue type scheme name. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":3,\"values\":[{\"id\":\"10000\",\"name\":\"Default Issue Type Scheme\",\"description\":\"Default issue type scheme is the list of global issue types. All newly created issue types will automatically be added to this scheme.\",\"defaultIssueTypeId\":\"10003\",\"isDefault\":true},{\"id\":\"10001\",\"name\":\"SUP: Kanban Issue Type Scheme\",\"description\":\"A collection of issue types suited to use in a kanban style project.\",\"projects\":{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":1,\"values\":[{\"avatarUrls\":{\"16x16\":\"secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"secure/projectavatar?size=small&pid=10000\",\"32x32\":\"secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"Project category description\",\"id\":\"10000\",\"name\":\"A project category\"},\"projectTypeKey\":\"ProjectTypeKey{key='software'}\",\"self\":\"project/EX\",\"simplified\":false}]}},{\"id\":\"10002\",\"name\":\"HR: Scrum issue type scheme\",\"description\":\"\",\"defaultIssueTypeId\":\"10004\",\"issueTypes\":{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":1,\"values\":[{\"description\":\"Improvement Issue Type\",\"hierarchyLevel\":-1,\"iconUrl\":\"www.example.com\",\"id\":\"1000L\",\"name\":\"Improvements\",\"subtask\":true}]}}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

