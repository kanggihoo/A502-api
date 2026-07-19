# 11-Assign field configuration scheme to project [PUT]

`PUT /rest/api/3/fieldconfigurationscheme/project`

Deprecated, use [ Field schemes](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-field-schemes/#api-group-field-schemes) which supports field association schemes.

Assigns a field configuration scheme to a project. If the field configuration scheme ID is `null`, the operation assigns the default field configuration scheme.

Field configuration schemes can only be assigned to classic projects.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "fieldConfigurationSchemeId": string, // The ID of the field configuration scheme. If the field configuration scheme ID is `null`, the operation assigns the default field configuration scheme.
  "projectId": string (required), // The ID of the project.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the project is not a classic project.

Example (application/json):
```json
"{\"errorMessages\":[\"Only classic projects can have field configuration schemes assigned.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access field configurations.\"],\"errors\":{}}"
```

#### 404 - Returned if the project is missing.

Example (application/json):
```json
"{\"errorMessages\":[\"The project was not found.\"],\"errors\":{}}"
```

