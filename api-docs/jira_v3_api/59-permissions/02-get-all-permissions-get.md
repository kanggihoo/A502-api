# 02-Get all permissions [GET]

`GET /rest/api/3/permissions`

Returns all permissions, including:

 *  global permissions.
 *  project permissions.
 *  global permissions added by plugins.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"permissions\":{\"BULK_CHANGE\":{\"description\":\"Ability to modify a collection of issues at once. For example, resolve multiple issues in one step.\",\"key\":\"BULK_CHANGE\",\"name\":\"Bulk Change\",\"type\":\"GLOBAL\"}}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

