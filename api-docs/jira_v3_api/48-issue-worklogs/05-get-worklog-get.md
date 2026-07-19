# 05-Get worklog [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`

Returns a worklog.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `id` | `string` | `path` | Yes | The ID of the worklog. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about work logs in the response. This parameter accepts<br><br>`properties`, which returns worklog properties. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"comment\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"I did some work here.\"}]}]},\"id\":\"100028\",\"issueId\":\"10002\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000\",\"started\":\"2021-01-17T12:34:00.000+0000\",\"timeSpent\":\"3h 20m\",\"timeSpentSeconds\":12000,\"updateAuthor\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"updated\":\"2021-01-18T23:45:00.000+0000\",\"visibility\":{\"identifier\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"type\":\"group\",\"value\":\"jira-developers\"}}"
```

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if:

 *  the issue is not found or the user does not have permission to view it.
 *  the worklog is not found or the user does not have permission to view it.
 *  time tracking is disabled.

.

