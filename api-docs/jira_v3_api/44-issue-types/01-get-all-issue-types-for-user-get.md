# 01-Get all issue types for user [GET]

`GET /rest/api/3/issuetype`

Returns all issue types.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Issue types are only returned as follows:

 *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.
 *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types associated with the projects the user has permission to browse are returned.
 *  if the user is anonymous then they will be able to access projects with the *Browse projects* for anonymous users
 *  if the user authentication is incorrect they will fall back to anonymous

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"avatarId\":1,\"description\":\"A task that needs to be done.\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\\\",\",\"id\":\"3\",\"name\":\"Task\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/3\",\"subtask\":false},{\"avatarId\":10002,\"description\":\"A problem with the software.\",\"entityId\":\"9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\\\",\",\"id\":\"1\",\"name\":\"Bug\",\"scope\":{\"project\":{\"id\":\"10000\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/1\",\"subtask\":false}]"
```

