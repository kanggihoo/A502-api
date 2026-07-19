# 01-Get bulk screen tabs [GET]

`GET /rest/api/3/screens/tabs`

Returns the list of tabs for a bulk of screens.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `array` | `query` | No | The list of screen IDs. To include multiple screen IDs, provide an ampersand-separated list. For example, `screenId=10000&screenId=10001`. |
| `tabId` | `array` | `query` | No | The list of tab IDs. To include multiple tab IDs, provide an ampersand-separated list. For example, `tabId=10000&tabId=10001`. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResult` | `integer` | `query` | No | The maximum number of items to return per page. The maximum number is 100, |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":2,\"values\":[{\"screenId\":10000,\"tabId\":10001,\"tabName\":\"My Custom Tab 1\"},{\"screenId\":10001,\"tabId\":10002,\"tabName\":\"My Custom Tab 2\"}]}"
```

#### 400 - Returned if the screen ID or the tab ID is empty.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

