# 15-Delete related work [DELETE]

`DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}`

Deletes the given related work for the given version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Resolve issues:* and *Edit issues* [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `versionId` | `string` | `path` | Yes | The ID of the version that the target related work belongs to. |
| `relatedWorkId` | `string` | `path` | Yes | The ID of the related work to delete. |

### Responses

#### 204 - Returned if the related work is deleted.

#### 400 - Returned if the request is invalid.

#### 401 - Returned if

the authentication credentials are incorrect.

#### 403 - Returned if the user does not have the required permissions.

#### 404 - Returned if the version/related work is not found.

