# 07-Get alternative issue types [GET]

`GET /rest/api/3/issuetype/{id}/alternatives`

Returns a list of issue types that can be used to replace the issue type. The alternative issue types are those assigned to the same workflow scheme, field configuration scheme, and screen scheme.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue type. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"avatarId\":1,\"description\":\"A task that needs to be done.\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\\\",\",\"id\":\"3\",\"name\":\"Task\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/3\",\"subtask\":false},{\"avatarId\":10002,\"description\":\"A problem with the software.\",\"entityId\":\"9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\\\",\",\"id\":\"1\",\"name\":\"Bug\",\"scope\":{\"project\":{\"id\":\"10000\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/1\",\"subtask\":false}]"
```

#### 404 - Returned if:

 *  the issue type is not found.
 *  the user does not have the required permissions.

