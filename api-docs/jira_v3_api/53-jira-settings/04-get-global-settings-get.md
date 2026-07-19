# 04-Get global settings [GET]

`GET /rest/api/3/configuration`

Returns the [global settings](https://confluence.atlassian.com/x/qYXKM) in Jira. These settings determine whether optional features (for example, subtasks, time tracking, and others) are enabled. If time tracking is enabled, this operation also returns the time tracking configuration.

**[Permissions](#permissions) required:** Permission to access Jira.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"attachmentsEnabled\":true,\"issueLinkingEnabled\":true,\"subTasksEnabled\":false,\"timeTrackingConfiguration\":{\"defaultUnit\":\"day\",\"timeFormat\":\"pretty\",\"workingDaysPerWeek\":5.0,\"workingHoursPerDay\":8.0},\"timeTrackingEnabled\":true,\"unassignedIssuesAllowed\":false,\"votingEnabled\":true,\"watchingEnabled\":true}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

