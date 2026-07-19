# 01-Get default share scope [GET]

`GET /rest/api/3/filter/defaultShareScope`

Returns the default sharing settings for new filters and dashboards for a user.

**[Permissions](#permissions) required:** Permission to access Jira.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"scope\":\"GLOBAL\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

