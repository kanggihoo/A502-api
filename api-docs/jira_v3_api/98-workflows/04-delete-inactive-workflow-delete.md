# 04-Delete inactive workflow [DELETE]

`DELETE /rest/api/3/workflow/{entityId}`

Deletes a workflow.

The workflow cannot be deleted if it is:

 *  an active workflow.
 *  a system workflow.
 *  associated with any workflow scheme.
 *  associated with any draft workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `entityId` | `string` | `path` | Yes | The entity ID of the workflow. |

### Responses

#### 204 - Returned if the workflow is deleted.

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Cannot delete an active workflow.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access the workflow configuration.\"],\"errors\":{}}"
```

#### 404 - Returned if the workflow is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The workflow was not found.\"],\"errors\":{}}"
```

