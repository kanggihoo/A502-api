# 02-Submit Connect issue field migration task [POST]

`POST /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task`

Submits a request to trigger migration of connect issue field to its Forge custom field counterpart.

When migrating a Connect app to Forge, [Issue Field](https://developer.atlassian.com/cloud/jira/software/modules/issue-field/) modules
must be converted to [Custom field](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/) modules.
This endpoint triggers the background migration of field data. Use the GET endpoint to retrieve
the status and progress of the task.

For more details, see
[Jira modules > Jira Custom Fields](https://developer.atlassian.com/platform/adopting-forge-from-connect/migrate-jira-custom-fields/).

**[Permissions](#permissions) required:** Only Connect and Forge apps can make this request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `connectKey` | `string` | `path` | Yes | The key of the Connect app that contains the Jira issue field being migrated. |
| `jiraIssueFieldsKey` | `string` | `path` | Yes | The module key of the Connect issue field being migrated. |

### Responses

#### 202 - Returned if the migration task was submitted successfully.

#### 401 - Returned if the authentication credentials are incorrect or missing.

Example (application/json):
```json
{
  "message": "Access to this resource must be authenticated as an app.",
  "statusCode": 401
}
```

#### 404 - Returned if no migrated Forge module with the given key is found.

Example (application/json):
```json
{
  "message": "No migrated Forge module with given key is found.",
  "statusCode": 404
}
```

#### 409 - Returned if a migration task is already in progress for the field.

Example (application/json):
```json
{
  "message": "Failed to trigger migration task because of already in progress task for the field.",
  "statusCode": 409
}
```

