# 01-Get system avatars by type [GET]

`GET /rest/api/3/avatar/{type}/system`

Returns a list of system avatar details by owner type, where the owner types are issue type, project, user or priority.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | `string` | `path` | Yes | The avatar type. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"system\":[{\"id\":\"1000\",\"isDeletable\":false,\"isSelected\":false,\"isSystemAvatar\":true,\"urls\":{\"16x16\":\"/secure/useravatar?size=xsmall&avatarId=10040&avatarType=project\",\"24x24\":\"/secure/useravatar?size=small&avatarId=10040&avatarType=project\",\"32x32\":\"/secure/useravatar?size=medium&avatarId=10040&avatarType=project\",\"48x48\":\"/secure/useravatar?avatarId=10040&avatarType=project\"}}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 500 - Returned if an error occurs while retrieving the list of avatars.

