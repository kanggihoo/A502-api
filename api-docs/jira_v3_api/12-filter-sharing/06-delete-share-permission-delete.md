# 06-Delete share permission [DELETE]

`DELETE /rest/api/3/filter/{id}/permission/{permissionId}`

Deletes a share permission from a filter.

**[Permissions](#permissions) required:** Permission to access Jira and the user must own the filter.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the filter. |
| `permissionId` | `integer` | `path` | Yes | The ID of the share permission. |

### Responses

#### 204 - Returned if the request is successful.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the filter is not found.
 *  the user does not own the filter.

