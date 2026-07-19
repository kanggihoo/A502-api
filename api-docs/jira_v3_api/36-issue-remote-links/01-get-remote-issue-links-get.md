# 01-Get remote issue links [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/remotelink`

Returns the remote issue links for an issue. When a remote issue link global ID is provided the record with that global ID is returned, otherwise all remote issue links are returned. Where a global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `globalId` | `string` | `query` | No | The global ID of the remote issue link. |

### Responses

#### 200 - Returned if the request is successful. A single RemoteIssueLink will be returned when specifying `globalId`, otherwise an array of RemoteIssueLink is returned.

Example (application/json):
```json
"[{\"application\":{\"name\":\"My Acme Tracker\",\"type\":\"com.acme.tracker\"},\"globalId\":\"system=http://www.mycompany.com/support&id=1\",\"id\":10000,\"object\":{\"icon\":{\"title\":\"Support Ticket\",\"url16x16\":\"http://www.mycompany.com/support/ticket.png\"},\"status\":{\"icon\":{\"link\":\"http://www.mycompany.com/support?id=1&details=closed\",\"title\":\"Case Closed\",\"url16x16\":\"http://www.mycompany.com/support/resolved.png\"},\"resolved\":true},\"summary\":\"Customer support issue\",\"title\":\"TSTSUP-111\",\"url\":\"http://www.mycompany.com/support?id=1\"},\"relationship\":\"causes\",\"self\":\"https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000\"},{\"application\":{\"name\":\"My Acme Tester\",\"type\":\"com.acme.tester\"},\"globalId\":\"system=http://www.anothercompany.com/tester&id=1234\",\"id\":10001,\"object\":{\"icon\":{\"title\":\"Test Case\",\"url16x16\":\"http://www.anothercompany.com/tester/images/testcase.gif\"},\"status\":{\"icon\":{\"link\":\"http://www.anothercompany.com/tester/person?accountId=5b10a2844c20165700ede21g\",\"title\":\"Tested by Mia Krystof\",\"url16x16\":\"http://www.anothercompany.com/tester/images/person/mia.gif\"},\"resolved\":false},\"summary\":\"Test that the submit button saves the item\",\"title\":\"Test Case #1234\",\"url\":\"http://www.anothercompany.com/tester/testcase/1234\"},\"relationship\":\"is tested by\",\"self\":\"https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10001\"}]"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if issue linking is disabled.

#### 404 - Returned if the issue or remote issue link is not found or the user does not have permission to view the issue.

#### 413 - Returned if the per-issue limit for remote links has been breached.

