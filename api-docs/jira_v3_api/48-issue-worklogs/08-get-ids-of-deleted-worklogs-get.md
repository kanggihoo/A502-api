# 08-Get IDs of deleted worklogs [GET]

`GET /rest/api/3/worklog/deleted`

Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.

This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

This resource does not return worklogs deleted during the minute preceding the request.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `since` | `integer` | `query` | No | The date and time, as a UNIX timestamp in milliseconds, after which deleted worklogs are returned. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"lastPage\":true,\"nextPage\":\"https://your-domain.atlassian.net/api/~ver~/worklog/deleted?since=1438013693136\",\"self\":\"https://your-domain.atlassian.net/api/~ver~/worklog/deleted?since=1438013671562\",\"since\":1438013671562,\"until\":1438013693136,\"values\":[{\"properties\":[],\"updatedTime\":1438013671562,\"worklogId\":103},{\"properties\":[],\"updatedTime\":1438013672165,\"worklogId\":104},{\"properties\":[],\"updatedTime\":1438013693136,\"worklogId\":105}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

