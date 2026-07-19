# 01-Get all application roles [GET]

`GET /rest/api/3/applicationrole`

Returns all application roles. In Jira, application roles are managed using the [Application access configuration](https://confluence.atlassian.com/x/3YxjL) page.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"defaultGroups\":[\"jira-software-users\"],\"defaultGroupsDetails\":[{\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"jira-software-users\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625\"}],\"defined\":false,\"groupDetails\":[{\"groupId\":\"42c8955c-63d7-42c8-9520-63d7aca0625\",\"name\":\"jira-testers\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=42c8955c-63d7-42c8-9520-63d7aca0625\"},{\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"jira-software-users\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625\"}],\"groups\":[\"jira-software-users\",\"jira-testers\"],\"hasUnlimitedSeats\":false,\"key\":\"jira-software\",\"name\":\"Jira Software\",\"numberOfSeats\":10,\"platform\":false,\"remainingSeats\":5,\"selectedByDefault\":false,\"userCount\":5,\"userCountDescription\":\"5 developers\"},{\"defaultGroups\":[\"jira-core-users\"],\"defaultGroupsDetails\":[{\"groupId\":\"92d01dca0625-42c8-42c8-9520-276f955c\",\"name\":\"jira-core-users\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=92d01dca0625-42c8-42c8-9520-276f955c\"}],\"defined\":false,\"groupDetails\":[{\"groupId\":\"92d01dca0625-42c8-42c8-9520-276f955c\",\"name\":\"jira-core-users\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=92d01dca0625-42c8-42c8-9520-276f955c\"}],\"groups\":[\"jira-core-users\"],\"hasUnlimitedSeats\":false,\"key\":\"jira-core\",\"name\":\"Jira Core\",\"numberOfSeats\":1,\"platform\":true,\"remainingSeats\":1,\"selectedByDefault\":false,\"userCount\":0,\"userCountDescription\":\"0 users\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user is not an administrator.

