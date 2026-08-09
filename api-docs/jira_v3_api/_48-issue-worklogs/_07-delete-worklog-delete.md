# 07-Delete worklog [DELETE]

`DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`

Deletes a worklog from an issue.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog or *Delete own worklogs* to delete worklogs created by the user,
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `id` | `string` | `path` | Yes | The ID of the worklog. |
| `notifyUsers` | `boolean` | `query` | No | Whether users watching the issue are notified by email. |
| `adjustEstimate` | `string` | `query` | No | Defines how to update the issue's time estimate, the options are:<br><br> *  `new` Sets the estimate to a specific value, defined in `newEstimate`.<br> *  `leave` Leaves the estimate unchanged.<br> *  `manual` Increases the estimate by amount specified in `increaseBy`.<br> *  `auto` Reduces the estimate by the value of `timeSpent` in the worklog. |
| `newEstimate` | `string` | `query` | No | The value to set as the issue's remaining time estimate, as days (\#d), hours (\#h), or minutes (\#m or \#). For example, *2d*. Required when `adjustEstimate` is `new`. |
| `increaseBy` | `string` | `query` | No | The amount to increase the issue's remaining estimate by, as days (\#d), hours (\#h), or minutes (\#m or \#). For example, *2d*. Required when `adjustEstimate` is `manual`. |
| `overrideEditableFlag` | `boolean` | `query` | No | Whether the work log entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with admin permission can use this flag. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if:

 *  `adjustEstimate` is set to `new` but `newEstimate` is not provided or is invalid.
 *  `adjustEstimate` is set to `manual` but `reduceBy` is not provided or is invalid.
 *  the user does not have permission to delete the worklog.

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if:

 *  the issue is not found or user does not have permission to view the issue.
 *  the worklog is not found or the user does not have permission to view it.
 *  time tracking is disabled.

