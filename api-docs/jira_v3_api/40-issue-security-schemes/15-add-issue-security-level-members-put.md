# 15-Add issue security level members [PUT]

`PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member`

Adds members to the issue security level. You can add up to 100 members per request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `schemeId` | `string` | `path` | Yes | The ID of the issue security scheme. |
| `levelId` | `string` | `path` | Yes | The ID of the issue security level. |

### Request Body (application/json)

```json
{
  "members": [
    {
      "parameter": string, // The value corresponding to the specified member type.
      "type": string (required), // The issue security level member type, e.g `reporter`, `group`, `user`, `projectrole`, `applicationRole`.
    }
  ], // The list of level members which should be added to the issue security scheme level.
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

#### 404 - Returned if the security scheme isn't found.

Example (application/json):
```json
"{\"errorMessages\":[\"Issue security scheme with ID 10000 not found.\"],\"errors\":{}}"
```

