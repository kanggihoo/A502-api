# 05-Get available transitions [GET]

`GET /rest/api/3/bulk/issues/transition`

Use this API to retrieve a list of transitions available for the specified issues that can be used or bulk transition operations. You can submit either single or multiple issues in the query to obtain the available transitions.

The response will provide the available transitions for issues, organized by their respective workflows. **Only the transitions that are common among the issues within that workflow and do not involve any additional field updates will be included.** For bulk transitions that require additional field updates, please utilise the Jira Cloud UI.

You can request available transitions for up to 1,000 issues in a single operation. This API uses pagination to return responses, delivering 50 workflows at a time.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Transition [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Transition-issues/) in all projects that contain the selected issues.
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdsOrKeys` | `string` | `query` | Yes | Comma (,) separated Ids or keys of the issues to get transitions available for them. |
| `endingBefore` | `string` | `query` | No | (Optional)The end cursor for use in pagination. |
| `startingAfter` | `string` | `query` | No | (Optional)The start cursor for use in pagination. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"availableTransitions\":[{\"isTransitionsFiltered\":false,\"issues\":[\"EPIC-1\",\"TASK-1\"],\"transitions\":[{\"to\":{\"statusId\":10001,\"statusName\":\"To Do\"},\"transitionId\":11,\"transitionName\":\"To Do\"},{\"to\":{\"statusId\":10002,\"statusName\":\"In Progress\"},\"transitionId\":21,\"transitionName\":\"In Progress\"},{\"to\":{\"statusId\":10003,\"statusName\":\"Done\"},\"transitionId\":31,\"transitionName\":\"Done\"}]},{\"isTransitionsFiltered\":true,\"issues\":[\"BUG-1\"],\"transitions\":[{\"to\":{\"statusId\":10004,\"statusName\":\"To Do bug\"},\"transitionId\":41,\"transitionName\":\"To Do bug\"},{\"to\":{\"statusId\":10005,\"statusName\":\"Triage\"},\"transitionId\":51,\"transitionName\":\"Triage\"}]}]}"
```

#### 400 - Returned if the request is not valid. For example, if a provided issue ID or key is invalid.

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

