# 01-Get selected time tracking provider [GET]

`GET /rest/api/3/configuration/timetracking`

Returns the time tracking provider that is currently selected. Note that if time tracking is disabled, then a successful but empty response is returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful and time tracking is enabled.

Example (application/json):
```json
"{\"key\":\"Jira\",\"name\":\"JIRA provided time tracking\",\"url\":\"/example/config/url\"}"
```

#### 204 - Returned if the request is successful but time tracking is disabled.

Schema (application/json):
```json
any
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

