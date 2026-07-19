# 05-Get share permission [GET]

`GET /rest/api/3/filter/{id}/permission/{permissionId}`

Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None, however, a share permission is only returned for:

 *  filters owned by the user.
 *  filters shared with a group that the user is a member of.
 *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  filters shared with a public project.
 *  filters shared with the public.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the filter. |
| `permissionId` | `integer` | `path` | Yes | The ID of the share permission. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":10000,\"type\":\"global\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the filter is not found.
 *  the permission is not found.
 *  the user does not have permission to view the filter.

