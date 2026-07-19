# 23-Export archived issue(s) [PUT]

`PUT /rest/api/3/issues/archive/export`

Enables admins to retrieve details of all archived issues. Upon a successful request, the admin who submitted it will receive an email with a link to download a CSV file with the issue details.

Note that this API only exports the values of system fields and archival-specific fields (`ArchivedBy` and `ArchivedDate`). Custom fields aren't supported.

**[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

**License required:** Premium or Enterprise

**Signed-in users only:** This API can't be accessed anonymously.

**Rate limiting:** Only a single request can be active at any given time.

  


### Request Body (application/json)

```json
{
  "archivedBy": [
    string
  ], // List archived issues archived by a specified account ID.
  "archivedDateRange": {
    "dateAfter": string (required), // List issues archived after a specified date, passed in the YYYY-MM-DD format.
    "dateBefore": string (required), // List issues archived before a specified date provided in the YYYY-MM-DD format.
  },
  "issueTypes": [
    string
  ], // List archived issues with a specified issue type ID.
  "projects": [
    string
  ], // List archived issues with a specified project key.
  "reporters": [
    string
  ], // List archived issues where the reporter is a specified account ID.
}
```
### Responses

#### 202 - Returns the details of your export task. You can use the [get task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) API to view the progress of your request.

Example (application/json):
```json
"{\"payload\":\"{projects=[FOO, BAR], reporters=[uuid-rep-001, uuid-rep-002], issueTypes=[10001, 10002], archivedDate={dateAfterInstant=2023-01-01, dateBeforeInstant=2023-01-12}, archivedBy=[uuid-rep-001, uuid-rep-002]}\",\"progress\":0,\"status\":\"ENQUEUED\",\"submittedTime\":1623230887000,\"taskId\":\"10990\"}"
```

#### 400 - Returned when:

 *  The request is invalid, or the filters provided are incorrect
 *  You requested too many issues for export. The limit is one million issues per request

Example (application/json):
```json
"[\"Your filter contains invalid values {errorMessage}\"]"
```

#### 401 - Returned if no issues were unarchived because the provided authentication credentials are either missing or invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"User is not logged in.\"],\"errors\":{}}"
```

#### 403 - Returned if no issues were unarchived because the user lacks the required Jira admin or site admin permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"User is not an admin.\"],\"errors\":{}}"
```

#### 412 - Returned if a request to export archived issues is already running.

Example (application/json):
```json
"{\"errorMessages\":[\"An issue archival task is already running with ID 1010. To start a new one, cancel the task or wait for it to finish.\"],\"errors\":{}}"
```

