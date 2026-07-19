# 02-Get application role [GET]

`GET /rest/api/3/applicationrole/{key}`

Returns an application role.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `path` | Yes | The key of the application role. Use the [Get all application roles](#api-rest-api-3-applicationrole-get) operation to get the key for each application role. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultGroups\":[\"jira-software-users\"],\"defaultGroupsDetails\":[{\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"jira-software-users\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625\"}],\"defined\":false,\"groupDetails\":[{\"groupId\":\"42c8955c-63d7-42c8-9520-63d7aca0625\",\"name\":\"jira-testers\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=42c8955c-63d7-42c8-9520-63d7aca0625\"},{\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"jira-software-users\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625\"}],\"groups\":[\"jira-software-users\",\"jira-testers\"],\"hasUnlimitedSeats\":false,\"key\":\"jira-software\",\"name\":\"Jira Software\",\"numberOfSeats\":10,\"platform\":false,\"remainingSeats\":5,\"selectedByDefault\":false,\"userCount\":5,\"userCountDescription\":\"5 developers\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user is not an administrator.

#### 404 - Returned if the role is not found.

