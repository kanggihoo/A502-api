# 07-Merge versions [PUT]

`PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo}`

Merges two project versions. The merge is completed by deleting the version specified in `id` and replacing any occurrences of its ID in `fixVersion` with the version ID specified in `moveIssuesTo`.

Consider using [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) instead. This resource supports swapping version values in `fixVersion`, `affectedVersion`, and custom fields.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the version to delete. |
| `moveIssuesTo` | `string` | `path` | Yes | The ID of the version to merge into. |

### Responses

#### 204 - Returned if the version is deleted.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if:

 *  the authentication credentials are incorrect or missing.
 *  the user does not have the required permissions.

#### 404 - Returned if the version to be deleted or the version to merge to are not found.

