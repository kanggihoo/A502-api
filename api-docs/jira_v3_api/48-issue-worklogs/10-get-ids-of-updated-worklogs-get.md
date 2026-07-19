# 10-Get IDs of updated worklogs [GET]

`GET /rest/api/3/worklog/updated`

Returns a list of IDs and update timestamps for worklogs updated after a date and time.

This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

This resource does not return worklogs updated during the minute preceding the request.

**[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:

 *  the worklog is set as *Viewable by All Users*.
 *  the user is a member of a project role or group with permission to view the worklog.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `since` | `integer` | `query` | No | The date and time, as a UNIX timestamp in milliseconds, after which updated worklogs are returned. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties` that returns the properties of each worklog. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"lastPage\":true,\"nextPage\":\"https://your-domain.atlassian.net/api/~ver~/worklog/updated?since=1438013693136\",\"self\":\"https://your-domain.atlassian.net/api/~ver~/worklog/updated?since=1438013671562\",\"since\":1438013671562,\"until\":1438013693136,\"values\":[{\"properties\":[],\"updatedTime\":1438013671562,\"worklogId\":103},{\"properties\":[],\"updatedTime\":1438013672165,\"worklogId\":104},{\"properties\":[],\"updatedTime\":1438013693136,\"worklogId\":105}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

