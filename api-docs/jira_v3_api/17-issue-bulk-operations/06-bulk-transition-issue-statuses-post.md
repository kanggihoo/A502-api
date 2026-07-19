# 06-Bulk transition issue statuses [POST]

`POST /rest/api/3/bulk/issues/transition`

Use this API to submit a bulk issue status transition request. You can transition multiple issues, alongside with their valid transition Ids. You can transition up to 1,000 issues in a single operation.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Transition [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Transition-issues/) in all projects that contain the selected issues.
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "bulkTransitionInputs": [
    {
      "selectedIssueIdsOrKeys": [
        string
      ] (required), // List of all the issue IDs or keys that are to be bulk transitioned.
      "transitionId": string (required), // The ID of the transition that is to be performed on the issues.
    }
  ] (required), // List of objects and each object has two properties:   *  Issues that will be bulk transitioned.  *  TransitionId that corresponds to a specific transition of issues that share the same workflow.
  "sendBulkNotification": boolean, // A boolean value that indicates whether to send a bulk change notification when the issues are being transitioned.  If `true`, dispatches a bulk notification email to users about the updates.
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

