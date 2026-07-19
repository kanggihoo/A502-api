# 01-Get resolutions [GET]

`GET /rest/api/3/resolution`

Returns a list of all issue resolution values.

**[Permissions](#permissions) required:** Permission to access Jira.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"description\":\"A fix for this issue is checked into the tree and tested.\",\"id\":\"10000\",\"name\":\"Fixed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/resolution/1\"},{\"description\":\"This is what it is supposed to do.\",\"id\":\"10001\",\"name\":\"Works as designed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/resolution/3\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

