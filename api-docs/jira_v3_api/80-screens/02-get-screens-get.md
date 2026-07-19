# 02-Get screens [GET]

`GET /rest/api/3/screens`

Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No | The list of screen IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. |
| `queryString` | `string` | `query` | No | String used to perform a case-insensitive partial match with screen name. |
| `scope` | `array` | `query` | No | The scope filter string. To filter by multiple scope, provide an ampersand-separated list. For example, `scope=GLOBAL&scope=PROJECT`. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `id` Sorts by screen ID.<br> *  `name` Sorts by screen name. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"self\":\"https://your-domain.atlassian.net/rest/api/3/screens\",\"startAt\":0,\"total\":3,\"values\":[{\"id\":1,\"name\":\"Default Screen\",\"description\":\"Provides for the update all system fields.\"},{\"id\":2,\"name\":\"Workflow Screen\",\"description\":\"This screen is used in the workflow and enables you to assign issues.\"},{\"id\":3,\"name\":\"Resolve Issue Screen\",\"description\":\"Offers the ability to set resolution, change fix versions, and assign an issue.\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

