# 13-Delete and replace version [POST]

`POST /rest/api/3/version/{id}/removeAndSwap`

Deletes a project version.

Alternative versions can be provided to update issues that use the deleted version in `fixVersion`, `affectedVersion`, or any version picker custom fields. If alternatives are not provided, occurrences of `fixVersion`, `affectedVersion`, and any version picker custom field, that contain the deleted version, are cleared. Any replacement version must be in the same project as the version being deleted and cannot be the version being deleted.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the version. |

### Request Body (application/json)

```json
{
  "customFieldReplacementList": [
    {
      "customFieldId": integer, // The ID of the custom field in which to replace the version number.
      "moveTo": integer, // The version number to use as a replacement for the deleted version.
    }
  ], // An array of custom field IDs (`customFieldId`) and version IDs (`moveTo`) to update when the fields contain the deleted version.
  "moveAffectedIssuesTo": integer, // The ID of the version to update `affectedVersion` to when the field contains the deleted version.
  "moveFixIssuesTo": integer, // The ID of the version to update `fixVersion` to when the field contains the deleted version.
}
```
### Responses

#### 204 - Returned if the version is deleted.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the version to delete is not found.
 *  the user does not have the required permissions.

