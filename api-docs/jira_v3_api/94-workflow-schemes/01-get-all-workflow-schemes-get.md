# 01-Get all workflow schemes [GET]

`GET /rest/api/3/workflowscheme`

Returns a [paginated](#pagination) list of all workflow schemes, not including draft workflow schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":2,\"values\":[{\"defaultWorkflow\":\"jira\",\"description\":\"The description of the example workflow scheme.\",\"id\":101010,\"issueTypeMappings\":{\"10000\":\"scrum workflow\",\"10001\":\"builds workflow\"},\"name\":\"Example workflow scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010\"},{\"defaultWorkflow\":\"jira\",\"description\":\"The description of the another example workflow scheme.\",\"id\":101011,\"issueTypeMappings\":{\"10000\":\"scrum workflow\",\"10001\":\"builds workflow\"},\"name\":\"Another example workflow scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/workflowscheme/101011\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

