# 01-Get precomputations (apps) [GET]

`GET /rest/api/3/jql/function/computation`

Returns the list of a function's precomputations along with information about when they were created, updated, and last used. Each precomputation has a `value` \- the JQL fragment to replace the custom function clause with.

**[Permissions](#permissions) required:** This API is only accessible to apps and apps can only inspect their own functions.

The new `read:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `functionKey` | `array` | `query` | No | The function key in format:<br><br> *  Forge: `ari:cloud:ecosystem::extension/[App ID]/[Environment ID]/static/[Function key from manifest]`<br> *  Connect: `[App key]__[Module key]` |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `functionKey` Sorts by the functionKey.<br> *  `used` Sorts by the used timestamp.<br> *  `created` Sorts by the created timestamp.<br> *  `updated` Sorts by the updated timestamp. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":1,\"values\":[{\"arguments\":[\"Test\"],\"created\":\"2023-10-14T05:25:20.000+0000\",\"field\":\"issue\",\"functionKey\":\"ari:cloud:ecosystem::extension/00000000-1111-2222-3333-4444444/111111-2222-3333-4444-55555/static/issuesWithText\",\"functionName\":\"issuesWithText\",\"id\":\"cf75a1b0-4ac6-4bd8-8a50-29a465a96520\",\"operator\":\"in\",\"updated\":\"2023-10-14T05:25:20.000+0000\",\"used\":\"2023-10-14T05:25:20.000+0000\",\"value\":\"issue in (TEST-1, TEST-2, TEST-3)\"},{\"arguments\":[\"10001\"],\"created\":\"2023-10-14T05:25:20.000+0000\",\"error\":\"Error message to be displayed to the user\",\"field\":\"issue\",\"functionKey\":\"ari:cloud:ecosystem::extension/00000000-1111-2222-3333-4444444/111111-2222-3333-4444-55555/static/issuesWithText\",\"functionName\":\"issuesWithText\",\"id\":\"2a854f11-d0e1-4260-aea8-64a562a7062a\",\"operator\":\"=\",\"updated\":\"2023-10-14T05:25:20.000+0000\",\"used\":\"2023-10-14T05:25:20.000+0000\"}]}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the request is not authenticated as the app that provided the function.

#### 404 - Returned if the function is not found.

