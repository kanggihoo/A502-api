# 05-Archive issue(s) by JQL [POST]

`POST /rest/api/3/issue/archive`

Enables admins to archive up to 100,000 issues in a single request using JQL, returning the URL to check the status of the submitted request.

You can use the [get task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) and [cancel task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-cancel-post) APIs to manage the request.

**Note that:**

 *  you can't archive subtasks directly, only through their parent issues
 *  you can only archive issues from software, service management, and business projects

**[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

**License required:** Premium or Enterprise

**Signed-in users only:** This API can't be accessed anonymously.

**Rate limiting:** Only a single request per jira instance can be active at any given time.

  


### Request Body (application/json)

```json
{
  "jql": string,
}
```
### Responses

#### 202 - Returns the URL to check the status of the submitted request.

Example (application/json):
```json
"\"https://your-domain.atlassian.net/rest/api/3/task/1010\""
```

#### 400 - Returned if no issues were archived due to a bad request, for example an invalid JQL query.

Example (application/json):
```json
"{\"errorMessages\":[\"Invalid JQL. Bad request.\"],\"errors\":{}}"
```

#### 401 - Returned if no issues were archived because the provided authentication credentials are either missing or invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"User is not logged in.\"],\"errors\":{}}"
```

#### 403 - Returned if no issues were archived because the user lacks the required Jira admin or site admin permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Archiving issues is only available for premium editions of Jira.\"],\"errors\":{}}"
```

#### 412 - Returned if a request to archive issue(s) is already running.

Example (application/json):
```json
"{\"errorMessages\":[\"An issue archival task is already running with ID 1010. To start a new one, cancel the task or wait for it to finish.\"],\"errors\":{}}"
```

