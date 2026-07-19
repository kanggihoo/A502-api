# 07-Create permission grant [POST]

`POST /rest/api/3/permissionscheme/{schemeId}/permission`

Creates a permission grant in a permission scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `schemeId` | `integer` | `path` | Yes | The ID of the permission scheme in which to create a new permission grant. |
| `expand` | `string` | `query` | No | Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:<br><br> *  `permissions` Returns all permission grants for each permission scheme.<br> *  `user` Returns information about the user who is granted the permission.<br> *  `group` Returns information about the group that is granted the permission.<br> *  `projectRole` Returns information about the project role granted the permission.<br> *  `field` Returns information about the custom field granted the permission.<br> *  `all` Returns all expandable information. |

### Request Body (application/json)

```json
{
  "holder": any, // The user or group being granted the permission. It consists of a `type`, a type-dependent `parameter` and a type-dependent `value`. See [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information.
  "id": integer, // The ID of the permission granted details.
  "permission": string, // The permission to grant. This permission can be one of the built-in permissions or a custom permission added by an app. See [Built-in permissions](../api-group-permission-schemes/#built-in-permissions) in *Get all permission schemes* for more information about the built-in permissions. See the [project permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/) module documentation for more information about custom permissions.
  "self": string, // The URL of the permission granted details.
}
```
### Responses

#### 201 - Returned if the scheme permission is created.

Example (application/json):
```json
"{\"holder\":{\"expand\":\"group\",\"parameter\":\"jira-core-users\",\"type\":\"group\",\"value\":\"ca85fac0-d974-40ca-a615-7af99c48d24f\"},\"id\":10000,\"permission\":\"ADMINISTER_PROJECTS\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000\"}"
```

#### 400 - Returned if the value for expand is invalid or the same permission grant is present.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

