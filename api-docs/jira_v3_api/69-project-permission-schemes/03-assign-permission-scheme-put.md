# 03-Assign permission scheme [PUT]

`PUT /rest/api/3/project/{projectKeyOrId}/permissionscheme`

Assigns a permission scheme with a project. See [Managing project permissions](https://confluence.atlassian.com/x/yodKLg) for more information about permission schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectKeyOrId` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:<br><br> *  `all` Returns all expandable information.<br> *  `field` Returns information about the custom field granted the permission.<br> *  `group` Returns information about the group that is granted the permission.<br> *  `permissions` Returns all permission grants for each permission scheme.<br> *  `projectRole` Returns information about the project role granted the permission.<br> *  `user` Returns information about the user who is granted the permission. |

### Request Body (application/json)

```json
{
  "id": integer (required), // The ID of the permission scheme to associate with the project. Use the [Get all permission schemes](#api-rest-api-3-permissionscheme-get) resource to get a list of permission scheme IDs.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"description\",\"id\":10000,\"name\":\"Example permission scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if:

 *  the user does not have the necessary permission to edit the project's configuration.
 *  the Jira instance is Jira Core Free or Jira Software Free. Permission schemes cannot be assigned to projects on free plans.

#### 404 - Returned if the project or permission scheme is not found.

