# 08-Get permission scheme grant [GET]

`GET /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}`

Returns a permission grant.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `schemeId` | `integer` | `path` | Yes | The ID of the permission scheme. |
| `permissionId` | `integer` | `path` | Yes | The ID of the permission grant. |
| `expand` | `string` | `query` | No | Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:<br><br> *  `all` Returns all expandable information.<br> *  `field` Returns information about the custom field granted the permission.<br> *  `group` Returns information about the group that is granted the permission.<br> *  `permissions` Returns all permission grants for each permission scheme.<br> *  `projectRole` Returns information about the project role granted the permission.<br> *  `user` Returns information about the user who is granted the permission. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"holder\":{\"expand\":\"group\",\"parameter\":\"jira-core-users\",\"type\":\"group\",\"value\":\"ca85fac0-d974-40ca-a615-7af99c48d24f\"},\"id\":10000,\"permission\":\"ADMINISTER_PROJECTS\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/permissionscheme/permission/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the permission scheme or permission grant is not found or the user does not have the necessary permission.

