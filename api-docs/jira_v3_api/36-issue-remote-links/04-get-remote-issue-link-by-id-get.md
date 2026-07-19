# 04-Get remote issue link by ID [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`

Returns a remote issue link for an issue.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `linkId` | `string` | `path` | Yes | The ID of the remote issue link. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"application\":{\"name\":\"My Acme Tracker\",\"type\":\"com.acme.tracker\"},\"globalId\":\"system=http://www.mycompany.com/support&id=1\",\"id\":10000,\"object\":{\"icon\":{\"title\":\"Support Ticket\",\"url16x16\":\"http://www.mycompany.com/support/ticket.png\"},\"status\":{\"icon\":{\"link\":\"http://www.mycompany.com/support?id=1&details=closed\",\"title\":\"Case Closed\",\"url16x16\":\"http://www.mycompany.com/support/resolved.png\"},\"resolved\":true},\"summary\":\"Customer support issue\",\"title\":\"TSTSUP-111\",\"url\":\"http://www.mycompany.com/support?id=1\"},\"relationship\":\"causes\",\"self\":\"https://your-domain.atlassian.net/rest/api/issue/MKY-1/remotelink/10000\"}"
```

#### 400 - Returned if the link ID is invalid or the remote issue link does not belong to the issue.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if issue linking is disabled.

#### 404 - Returned if the issue or remote issue link is not found or the user does not have permission to view the issue.

