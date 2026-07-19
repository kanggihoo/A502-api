# 01-Get UI modifications [GET]

`GET /rest/api/3/uiModifications`

Gets UI modifications. UI modifications can only be retrieved by Forge apps.

**[Permissions](#permissions) required:** None.

The new `read:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `expand` | `string` | `query` | No | Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `data` Returns UI modification data.<br> *  `contexts` Returns UI modification contexts. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":3,\"values\":[{\"id\":\"d7dbda8a-6239-4b63-8e13-a5ef975c8e61\",\"name\":\"Reveal Story Points\",\"description\":\"Reveals Story Points field when any Sprint is selected.\",\"self\":\"https://api.atlassian.com/ex/jira/{cloudid}/rest/api/2/uiModifications/d7dbda8a-6239-4b63-8e13-a5ef975c8e61\",\"data\":\"{field: 'Story Points', config: {hidden: false}}\",\"contexts\":[{\"id\":\"1533537a-bda3-4ac6-8481-846128cd9ef4\",\"projectId\":\"10000\",\"issueTypeId\":\"10000\",\"viewType\":\"GIC\",\"isAvailable\":true},{\"id\":\"c016fefa-6eb3-40c9-8596-4c4ef273e67c\",\"projectId\":\"10000\",\"issueTypeId\":\"10001\",\"viewType\":\"IssueView\",\"isAvailable\":true},{\"id\":\"1016defa-7ew3-40c5-8696-4c1efg73e67s\",\"projectId\":\"10000\",\"issueTypeId\":\"10002\",\"viewType\":\"IssueTransition\",\"isAvailable\":true}]},{\"id\":\"e4fe8db5-f82f-416b-a3aa-b260b55da577\",\"name\":\"Set Assignee\",\"description\":\"Sets the Assignee field automatically.\",\"self\":\"https://api.atlassian.com/ex/jira/{cloudid}/rest/api/2/uiModifications/e4fe8db5-f82f-416b-a3aa-b260b55da577\",\"contexts\":[{\"id\":\"8b3740f9-8780-4958-8228-69dcfbda11d9\",\"projectId\":\"10000\",\"issueTypeId\":\"10000\",\"viewType\":\"GIC\",\"isAvailable\":true}]},{\"id\":\"d3f4097e-8d8e-451e-9fb6-27c3c8c3bfff\",\"name\":\"Wildcard example\",\"description\":\"This context is applied to all issue types\",\"self\":\"https://api.atlassian.com/ex/jira/{cloudid}/rest/api/2/uiModifications/d3f4097e-8d8e-451e-9fb6-27c3c8c3bfff\",\"contexts\":[{\"id\":\"521f2181-5d5e-46ea-9fc9-871bbf245b8b\",\"projectId\":\"10000\",\"issueTypeId\":null,\"viewType\":\"GIC\",\"isAvailable\":true}]},{\"id\":\"1453f993-79ce-4389-a36d-eb72d5c85dd6\",\"name\":\"JSM Context\",\"description\":\"JSM context doesn't support wildcards.\",\"self\":\"https://api.atlassian.com/ex/jira/{cloudid}/rest/api/2/uiModifications/1453f993-79ce-4389-a36d-eb72d5c85dd6\",\"contexts\":[{\"id\":\"521f2181-8780-4958-9fc9-871bbf245b8b\",\"projectId\":null,\"portalId\":\"5\",\"issueTypeId\":null,\"requestTypeId\":\"100\",\"viewType\":\"JSMRequestCreate\",\"isAvailable\":true}]}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the request is not from a Forge app.

