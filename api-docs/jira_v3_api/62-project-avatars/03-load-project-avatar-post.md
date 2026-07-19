# 03-Load project avatar [POST]

`POST /rest/api/3/project/{projectIdOrKey}/avatar2`

Loads an avatar for a project.

Specify the avatar's local file location in the body of the request. Also, include the following headers:

 *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).
 *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

For example:  
`curl --request POST `

`--user email@example.com:<api_token> `

`--header 'X-Atlassian-Token: no-check' `

`--header 'Content-Type: image/< image_type>' `

`--data-binary "<@/path/to/file/with/your/avatar>" `

`--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'`

The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-put) to set it as the project's displayed avatar.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The ID or (case-sensitive) key of the project. |
| `x` | `integer` | `query` | No | The X coordinate of the top-left corner of the crop region. |
| `y` | `integer` | `query` | No | The Y coordinate of the top-left corner of the crop region. |
| `size` | `integer` | `query` | No | The length of each side of the crop region. |

### Request Body (*/*)

```json
any
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"1010\",\"isDeletable\":true,\"isSelected\":false,\"isSystemAvatar\":false}"
```

#### 400 - Returned if:

 *  an image isn't included in the request.
 *  the image type is unsupported.
 *  the crop parameters extend the crop area beyond the edge of the image.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to administer the project or an anonymous call is made to the operation.

#### 404 - Returned if the project is not found or the user does not have permission to view the project.

