# 02-Get approximate license count [GET]

`GET /rest/api/3/license/approximateLicenseCount`

Returns the approximate number of user accounts across all Jira licenses. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"key\":\"license.totalApproximateUserCount\",\"value\":\"1000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{}
```

#### 403 - Returned if the user does not have permission to complete this request.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access license details.\"],\"errors\":{}}"
```

