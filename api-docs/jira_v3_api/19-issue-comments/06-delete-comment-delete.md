# 06-Delete comment [DELETE]

`DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id}`

Deletes a comment.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Delete all comments*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any comment or *Delete own comments* to delete comment created by the user,
 *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `id` | `string` | `path` | Yes | The ID of the comment. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if the user does not have permission to delete the comment.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the issue or comment is not found or the user does not have permission to view the issue or comment.

#### 405 - Returned if an anonymous call is made to the operation.

