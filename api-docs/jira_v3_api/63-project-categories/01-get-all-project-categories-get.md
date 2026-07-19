# 01-Get all project categories [GET]

`GET /rest/api/3/projectCategory`

Returns all project categories.

**[Permissions](#permissions) required:** Permission to access Jira.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},{\"description\":\"Second Project Category\",\"id\":\"10001\",\"name\":\"SECOND\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10001\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

