# 03-Set default priority [PUT]

`PUT /rest/api/3/priority/default`

Sets default issue priority.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "id": string (required), // The ID of the new default issue priority. Must be an existing ID or null. Setting this to null erases the default priority setting.
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
"{\"errorMessages\":[\"The id has to be provided.\"],\"errors\":{}}"
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

#### 404 - Returned if the issue priority isn't found.

Example (application/json):
```json
"{\"errorMessages\":[\"Priority with ID 10000 not found.\"],\"errors\":{}}"
```

