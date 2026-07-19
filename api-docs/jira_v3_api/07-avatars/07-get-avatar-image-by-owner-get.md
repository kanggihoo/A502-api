# 07-Get avatar image by owner [GET]

`GET /rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}`

Returns the avatar image for a project, issue type or priority.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  For system avatars, none.
 *  For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
 *  For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
 *  For priority avatars, none.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | `string` | `path` | Yes | The icon type of the avatar. |
| `entityId` | `string` | `path` | Yes | The ID of the project or issue type the avatar belongs to. |
| `size` | `string` | `query` | No | The size of the avatar image. If not provided the default size is returned. |
| `format` | `string` | `query` | No | The format to return the avatar image in. If not provided the original content format is returned. |

### Responses

#### 200 - Returned if the request is successful.

#### 400 - Returned if the request is not valid.

Example (*/*):
```json
"{\"errorMessages\":[\"Human readable error message\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect.

Example (*/*):
```json
"{\"errorMessages\":[\"Human readable error message\"],\"errors\":{}}"
```

#### 403 - Returned if the user does not have the necessary permission.

Example (*/*):
```json
"{\"errorMessages\":[\"Human readable error message\"],\"errors\":{}}"
```

#### 404 - Returned if an avatar is not found or an avatar matching the requested size is not found.

Example (*/*):
```json
"{\"errorMessages\":[\"Human readable error message\"],\"errors\":{}}"
```

