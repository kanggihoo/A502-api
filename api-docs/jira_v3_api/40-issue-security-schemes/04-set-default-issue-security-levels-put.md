# 04-Set default issue security levels [PUT]

`PUT /rest/api/3/issuesecurityschemes/level/default`

Sets default issue security levels for schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "defaultValues": [
    {
      "defaultLevelId": string (required), // The ID of the issue security level to set as default for the specified scheme. Providing null will reset the default level.
      "issueSecuritySchemeId": string (required), // The ID of the issue security scheme to set default level for.
    }
  ] (required), // List of objects with issue security scheme ID and new default level ID.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"some-wrong-string is not a valid value. The issue security scheme ID must be a positive integer.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

#### 403 - Returned if the user doesn't have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"You are not authorized to perform this action. Administrator privileges are required.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue resolution isn't found.

Example (application/json):
```json
"{\"errorMessages\":[\"Issue security scheme with ID 10000 not found.\"],\"errors\":{}}"
```

