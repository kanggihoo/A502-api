# 02-Create issue type scheme [POST]

`POST /rest/api/3/issuetypescheme`

Creates an issue type scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "defaultIssueTypeId": string, // The ID of the default issue type of the issue type scheme. This ID must be included in `issueTypeIds`.
  "description": string, // The description of the issue type scheme. The maximum length is 4000 characters.
  "issueTypeIds": [
    string
  ] (required), // The list of issue types IDs of the issue type scheme. At least one standard issue type ID is required.
  "name": string (required), // The name of the issue type scheme. The name must be unique. The maximum length is 255 characters.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueTypeSchemeId\":\"10010\"}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The default issue type ID has to be present in issue type IDs list.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type schemes.\"],\"errors\":{}}"
```

#### 409 - Returned if the scheme name is used by another scheme.

Example (application/json):
```json
"{\"errorMessages\":[\"The name is used by another scheme.\"],\"errors\":{}}"
```

