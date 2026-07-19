# 14-Set workflow for issue type in workflow scheme [PUT]

`PUT /rest/api/3/workflowscheme/{id}/issuetype/{issueType}`

Sets the workflow for an issue type in a workflow scheme.

Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new issue type-workflow mapping. The draft workflow scheme can be published in Jira.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow scheme. |
| `issueType` | `string` | `path` | Yes | The ID of the issue type. |

### Request Body (application/json)

```json
{
  "issueType": string, // The ID of the issue type. Not required if updating the issue type-workflow mapping.
  "updateDraftIfNeeded": boolean, // Set to true to create or update the draft of a workflow scheme and update the mapping in the draft, when the workflow scheme cannot be edited. Defaults to `false`. Only applicable when updating the workflow-issue types mapping.
  "workflow": string, // The name of the workflow.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultWorkflow\":\"jira\",\"description\":\"The description of the example workflow scheme.\",\"draft\":false,\"id\":101010,\"issueTypeMappings\":{\"10000\":\"scrum workflow\",\"10001\":\"builds workflow\"},\"name\":\"Example workflow scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/workflowscheme/101010\"}"
```

#### 400 - Returned if the workflow cannot be edited and `updateDraftIfNeeded` is false.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the workflow scheme or issue type is not found.

