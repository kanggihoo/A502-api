# 04-Delete avatar [DELETE]

`DELETE /rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}`

Deletes an avatar from a project, issue type or priority.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | `string` | `path` | Yes | The avatar type. |
| `owningObjectId` | `string` | `path` | Yes | The ID of the item the avatar is associated with. |
| `id` | `integer` | `path` | Yes | The ID of the avatar. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if the request is invalid.

#### 403 - Returned if the user does not have permission to delete the avatar, the avatar is not deletable.

#### 404 - Returned if the avatar type, associated item ID, or avatar ID is invalid.

