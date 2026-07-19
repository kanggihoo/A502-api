# 12-Unarchive issue(s) by issue keys/ID [PUT]

`PUT /rest/api/3/issue/unarchive`

Enables admins to unarchive up to 1000 issues in a single request using issue ID/key, returning details of the issue(s) unarchived in the process and the errors encountered, if any.

**Note that:**

 *  you can't unarchive subtasks directly, only through their parent issues
 *  you can only unarchive issues from software, service management, and business projects

**[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

**License required:** Premium or Enterprise

**Signed-in users only:** This API can't be accessed anonymously.

  


### Request Body (application/json)

```json
{
  "issueIdsOrKeys": [
    string
  ],
}
```
### Responses

#### 200 - Returned if there is at least one valid issue to unarchive in the request. It will return the count of unarchived issues, which also includes the count of the subtasks unarchived, and it will show the detailed errors for those issues which are not unarchived.

Example (application/json):
```json
"{\"errors\":{\"issueIsSubtask\":{\"count\":3,\"issueIdsOrKeys\":[\"ST-1\",\"ST-2\",\"ST-3\"],\"message\":\"Issue is subtask.\"},\"issuesInArchivedProjects\":{\"count\":2,\"issueIdsOrKeys\":[\"AR-1\",\"AR-2\"],\"message\":\"Issue exists in archived project.\"},\"issuesNotFound\":{\"count\":3,\"issueIdsOrKeys\":[\"PR-1\",\"PR-2\",\"PR-3\"],\"message\":\"Issue not found.\"}},\"numberOfIssuesUpdated\":10}"
```

#### 400 - Returned if none of the issues in the request are eligible to be unarchived. Possible reasons:

 *  the issues weren't found
 *  the issues are subtasks
 *  the issues belong to archived projects

Example (application/json):
```json
"{\"errorMessages\":[\"No valid issue to archive or unarchive. Bad request.\"],\"errors\":{}}"
```

#### 401 - Returned if no issues were unarchived because the provided authentication credentials are either missing or invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"User is not logged in.\"],\"errors\":{}}"
```

#### 403 - Returned if no issues were unarchived because the user lacks the required Jira admin or site admin permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only admins can archive or unarchive issues. Access denied.\"],\"errors\":{}}"
```

#### 412 - Returned if one or more issues were successfully unarchived, but the operation was incomplete because the number of issue IDs or keys provided exceeds 1000.

Example (application/json):
```json
"{\"errorMessages\":[\"The number of issues to archive or unarchive exceeds the hard limit of 1000. Precondition failed.\"],\"errors\":{}}"
```

