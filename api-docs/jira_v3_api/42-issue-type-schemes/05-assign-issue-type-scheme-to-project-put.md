# 05-Assign issue type scheme to project [PUT]

`PUT /rest/api/3/issuetypescheme/project`

Assigns an issue type scheme to a project.

If any issues in the project are assigned issue types not present in the new scheme, the operation will fail. To complete the assignment those issues must be updated to use issue types in the new scheme.

Issue type schemes can only be assigned to classic projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "issueTypeSchemeId": string (required), // The ID of the issue type scheme.
  "projectId": string (required), // The ID of the project.
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
"{\"errorMessages\":[\"This issue type scheme can't be assigned to the project. This is because some issues in this project use issue types not present in the scheme. Before assigning the scheme to the project, update the issue types on these issues: 7\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type scheme or the project is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type scheme was not found.\"],\"errors\":{}}"
```

