# 03-Bulk edit dashboards [PUT]

`PUT /rest/api/3/dashboard/bulk/edit`

Bulk edit dashboards. Maximum number of dashboards to be edited at the same time is 100.

**[Permissions](#permissions) required:** None

The dashboards to be updated must be owned by the user, or the user must be an administrator.

### Request Body (application/json)

```json
{
  "action": enum("changeOwner" | "changePermission" | "addPermission" | "removePermission") (required), // Allowed action for bulk edit shareable entity
  "changeOwnerDetails": any, // The details of change owner action.
  "entityIds": [
    integer
  ] (required), // The id list of shareable entities to be changed.
  "extendAdminPermissions": boolean, // Whether the actions are executed by users with Administer Jira global permission.
  "permissionDetails": any, // The permission details to be changed.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"action\":\"changePermission\",\"entityErrors\":{\"10002\":{\"errorMessages\":[\"Only owner or editors of the dashboard can change permissions.\"],\"errors\":{}}}}"
```

#### 400 - Returned if the request is not valid.

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

