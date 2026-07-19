# 20-Send notification for issue [POST]

`POST /rest/api/3/issue/{issueIdOrKey}/notify`

Creates an email notification for an issue and adds it to the mail queue.

**[Permissions](#permissions) required:**

 *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | ID or key of the issue that the notification is sent for. |

### Request Body (application/json)

```json
{
  "htmlBody": string, // The HTML body of the email notification for the issue.
  "restrict": any, // Restricts the notifications to users with the specified permissions.
  "subject": string, // The subject of the email notification for the issue. If this is not specified, then the subject is set to the issue key and summary.
  "textBody": string, // The plain text body of the email notification for the issue.
  "to": any, // The recipients of the email notification for the issue.
}
```
### Responses

#### 204 - Returned if the email is queued for sending.

Schema (application/json):
```json
any
```

#### 400 - Returned if:

 *  the recipient is the same as the calling user.
 *  the recipient is invalid. For example, the recipient is set to the assignee, but the issue is unassigned.
 *  the issueIdOrKey is of an invalid/null issue.
 *  the request is invalid. For example, required fields are missing or have invalid values.

#### 403 - Returned if:

 *  outgoing emails are disabled.
 *  no SMTP server is configured.

#### 404 - Returned if the issue is not found.

