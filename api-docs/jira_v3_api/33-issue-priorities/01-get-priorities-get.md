# 01-Get priorities [GET]

`GET /rest/api/3/priority`

Returns the list of all issue priorities.

**Deprecated:** Use [Search priorities](#api-rest-api-3-priority-search-get) instead. **[Permissions](#permissions) required:** Permission to access Jira.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"description\":\"Major loss of function.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/priorities/major.png\",\"id\":\"1\",\"name\":\"Major\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/priority/3\",\"statusColor\":\"#009900\"},{\"description\":\"Very little impact.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/priorities/trivial.png\",\"id\":\"2\",\"name\":\"Trivial\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/priority/5\",\"statusColor\":\"#cfcfcf\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect.

