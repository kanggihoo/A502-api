# 03-Bulk edit issues [POST]

`POST /rest/api/3/bulk/issues/fields`

Use this API to submit a bulk edit request and simultaneously edit multiple issues. There are limits applied to the number of issues and fields that can be edited. A single request can accommodate a maximum of 1000 issues (including subtasks) and 200 fields.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  Edit [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "editedFieldsInput": any (required), // An object that defines the values to be updated in specified fields of an issue. The structure and content of this parameter vary depending on the type of field being edited. Although the order is not significant, ensure that field IDs align with those in selectedActions.
  "selectedActions": [
    string
  ] (required), // List of all the field IDs that are to be bulk edited. Each field ID in this list corresponds to a specific attribute of an issue that is set to be modified in the bulk edit operation. The relevant field ID can be obtained by calling the Bulk Edit Get Fields REST API (documentation available on this page itself).
  "selectedIssueIdsOrKeys": [
    string
  ] (required), // List of issue IDs or keys which are to be bulk edited. These IDs or keys can be from different projects and issue types.
  "sendBulkNotification": boolean, // A boolean value that indicates whether to send a bulk change notification when the issues are being edited.  If `true`, dispatches a bulk notification email to users about the updates.
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
"{\"errors\":[{\"message\":\"The following editedFieldInput values are not listed as selectedActions : issuetype\"}]}"
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

