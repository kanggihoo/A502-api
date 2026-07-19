# 04-Update permission scheme [PUT]

`PUT /rest/api/3/permissionscheme/{schemeId}`

Updates a permission scheme. Below are some important things to note when using this resource:

 *  If a permissions list is present in the request, then it is set in the permission scheme, overwriting *all existing* grants.
 *  If you want to update only the name and description, then do not send a permissions list in the request.
 *  Sending an empty list will remove all permission grants from the permission scheme.

If you want to add or delete a permission grant instead of updating the whole list, see [Create permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete).

See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `schemeId` | `integer` | `path` | Yes | The ID of the permission scheme to update. |
| `expand` | `string` | `query` | No | Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:<br><br> *  `all` Returns all expandable information.<br> *  `field` Returns information about the custom field granted the permission.<br> *  `group` Returns information about the group that is granted the permission.<br> *  `permissions` Returns all permission grants for each permission scheme.<br> *  `projectRole` Returns information about the project role granted the permission.<br> *  `user` Returns information about the user who is granted the permission. |

### Request Body (application/json)

```json
{
  "description": string, // A description for the permission scheme.
  "expand": string, // The expand options available for the permission scheme.
  "id": integer, // The ID of the permission scheme.
  "name": string (required), // The name of the permission scheme. Must be unique.
  "permissions": [
    {
      "holder": any, // The user or group being granted the permission. It consists of a `type`, a type-dependent `parameter` and a type-dependent `value`. See [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more information.
      "id": integer, // The ID of the permission granted details.
      "permission": string, // The permission to grant. This permission can be one of the built-in permissions or a custom permission added by an app. See [Built-in permissions](../api-group-permission-schemes/#built-in-permissions) in *Get all permission schemes* for more information about the built-in permissions. See the [project permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/) module documentation for more information about custom permissions.
      "self": string, // The URL of the permission granted details.
    }
  ], // The permission scheme to create or update. See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more information.
  "scope": any, // The scope of the permission scheme.
  "self": string, // The URL of the permission scheme.
}
```
### Responses

#### 200 - Returned if the scheme is updated.

Example (application/json):
```json
"{\"description\":\"description\",\"id\":10000,\"name\":\"Example permission scheme\",\"permissions\":[{\"holder\":{\"expand\":\"group\",\"parameter\":\"jira-core-users\",\"type\":\"group\",\"value\":\"ca85fac0-d974-40ca-a615-7af99c48d24f\"},\"id\":10000,\"permission\":\"ADMINISTER_PROJECTS\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000\"}],\"self\":\"https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if:

 *  the user does not have the necessary permission to update permission schemes.
 *  the Jira instance is Jira Core Free or Jira Software Free. Permission schemes cannot be updated on free plans.

#### 404 - Returned if the permission scheme is not found.

