# 02-Get data policy for projects [GET]

`GET /rest/api/3/data-policy/project`

Returns data policies for the projects specified in the request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `ids` | `string` | `query` | No | A list of project identifiers. This parameter accepts a comma-separated list. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"projectDataPolicies\":[{\"dataPolicy\":{\"anyContentBlocked\":false},\"id\":1000},{\"dataPolicy\":{\"anyContentBlocked\":true},\"id\":1001}]}"
```

#### 400 - Returned if the request is not valid or includes invalid or not-permitted project identifiers.

Example (application/json):
```json
"{\"errorMessages\":[\"Invalid request: some projects are not available or do not exist.\"],\"errors\":{}}"
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

