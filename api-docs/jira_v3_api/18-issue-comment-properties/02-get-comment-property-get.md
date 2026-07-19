# 02-Get comment property [GET]

`GET /rest/api/3/comment/{commentId}/properties/{propertyKey}`

Returns the value of a comment property.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `commentId` | `string` | `path` | Yes | The ID of the comment. |
| `propertyKey` | `string` | `path` | Yes | The key of the property. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"key\":\"issue.support\",\"value\":{\"system.conversation.id\":\"b1bf38be-5e94-4b40-a3b8-9278735ee1e6\",\"system.support.time\":\"1m\"}}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the comment or the property is not found.

