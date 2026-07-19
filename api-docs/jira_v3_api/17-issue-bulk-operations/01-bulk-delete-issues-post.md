# 01-Bulk delete issues [POST]

`POST /rest/api/3/bulk/issues/delete`

Use this API to submit a bulk delete request. You can delete up to 1,000 issues in a single operation.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Delete [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Delete-issues/) in all projects that contain the selected issues.
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "selectedIssueIdsOrKeys": [
    string
  ] (required), // List of issue IDs or keys which are to be bulk deleted. These IDs or keys can be from different projects and issue types.
  "sendBulkNotification": boolean, // A boolean value that indicates whether to send a bulk change notification when the issues are being deleted.  If `true`, dispatches a bulk notification email to users about the updates.
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

#### 403 - Returned if the user does not have the necessary permission.

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

