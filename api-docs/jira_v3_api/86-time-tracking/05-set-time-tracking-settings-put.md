# 05-Set time tracking settings [PUT]

`PUT /rest/api/3/configuration/timetracking/options`

Sets the time tracking settings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "defaultUnit": enum("minute" | "hour" | "day" | "week") (required), // The default unit of time applied to logged time.
  "timeFormat": enum("pretty" | "days" | "hours") (required), // The format that will appear on an issue's *Time Spent* field.
  "workingDaysPerWeek": number (required), // The number of days in a working week.
  "workingHoursPerDay": number (required), // The number of hours in a working day.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultUnit\":\"hour\",\"timeFormat\":\"pretty\",\"workingDaysPerWeek\":5.5,\"workingHoursPerDay\":7.6}"
```

#### 400 - Returned if the request object is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

