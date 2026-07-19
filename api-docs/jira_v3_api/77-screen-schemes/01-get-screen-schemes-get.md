# 01-Get screen schemes [GET]

`GET /rest/api/3/screenscheme`

Returns a [paginated](#pagination) list of screen schemes.

Only screen schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No | The list of screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) include additional information in the response. This parameter accepts `issueTypeScreenSchemes` that, for each screen schemes, returns information about the issue type screen scheme the screen scheme is assigned to. |
| `queryString` | `string` | `query` | No | String used to perform a case-insensitive partial match with screen scheme name. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `id` Sorts by screen scheme ID.<br> *  `name` Sorts by screen scheme name. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"self\":\"https://your-domain.atlassian.net/rest/api/3/screenscheme?maxResults=25&startAt=0\",\"startAt\":0,\"total\":2,\"values\":[{\"id\":10010,\"name\":\"Employee screen scheme\",\"description\":\"Manage employee data\",\"screens\":{\"default\":10017,\"edit\":10019,\"create\":10019,\"view\":10020},\"issueTypeScreenSchemes\":{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":1,\"values\":[{\"id\":\"10000\",\"name\":\"Office issue type screen scheme\",\"description\":\"Managing office projects\"}]}},{\"id\":10032,\"name\":\"Office screen scheme\",\"description\":\"Manage office data\",\"screens\":{\"default\":10020}}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

