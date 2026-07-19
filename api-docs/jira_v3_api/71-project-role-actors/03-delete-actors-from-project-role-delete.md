# 03-Delete actors from project role [DELETE]

`DELETE /rest/api/3/project/{projectIdOrKey}/role/{id}`

Deletes actors from a project role for the project.

To remove default actors from the project role, use [Delete default actors from project role](#api-rest-api-3-role-id-actors-delete).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `id` | `integer` | `path` | Yes | The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs. |
| `user` | `string` | `query` | No | The user account ID of the user to remove from the project role. |
| `group` | `string` | `query` | No | The name of the group to remove from the project role. This parameter cannot be used with the `groupId` parameter. As a group's name can change, use of `groupId` is recommended. |
| `groupId` | `string` | `query` | No | The ID of the group to remove from the project role. This parameter cannot be used with the `group` parameter. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if the request is not valid.

#### 404 - Returned if:

 *  the project or project role is not found.
 *  the calling user does not have administrative permission.

