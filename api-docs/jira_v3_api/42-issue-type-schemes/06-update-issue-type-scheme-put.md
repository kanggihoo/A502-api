# 06-Update issue type scheme [PUT]

`PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}`

Updates an issue type scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeSchemeId` | `integer` | `path` | Yes | The ID of the issue type scheme. |

### Request Body (application/json)

```json
{
  "defaultIssueTypeId": string, // The ID of the default issue type of the issue type scheme.
  "description": string, // The description of the issue type scheme. The maximum length is 4000 characters.
  "name": string, // The name of the issue type scheme. The name must be unique. The maximum length is 255 characters.
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
"{\"errorMessages\":[\"The default issue type has to be one of the issue types of the scheme.\"],\"errors\":{}}"
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

