# 11-Delete issue security scheme [DELETE]

`DELETE /rest/api/3/issuesecurityschemes/{schemeId}`

Deletes an issue security scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `schemeId` | `string` | `path` | Yes | The ID of the issue security scheme. |

### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"\"You can't delete an issue security scheme if any projects are associated with it.\""
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

#### 404 - Returned if the issue security scheme isn't found.

Example (application/json):
```json
"{\"errorMessages\":[\"Issue security scheme with ID 10000 not found.\"],\"errors\":{}}"
```

