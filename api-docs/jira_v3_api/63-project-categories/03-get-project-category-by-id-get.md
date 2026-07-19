# 03-Get project category by ID [GET]

`GET /rest/api/3/projectCategory/{id}`

Returns a project category.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the project category. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the project category is not found.

