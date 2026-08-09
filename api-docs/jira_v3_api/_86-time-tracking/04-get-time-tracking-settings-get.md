# 04-Get time tracking settings [GET]

`GET /rest/api/3/configuration/timetracking/options`

Returns the time tracking settings. This includes settings such as the time format, default time unit, and others. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultUnit\":\"hour\",\"timeFormat\":\"pretty\",\"workingDaysPerWeek\":5.5,\"workingHoursPerDay\":7.6}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

