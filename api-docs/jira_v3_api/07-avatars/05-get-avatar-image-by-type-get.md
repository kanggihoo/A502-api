# 05-Get avatar image by type [GET]

`GET /rest/api/3/universal_avatar/view/type/{type}`

Returns the default project, issue type or priority avatar image.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | `string` | `path` | Yes | The icon type of the avatar. |
| `size` | `string` | `query` | No | The size of the avatar image. If not provided the default size is returned. |
| `format` | `string` | `query` | No | The format to return the avatar image in. If not provided the original content format is returned. |

### Responses

#### 200 - Returned if the request is successful.

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

