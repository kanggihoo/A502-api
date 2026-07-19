# 08-Get projects by priority scheme [GET]

`GET /rest/api/3/priorityscheme/{schemeId}/projects`

Returns a [paginated](#pagination) list of projects by scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `string` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `string` | `query` | No | The maximum number of items to return per page. |
| `projectId` | `array` | `query` | No | The project IDs to filter by. For example, `projectId=10000&projectId=10001`. |
| `schemeId` | `string` | `path` | Yes | The priority scheme ID. |
| `query` | `string` | `query` | No | The string to query projects on by name. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":1,\"values\":[{\"avatarUrls\":{\"16x16\":\"secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"secure/projectavatar?size=small&pid=10000\",\"32x32\":\"secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"Project category description\",\"id\":\"10000\",\"name\":\"A project category\"},\"projectTypeKey\":\"ProjectTypeKey{key='software'}\",\"self\":\"project/EX\",\"simplified\":false}]}"
```

#### 400 - Returned if the request isn't valid.

#### 401 - Returned if the authentication credentials are incorrect.

