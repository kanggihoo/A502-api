# 09-Get worklogs [POST]

`POST /rest/api/3/worklog/list`

Returns worklog details for a list of worklog IDs.

The returned list of worklogs is limited to 1000 items.

**[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:

 *  the worklog is set as *Viewable by All Users*.
 *  the user is a member of a project role or group with permission to view the worklog.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties` that returns the properties of each worklog. |

### Request Body (application/json)

```json
{
  "ids": [
    integer
  ] (required), // A list of worklog IDs.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"comment\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"I did some work here.\"}]}]},\"id\":\"100028\",\"issueId\":\"10002\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000\",\"started\":\"2021-01-17T12:34:00.000+0000\",\"timeSpent\":\"3h 20m\",\"timeSpentSeconds\":12000,\"updateAuthor\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"updated\":\"2021-01-18T23:45:00.000+0000\",\"visibility\":{\"identifier\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"type\":\"group\",\"value\":\"jira-developers\"}}]"
```

#### 400 - Returned if the request contains more than 1000 worklog IDs or is empty.

#### 401 - Returned if the authentication credentials are incorrect or missing.

