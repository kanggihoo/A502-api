# 04-Get available priorities by priority scheme [GET]

`GET /rest/api/3/priorityscheme/priorities/available`

Returns a [paginated](#pagination) list of priorities available for adding to a priority scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `string` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `string` | `query` | No | The maximum number of items to return per page. |
| `query` | `string` | `query` | No | The string to query priorities on by name. |
| `schemeId` | `string` | `query` | Yes | The priority scheme ID. |
| `exclude` | `array` | `query` | No | A list of priority IDs to exclude from the results. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":3,\"values\":[{\"description\":\"Serious problem that could block progress.\",\"iconUrl\":\"/images/icons/priorities/high.svg\",\"id\":\"1\",\"isDefault\":false,\"name\":\"High\",\"statusColor\":\"#f15C75\"},{\"description\":\"Has the potential to affect progress.\",\"iconUrl\":\"/images/icons/priorities/medium.svg\",\"id\":\"2\",\"isDefault\":true,\"name\":\"Medium\",\"statusColor\":\"#f79232\"},{\"description\":\"Minor problem or easily worked around.\",\"iconUrl\":\"/images/icons/priorities/low.svg\",\"id\":\"3\",\"isDefault\":false,\"name\":\"Low\",\"statusColor\":\"#707070\"}]}"
```

#### 400 - Returned if the request isn't valid.

#### 401 - Returned if the authentication credentials are incorrect.

