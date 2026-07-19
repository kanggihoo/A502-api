# 03-Bulk delete worklogs [DELETE]

`DELETE /rest/api/3/issue/{issueIdOrKey}/worklog`

Deletes a list of worklogs from an issue. This is an experimental API with limitations:

 *  You can't delete more than 5000 worklogs at once.
 *  No notifications will be sent for deleted worklogs.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog.
 *  If any worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `adjustEstimate` | `string` | `query` | No | Defines how to update the issue's time estimate, the options are:<br><br> *  `leave` Leaves the estimate unchanged.<br> *  `auto` Reduces the estimate by the aggregate value of `timeSpent` across all worklogs being deleted. |
| `overrideEditableFlag` | `boolean` | `query` | No | Whether the work log entries should be removed to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with admin permission can use this flag. |

### Request Body (application/json)

```json
{
  "ids": [
    integer
  ] (required), // A list of worklog IDs.
}
```
### Responses

#### 200 - Returned if the bulk deletion request was partially successful, with a message indicating partial success.

#### 204 - Returned if the request is successful.

#### 400 - Returned if:

 *  `request` is not provided or is invalid
 *  the user does not have permission to delete the worklogs
 *  the number of worklogs being deleted exceeds the limit

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if:

 *  the issue is not found or user does not have permission to view the issue
 *  at least one of the worklogs is not associated with the provided issue
 *  time tracking is disabled

