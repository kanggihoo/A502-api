# 04-Get all project avatars [GET]

`GET /rest/api/3/project/{projectIdOrKey}/avatars`

Returns all project avatars, grouped by system and custom avatars.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The ID or (case-sensitive) key of the project. |

### Responses

#### 200 - Returned if request is successful.

Example (application/json):
```json
"{\"custom\":[{\"id\":\"1010\",\"isDeletable\":true,\"isSelected\":false,\"isSystemAvatar\":false,\"urls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10080&avatarType=project\",\"24x24\":\"https://your-domain.atlassian.net/secure/viewavatar?size=small&avatarId=10080&avatarType=project\",\"32x32\":\"https://your-domain.atlassian.net/secure/viewavatar?size=medium&avatarId=10080&avatarType=project\",\"48x48\":\"https://your-domain.atlassian.net/secure/viewavatar?avatarId=10080&avatarType=project\"}}],\"system\":[{\"id\":\"1000\",\"isDeletable\":false,\"isSelected\":false,\"isSystemAvatar\":true,\"urls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10040&avatarType=project\",\"24x24\":\"https://your-domain.atlassian.net/secure/viewavatar?size=small&avatarId=10040&avatarType=project\",\"32x32\":\"https://your-domain.atlassian.net/secure/viewavatar?size=medium&avatarId=10040&avatarType=project\",\"48x48\":\"https://your-domain.atlassian.net/secure/viewavatar?avatarId=10040&avatarType=project\"}}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the project is not found or the user does not have permission to view the project.

