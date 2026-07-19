# 02-Add worklog [POST]

`POST /rest/api/3/issue/{issueIdOrKey}/worklog`

Adds a worklog to an issue.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Work on issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key the issue. |
| `notifyUsers` | `boolean` | `query` | No | Whether users watching the issue are notified by email. |
| `adjustEstimate` | `string` | `query` | No | Defines how to update the issue's time estimate, the options are:<br><br> *  `new` Sets the estimate to a specific value, defined in `newEstimate`.<br> *  `leave` Leaves the estimate unchanged.<br> *  `manual` Reduces the estimate by amount specified in `reduceBy`.<br> *  `auto` Reduces the estimate by the value of `timeSpent` in the worklog. |
| `newEstimate` | `string` | `query` | No | The value to set as the issue's remaining time estimate, as days (\#d), hours (\#h), or minutes (\#m or \#). For example, *2d*. Required when `adjustEstimate` is `new`. |
| `reduceBy` | `string` | `query` | No | The amount to reduce the issue's remaining estimate by, as days (\#d), hours (\#h), or minutes (\#m). For example, *2d*. Required when `adjustEstimate` is `manual`. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about work logs in the response. This parameter accepts `properties`, which returns worklog properties. |
| `overrideEditableFlag` | `boolean` | `query` | No | Whether the worklog entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can use this flag. |

### Request Body (application/json)

```json
{
  "author": any, // Details of the user who created the worklog.
  "comment": any, // A comment about the worklog in [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/). Optional when creating or updating a worklog.
  "created": string, // The datetime on which the worklog was created.
  "id": string, // The ID of the worklog record.
  "issueId": string, // The ID of the issue this worklog is for.
  "properties": [
    {
      "key": string, // The key of the property. Required on create and update.
      "value": any, // The value of the property. Required on create and update.
    }
  ], // Details of properties for the worklog. Optional when creating or updating a worklog.
  "self": string, // The URL of the worklog item.
  "started": string, // The datetime on which the worklog effort was started. Required when creating a worklog. Optional when updating a worklog.
  "timeSpent": string, // The time spent working on the issue as days (\#d), hours (\#h), or minutes (\#m or \#). Required when creating a worklog if `timeSpentSeconds` isn't provided. Optional when updating a worklog. Cannot be provided if `timeSpentSecond` is provided.
  "timeSpentSeconds": integer, // The time in seconds spent working on the issue. Required when creating a worklog if `timeSpent` isn't provided. Optional when updating a worklog. Cannot be provided if `timeSpent` is provided.
  "updateAuthor": any, // Details of the user who last updated the worklog.
  "updated": string, // The datetime on which the worklog was last updated.
  "visibility": any, // Details about any restrictions in the visibility of the worklog. Optional when creating or updating a worklog.
}
```
### Responses

#### 201 - Returned if the request is successful.

Schema (application/json):
```json
{
  "author": any, // Details of the user who created the worklog.
  "comment": any, // A comment about the worklog in [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/). Optional when creating or updating a worklog.
  "created": string, // The datetime on which the worklog was created.
  "id": string, // The ID of the worklog record.
  "issueId": string, // The ID of the issue this worklog is for.
  "properties": [
    {
      "key": string, // The key of the property. Required on create and update.
      "value": any, // The value of the property. Required on create and update.
    }
  ], // Details of properties for the worklog. Optional when creating or updating a worklog.
  "self": string, // The URL of the worklog item.
  "started": string, // The datetime on which the worklog effort was started. Required when creating a worklog. Optional when updating a worklog.
  "timeSpent": string, // The time spent working on the issue as days (\#d), hours (\#h), or minutes (\#m or \#). Required when creating a worklog if `timeSpentSeconds` isn't provided. Optional when updating a worklog. Cannot be provided if `timeSpentSecond` is provided.
  "timeSpentSeconds": integer, // The time in seconds spent working on the issue. Required when creating a worklog if `timeSpent` isn't provided. Optional when updating a worklog. Cannot be provided if `timeSpent` is provided.
  "updateAuthor": any, // Details of the user who last updated the worklog.
  "updated": string, // The datetime on which the worklog was last updated.
  "visibility": any, // Details about any restrictions in the visibility of the worklog. Optional when creating or updating a worklog.
}
```

#### 400 - Returned if:

 *  `adjustEstimate` is set to `new` but `newEstimate` is not provided or is invalid.
 *  `adjustEstimate` is set to `manual` but `reduceBy` is not provided or is invalid.
 *  the user does not have permission to add the worklog.
 *  the request JSON is malformed.

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if the issue is not found or the user does not have permission to view it.

#### 413 - Returned if the per-issue limit has been breached for one of the following fields:

 *  worklogs
 *  attachments

