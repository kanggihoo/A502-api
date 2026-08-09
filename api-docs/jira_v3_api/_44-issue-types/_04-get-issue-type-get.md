# 04-Get issue type [GET]

`GET /rest/api/3/issuetype/{id}`

Returns an issue type.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue type. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"avatarId\":1,\"description\":\"A task that needs to be done.\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\\\",\",\"id\":\"3\",\"name\":\"Task\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/3\",\"subtask\":false}"
```

#### 400 - Returned if the issue type ID is invalid.

#### 404 - Returned if:

 *  the issue type is not found.
 *  the user does not have the required permissions.

