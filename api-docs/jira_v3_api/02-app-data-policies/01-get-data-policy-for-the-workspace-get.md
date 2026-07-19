# 01-Get data policy for the workspace [GET]

`GET /rest/api/3/data-policy`

Returns data policy for the workspace.

### Responses

#### 200 - Returned if the request is successful

Example (application/json):
```json
"{\"anyContentBlocked\":false}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Example (application/json):
```json
"{\"errorMessages\":[\"Only apps can access this resource.\"],\"errors\":{}}"
```

#### 403 - Returned if the client is not authorized to make the request.

Example (application/json):
```json
"{\"errorMessages\":[\"\"],\"errors\":{}}"
```

