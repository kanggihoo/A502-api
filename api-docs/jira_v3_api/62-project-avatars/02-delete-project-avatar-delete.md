# 02-Delete project avatar [DELETE]

`DELETE /rest/api/3/project/{projectIdOrKey}/avatar/{id}`

Deletes a custom avatar from a project. Note that system avatars cannot be deleted.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or (case-sensitive) key. |
| `id` | `integer` | `path` | Yes | The ID of the avatar. |

### Responses

#### 204 - Returned if the request is successful.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the avatar is a system avatar or the user does not have permission to administer the project.

#### 404 - Returned if the project or avatar is not found or the user does not have permission to view the project.

