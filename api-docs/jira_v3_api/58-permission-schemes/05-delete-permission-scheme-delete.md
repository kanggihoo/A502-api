# 05-Delete permission scheme [DELETE]

`DELETE /rest/api/3/permissionscheme/{schemeId}`

Deletes a permission scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `schemeId` | `integer` | `path` | Yes | The ID of the permission scheme being deleted. |

### Responses

#### 204 - Returned if the permission scheme is deleted.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the permission scheme is not found.

