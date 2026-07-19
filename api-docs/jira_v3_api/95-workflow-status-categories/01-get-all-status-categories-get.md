# 01-Get all status categories [GET]

`GET /rest/api/3/statuscategory`

Returns a list of all status categories.

**[Permissions](#permissions) required:** Permission to access Jira.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"colorName\":\"yellow\",\"id\":1,\"key\":\"in-flight\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/1\"},{\"colorName\":\"green\",\"id\":9,\"key\":\"completed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/9\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

