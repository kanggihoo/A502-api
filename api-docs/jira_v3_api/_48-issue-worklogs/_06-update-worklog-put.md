# 06-Update worklog [PUT]

`PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`

Updates a worklog.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key the issue. |
| `id` | `string` | `path` | Yes | The ID of the worklog. |
| `notifyUsers` | `boolean` | `query` | No | Whether users watching the issue are notified by email. |
| `adjustEstimate` | `string` | `query` | No | Defines how to update the issue's time estimate, the options are:<br><br> *  `new` Sets the estimate to a specific value, defined in `newEstimate`.<br> *  `leave` Leaves the estimate unchanged.<br> *  `auto` Updates the estimate by the difference between the original and updated value of `timeSpent` or `timeSpentSeconds`. |
| `newEstimate` | `string` | `query` | No | The value to set as the issue's remaining time estimate, as days (\#d), hours (\#h), or minutes (\#m or \#). For example, *2d*. Required when `adjustEstimate` is `new`. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties`, which returns worklog properties. |
| `overrideEditableFlag` | `boolean` | `query` | No | Whether the worklog should be added to the issue even if the issue is not editable. For example, because the issue is closed. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can use this flag. |

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

#### 200 - Returned if the request is successful

Example (application/json):
```json
"{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"comment\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"I did some work here.\"}]}]},\"id\":\"100028\",\"issueId\":\"10002\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000\",\"started\":\"2021-01-17T12:34:00.000+0000\",\"timeSpent\":\"3h 20m\",\"timeSpentSeconds\":12000,\"updateAuthor\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"updated\":\"2021-01-18T23:45:00.000+0000\",\"visibility\":{\"identifier\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"type\":\"group\",\"value\":\"jira-developers\"}}"
```

#### 400 - Returned if:

 *  `adjustEstimate` is set to `new` but `newEstimate` is not provided or is invalid.
 *  the user does not have permission to update the worklog.
 *  the request JSON is malformed.

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if:

 *  the issue is not found or user does not have permission to view the issue.
 *  the worklog is not found or the user does not have permission to view it.
 *  time tracking is disabled.

