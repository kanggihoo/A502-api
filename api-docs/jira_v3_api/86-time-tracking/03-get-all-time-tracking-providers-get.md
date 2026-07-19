# 03-Get all time tracking providers [GET]

`GET /rest/api/3/configuration/timetracking/list`

Returns all time tracking providers. By default, Jira only has one time tracking provider: *JIRA provided time tracking*. However, you can install other time tracking providers via apps from the Atlassian Marketplace. For more information on time tracking providers, see the documentation for the [ Time Tracking Provider](https://developer.atlassian.com/cloud/jira/platform/modules/time-tracking-provider/) module.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"key\":\"Jira\",\"name\":\"JIRA provided time tracking\",\"url\":\"/example/config/url\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

