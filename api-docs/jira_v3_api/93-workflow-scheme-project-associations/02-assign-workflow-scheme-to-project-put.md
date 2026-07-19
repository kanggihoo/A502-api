# 02-Assign workflow scheme to project [PUT]

`PUT /rest/api/3/workflowscheme/project`

Assigns a workflow scheme to a project. This operation is performed only when there are no issues in the project.

Workflow schemes can only be assigned to classic projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "projectId": string (required), // The ID of the project.
  "workflowSchemeId": string, // The ID of the workflow scheme. If the workflow scheme ID is `null`, the operation assigns the default workflow scheme.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Only classic projects can have workflow schemes assigned.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access workflow scheme associations.\"],\"errors\":{}}"
```

#### 404 - Returned if the workflow scheme or the project are not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The workflow scheme was not found.\"],\"errors\":{}}"
```

