# 05-Assign issue type screen scheme to project [PUT]

`PUT /rest/api/3/issuetypescreenscheme/project`

Assigns an issue type screen scheme to a project.

Issue type screen schemes can only be assigned to classic projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "issueTypeScreenSchemeId": string, // The ID of the issue type screen scheme.
  "projectId": string, // The ID of the project.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if:

 *  project is not found.
 *  issue type screen scheme is not found.
 *  the project is not a classic project.

Example (application/json):
```json
"{\"errorMessages\":[\"Only classic projects can have issue type screen schemes assigned.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type screen schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type screen scheme or the project are missing.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type screen scheme was not found.\"],\"errors\":{}}"
```

