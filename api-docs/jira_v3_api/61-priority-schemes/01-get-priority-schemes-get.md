# 01-Get priority schemes [GET]

`GET /rest/api/3/priorityscheme`

Returns a [paginated](#pagination) list of priority schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `string` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `string` | `query` | No | The maximum number of items to return per page. |
| `priorityId` | `array` | `query` | No | A set of priority IDs to filter by. To include multiple IDs, provide an ampersand-separated list. For example, `priorityId=10000&priorityId=10001`. |
| `schemeId` | `array` | `query` | No | A set of priority scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `schemeId=10000&schemeId=10001`. |
| `schemeName` | `string` | `query` | No | The name of scheme to search for. |
| `onlyDefault` | `boolean` | `query` | No | Whether only the default priority is returned. |
| `orderBy` | `string` | `query` | No | The ordering to return the priority schemes by. |
| `expand` | `string` | `query` | No | A comma separated list of additional information to return. "priorities" will return priorities associated with the priority scheme. "projects" will return projects associated with the priority scheme. `expand=priorities,projects`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":1,\"values\":[{\"description\":\"This is the default scheme used by all new and unassigned projects\",\"id\":\"1\",\"isDefault\":true,\"name\":\"Default Priority Scheme\",\"priorities\":{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":3,\"values\":[{\"description\":\"Serious problem that could block progress.\",\"iconUrl\":\"/images/icons/priorities/high.svg\",\"id\":\"1\",\"isDefault\":false,\"name\":\"High\",\"statusColor\":\"#f15C75\"},{\"description\":\"Has the potential to affect progress.\",\"iconUrl\":\"/images/icons/priorities/medium.svg\",\"id\":\"2\",\"isDefault\":true,\"name\":\"Medium\",\"statusColor\":\"#f79232\"},{\"description\":\"Minor problem or easily worked around.\",\"iconUrl\":\"/images/icons/priorities/low.svg\",\"id\":\"3\",\"isDefault\":false,\"name\":\"Low\",\"statusColor\":\"#707070\"}]},\"projects\":{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":1,\"values\":[{\"avatarUrls\":{\"16x16\":\"secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"secure/projectavatar?size=small&pid=10000\",\"32x32\":\"secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"Project category description\",\"id\":\"10000\",\"name\":\"A project category\"},\"projectTypeKey\":\"ProjectTypeKey{key='software'}\",\"self\":\"project/EX\",\"simplified\":false}]}}]}"
```

#### 400 - Returned if the request isn't valid.

#### 401 - Returned if the authentication credentials are incorrect.

