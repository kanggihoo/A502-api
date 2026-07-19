# 04-Delete comment property [DELETE]

`DELETE /rest/api/3/comment/{commentId}/properties/{propertyKey}`

Deletes a comment property.

**[Permissions](#permissions) required:** either of:

 *  *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from any comment.
 *  *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a property from a comment created by the user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `commentId` | `string` | `path` | Yes | The ID of the comment. |
| `propertyKey` | `string` | `path` | Yes | The key of the property. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the comment or the property is not found.

