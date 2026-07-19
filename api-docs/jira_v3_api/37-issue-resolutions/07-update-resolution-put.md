# 07-Update resolution [PUT]

`PUT /rest/api/3/resolution/{id}`

Updates an issue resolution.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue resolution. |

### Request Body (application/json)

```json
{
  "description": string, // The description of the resolution.
  "name": string (required), // The name of the resolution. Must be unique.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request isn't valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The length of the description must not exceed 255 characters.\"],\"errors\":{}}"
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
"{\"errorMessages\":[\"Resolution with ID 10000 not found.\"],\"errors\":{}}"
```

