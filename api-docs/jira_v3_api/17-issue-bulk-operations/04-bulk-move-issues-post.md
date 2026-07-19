# 04-Bulk move issues [POST]

`POST /rest/api/3/bulk/issues/move`

Use this API to submit a bulk issue move request. You can move multiple issues from multiple projects in a single request, but they must all be moved to a single project, issue type, and parent. You can't move more than 1000 issues (including subtasks) at once.

#### Scenarios: ####

This is an early version of the API and it doesn't have full feature parity with the Bulk Move UI experience.

 *  Moving issue of type A to issue of type B in the same project or a different project: `SUPPORTED`
 *  Moving multiple issues of type A in one or more projects to multiple issues of type B in one of the source projects or a different project: `SUPPORTED`
 *  Moving issues of multiple issue types in one or more projects to issues of a single issue type in one of the source project or a different project: **`SUPPORTED`**  
    E.g. Moving issues of story and task issue types in project 1 and project 2 to issues of task issue type in project 3
 *  Moving a standard parent issue of type A with its multiple subtask issue types in one project to standard issue of type B and multiple subtask issue types in the same project or a different project: `SUPPORTED`
 *  Moving standard issues with their subtasks to a parent issue in the same project or a different project without losing their relation: `SUPPORTED`
 *  Moving an epic issue with its child issues to a different project without losing their relation: `SUPPORTED`  
    This usecase is **supported using multiple requests**. Move the epic in one request and then move the children in a separate request with target parent set to the epic issue id  
      
    (Alternatively, move them individually and stitch the relationship back with the Bulk Edit API)

#### Limits applied to bulk issue moves: ####

When using the bulk move, keep in mind that there are limits on the number of issues and fields you can include.

 *  You can move up to 1,000 issues in a single operation, including any subtasks.
 *  The total combined number of fields across all issues must not exceed 1,500,000. For example, if each issue includes 15,000 fields, then the maximum number of issues that can be moved is 100.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Move [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in source projects.
 *  Create [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in destination projects.
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in destination projects, if moving subtasks only.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "sendBulkNotification": boolean, // A boolean value that indicates whether to send a bulk change notification when the issues are being moved.  If `true`, dispatches a bulk notification email to users about the updates.
  "targetToSourcesMapping": {}, // An object representing the mapping of issues and data related to destination entities, like fields and statuses, that are required during a bulk move.  The key is a string that is created by concatenating the following three entities in order, separated by commas. The format is `<project ID or key>,<issueType ID>,<parent ID or key>`. It should be unique across mappings provided in the payload. If you provide multiple mappings for the same key, only one will be processed. However, the operation won't fail, so the error may be hard to track down.   *  ***Destination project*** (Required): ID or key of the project to which the issues are being moved.  *  ***Destination issueType*** (Required): ID of the issueType to which the issues are being moved.  *  ***Destination parent ID or key*** (Optional): ID or key of the issue which will become the parent of the issues being moved. Only required when the destination issueType is a subtask.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"taskId\":\"10641\"}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errors\":[{\"message\":\"Some of the issues in the issueIdsOrKeys are not valid\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errors": [
    {
      "message": string,
    }
  ],
}
```

