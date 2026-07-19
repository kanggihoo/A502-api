# 07-Delete issue type scheme [DELETE]

`DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}`

Deletes an issue type scheme.

Only issue type schemes used in classic projects can be deleted. Only issue type schemes not associated with a project can be deleted

A validation error will be returned if the specified scheme is associated with one or more projects. Use [Get issue type scheme API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-get) (with the projects expand, and id query parameter) to get a list of projects. Then, use [Assign issue type scheme to project API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-type-schemes/#api-rest-api-3-issuetypescheme-project-put) to associate all projects to another scheme before deleting.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeSchemeId` | `integer` | `path` | Yes | The ID of the issue type scheme. |

### Responses

#### 204 - Returned if the issue type scheme is deleted.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is to delete the default issue type scheme or if the scheme is associated with a project

Example (application/json):
```json
"{\"errorMessages\":[\"The default issue type scheme can't be removed.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type scheme was not found.\"],\"errors\":{}}"
```

