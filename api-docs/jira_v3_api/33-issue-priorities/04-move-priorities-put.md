# 04-Move priorities [PUT]

`PUT /rest/api/3/priority/move`

Changes the order of issue priorities.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "after": string, // The ID of the priority. Required if `position` isn't provided.
  "ids": [
    string
  ] (required), // The list of issue IDs to be reordered. Cannot contain duplicates nor after ID.
  "position": string, // The position for issue priorities to be moved to. Required if `after` isn't provided.
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
"{\"errorMessages\":[\"The ids must contain no more than 1,000 items.\"],\"errors\":{}}"
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

