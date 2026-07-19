# 03-Get issue types for project [GET]

`GET /rest/api/3/issuetype/project`

Returns issue types for a project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `integer` | `query` | Yes | The ID of the project. |
| `level` | `integer` | `query` | No | The level of the issue type to filter by. Use:<br><br> *  `-1` for Subtask.<br> *  `0` for Base.<br> *  `1` for Epic. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"avatarId\":10002,\"description\":\"A problem with the software.\",\"entityId\":\"9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\\\",\",\"id\":\"1\",\"name\":\"Bug\",\"scope\":{\"project\":{\"id\":\"10000\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/1\",\"subtask\":false},{\"avatarId\":1,\"description\":\"A task that needs to be done.\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\\\",\",\"id\":\"3\",\"name\":\"Task\",\"scope\":{\"project\":{\"id\":\"10000\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/3\",\"subtask\":false}]"
```

#### 400 - Returned if the request is not valid.

#### 404 - Returned if:

 *  the project is not found.
 *  the user does not have the necessary permission.

