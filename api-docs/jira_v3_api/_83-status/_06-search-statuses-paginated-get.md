# 06-Search statuses paginated [GET]

`GET /rest/api/3/statuses/search`

Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination) list of statuses that match a search on name or project.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `string` | `query` | No | The project the status is part of or null for global statuses. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `searchString` | `string` | `query` | No | Term to match status names against or null to search for all statuses in the search scope. |
| `statusCategory` | `string` | `query` | No | Category of the status to filter by. The supported values are: `TODO`, `IN_PROGRESS`, and `DONE`. |
| `includeGlobalStatuses` | `boolean` | `query` | No | Whether to include global statuses (scope = null, not tied to any project) in the response. Defaults to false. Only relevant for project scoped queries. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":2,\"nextPage\":\"https://your-domain.atlassian.net/rest/api/3/statuses/search?startAt=2&maxResults=2\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuses/search?startAt=0&maxResults=2\",\"startAt\":0,\"total\":5,\"values\":[{\"description\":\"The issue is resolved\",\"id\":\"1000\",\"name\":\"Finished\",\"scope\":{\"project\":{\"id\":\"1\"},\"type\":\"PROJECT\"},\"statusCategory\":\"DONE\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

