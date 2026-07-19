# 01-Get issue type screen schemes [GET]

`GET /rest/api/3/issuetypescreenscheme`

Returns a [paginated](#pagination) list of issue type screen schemes.

Only issue type screen schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No | The list of issue type screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. |
| `queryString` | `string` | `query` | No | String used to perform a case-insensitive partial match with issue type screen scheme name. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `name` Sorts by issue type screen scheme name.<br> *  `id` Sorts by issue type screen scheme ID. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts `projects` that, for each issue type screen schemes, returns information about the projects the issue type screen scheme is assigned to. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":2,\"values\":[{\"id\":\"1\",\"name\":\"Default Issue Type Screen Scheme\",\"description\":\"The default issue type screen scheme\"},{\"id\":\"10000\",\"name\":\"Office issue type screen scheme\",\"description\":\"Managing office projects\",\"projects\":{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":1,\"values\":[{\"avatarUrls\":{\"16x16\":\"secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"secure/projectavatar?size=small&pid=10000\",\"32x32\":\"secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"Project category description\",\"id\":\"10000\",\"name\":\"A project category\"},\"projectTypeKey\":\"ProjectTypeKey{key='software'}\",\"self\":\"project/EX\",\"simplified\":false}]}}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

