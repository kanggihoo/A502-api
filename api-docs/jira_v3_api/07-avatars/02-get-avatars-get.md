# 02-Get avatars [GET]

`GET /rest/api/3/universal_avatar/type/{type}/owner/{entityId}`

Returns the system and custom avatars for a project, issue type or priority.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  for custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
 *  for custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
 *  for system avatars, none.
 *  for priority avatars, none.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | `string` | `path` | Yes | The avatar type. |
| `entityId` | `string` | `path` | Yes | The ID of the item the avatar is associated with. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"custom\":[{\"id\":\"1010\",\"isDeletable\":true,\"isSelected\":false,\"isSystemAvatar\":false,\"urls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10080&avatarType=project\",\"24x24\":\"https://your-domain.atlassian.net/secure/viewavatar?size=small&avatarId=10080&avatarType=project\",\"32x32\":\"https://your-domain.atlassian.net/secure/viewavatar?size=medium&avatarId=10080&avatarType=project\",\"48x48\":\"https://your-domain.atlassian.net/secure/viewavatar?avatarId=10080&avatarType=project\"}}],\"system\":[{\"id\":\"1000\",\"isDeletable\":false,\"isSelected\":false,\"isSystemAvatar\":true,\"urls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10040&avatarType=project\",\"24x24\":\"https://your-domain.atlassian.net/secure/viewavatar?size=small&avatarId=10040&avatarType=project\",\"32x32\":\"https://your-domain.atlassian.net/secure/viewavatar?size=medium&avatarId=10040&avatarType=project\",\"48x48\":\"https://your-domain.atlassian.net/secure/viewavatar?avatarId=10040&avatarType=project\"}}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the avatar type is invalid, the associated item ID is missing, or the item is not found.

