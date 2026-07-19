# 02-Create issue type screen scheme [POST]

`POST /rest/api/3/issuetypescreenscheme`

Creates an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "description": string, // The description of the issue type screen scheme. The maximum length is 255 characters.
  "issueTypeMappings": [
    {
      "issueTypeId": string (required), // The ID of the issue type or *default*. Only issue types used in classic projects are accepted. An entry for *default* must be provided and defines the mapping for all issue types without a screen scheme.
      "screenSchemeId": string (required), // The ID of the screen scheme. Only screen schemes used in classic projects are accepted.
    }
  ] (required), // The IDs of the screen schemes for the issue type IDs and *default*. A *default* entry is required to create an issue type screen scheme, it defines the mapping for all issue types without a screen scheme.
  "name": string (required), // The name of the issue type screen scheme. The name must be unique. The maximum length is 255 characters.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"10001\"}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"One or more issue type IDs are repeated, an issue type ID can only be specified once.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type screen schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type or screen scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"One or more issue type IDs were not found.\"],\"errors\":{}}"
```

#### 409 - Returned if the issue type is a sub-task, but sub-tasks are disabled in Jira settings.

Example (application/json):
```json
"{\"errorMessages\":[\"Sub-tasks are disabled in Jira. At least one of the issue types is a sub-task.\"],\"errors\":{}}"
```

