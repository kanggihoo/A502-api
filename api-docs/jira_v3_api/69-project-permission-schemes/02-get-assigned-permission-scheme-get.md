# 02-Get assigned permission scheme [GET]

`GET /rest/api/3/project/{projectKeyOrId}/permissionscheme`

Gets the [permission scheme](https://confluence.atlassian.com/x/yodKLg) associated with the project.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectKeyOrId` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:<br><br> *  `all` Returns all expandable information.<br> *  `field` Returns information about the custom field granted the permission.<br> *  `group` Returns information about the group that is granted the permission.<br> *  `permissions` Returns all permission grants for each permission scheme.<br> *  `projectRole` Returns information about the project role granted the permission.<br> *  `user` Returns information about the user who is granted the permission. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"description\",\"id\":10000,\"name\":\"Example permission scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/permissionscheme/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to view the project's configuration.

#### 404 - Returned if the project is not found or the user does not have permission to view the project.

