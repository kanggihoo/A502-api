# 02-Bulk set issue properties by issue [POST]

`POST /rest/api/3/issue/properties/multi`

Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.

This operation is:

 *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.
 *  non-transactional. Updating some entities may fail. Such information will available in the task result.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "issues": [
    {
      "issueID": integer, // The ID of the issue.
      "properties": {}, // Entity properties to set on the issue. The maximum length of an issue property value is 32768 characters.
    }
  ], // A list of issue IDs and their respective properties.
}
```
### Responses

#### 303 - Returned if the operation is successful.

#### 400 - Return if the request is invalid.

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

#### 403 - Return if the user does not have the necessary permission.

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

