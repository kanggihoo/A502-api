# 02-Create issue security scheme [POST]

`POST /rest/api/3/issuesecurityschemes`

Creates a security scheme with security scheme levels and levels' members. You can create up to 100 security scheme levels and security scheme levels' members per request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // The description of the issue security scheme.
  "levels": [
    {
      "description": string, // The description of the issue security scheme level.
      "isDefault": boolean, // Specifies whether the level is the default level. False by default.
      "members": [
        {
          "parameter": string, // The value corresponding to the specified member type.
          "type": string (required), // The issue security level member type, e.g `reporter`, `group`, `user`, `projectrole`, `applicationRole`.
        }
      ], // The list of level members which should be added to the issue security scheme level.
      "name": string (required), // The name of the issue security scheme level. Must be unique.
    }
  ], // The list of scheme levels which should be added to the security scheme.
  "name": string (required), // The name of the issue security scheme. Must be unique (case-insensitive).
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"10001\"}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"The length of the description must not exceed 4,000 characters.\"],\"errors\":{}}"
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

