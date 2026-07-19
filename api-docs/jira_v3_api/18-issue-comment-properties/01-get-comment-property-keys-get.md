# 01-Get comment property keys [GET]

`GET /rest/api/3/comment/{commentId}/properties`

Returns the keys of all the properties of a comment.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `commentId` | `string` | `path` | Yes | The ID of the comment. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"keys\":[{\"key\":\"issue.support\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support\"}]}"
```

#### 400 - Returned if the comment ID is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the comment is not found.

