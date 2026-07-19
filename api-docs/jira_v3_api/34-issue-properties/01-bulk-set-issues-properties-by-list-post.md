# 01-Bulk set issues properties by list [POST]

`POST /rest/api/3/issue/properties`

Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can be specified along with up to 10,000 issues on which to set or update that list of entity properties.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON. The maximum length of single issue property value is 32768 characters. This operation can be accessed anonymously.

This operation is:

 *  transactional, either all properties are updated in all eligible issues or, when errors occur, no properties are updated.
 *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "entitiesIds": [
    integer
  ], // A list of entity property IDs.
  "properties": {}, // A list of entity property keys and values.
}
```
### Responses

#### 303 - Returned if the operation is successful.

#### 400 - Return if the request is invalid or the user does not have the necessary permission.

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

#### 401 - Returned if the authentication credentials are incorrect.

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

#### 409 - Returned if another bulk update on the same issues is already in progress. Retry the request later.

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

