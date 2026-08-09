# 06-Delete remote issue link by ID [DELETE]

`DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`

Deletes a remote issue link from an issue.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects*, *Edit issues*, and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `linkId` | `string` | `path` | Yes | The ID of a remote issue link. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if the link ID is invalid or the remote issue link does not belong to the issue.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to link issues.

#### 404 - Returned if the issue or remote issue link is not found or the user does not have permission to view the issue.

