# 01-Get Connect issue field migration task [GET]

`GET /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task`

Returns the details of a Connect issue field's migration to Forge.

When migrating a Connect app to Forge, [Issue Field](https://developer.atlassian.com/cloud/jira/software/modules/issue-field/) modules
must be converted to [Custom field](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/). When the
Forge version of the app is installed, Forge creates a
[background task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-group-tasks) to track the
migration of field data across. This endpoint returns the status and other details of that background task.

For more details, see
[Jira modules > Jira Custom Fields](https://developer.atlassian.com/platform/adopting-forge-from-connect/migrate-jira-custom-fields/).

**[Permissions](#permissions) required:** Only Connect and Forge apps can make this request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `connectKey` | `string` | `path` | Yes | The key of the Connect app that contains the Jira issue field being migrated. |
| `jiraIssueFieldsKey` | `string` | `path` | Yes | The module key of the Connect issue field being migrated. |

### Responses

#### 200 - Returned if the request is successful and a migration task is found.

Schema (application/json):
```json
{
  "description": string, // The description of the task.
  "elapsedRuntime": integer (required), // The execution time of the task, in milliseconds.
  "finished": string, // A timestamp recording when the task was finished.
  "id": string (required), // The ID of the task.
  "lastUpdate": string (required), // A timestamp recording when the task progress was last updated.
  "message": string, // Information about the progress of the task.
  "progress": integer (required), // The progress of the task, as a percentage complete.
  "result": any, // The result of the task execution.
  "self": string (required), // The URL of the task.
  "started": string, // A timestamp recording when the task was started.
  "status": enum("ENQUEUED" | "RUNNING" | "COMPLETE" | "FAILED" | "CANCEL_REQUESTED" | "CANCELLED" | "DEAD") (required), // The status of the task.
  "submitted": string, // A timestamp recording when the task was submitted.
  "submittedBy": integer (required), // The ID of the user who submitted the task.
}
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Example (application/json):
```json
{
  "message": "Access to this resource must be authenticated as an app.",
  "statusCode": 401
}
```

#### 404 - Returned if:
* no migrated Forge module with the given key is found.
* no ongoing migration task exists for the custom field.

Example (application/json):
```json
{
  "message": "No ongoing migration task for the custom field.",
  "statusCode": 404
}
```

