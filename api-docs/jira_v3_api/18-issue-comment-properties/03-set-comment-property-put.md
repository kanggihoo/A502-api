# 03-Set comment property [PUT]

`PUT /rest/api/3/comment/{commentId}/properties/{propertyKey}`

Creates or updates the value of a property for a comment. Use this resource to store custom data against a comment.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

**[Permissions](#permissions) required:** either of:

 *  *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on any comment.
 *  *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to create or update the value of a property on a comment created by the user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `commentId` | `string` | `path` | Yes | The ID of the comment. |
| `propertyKey` | `string` | `path` | Yes | The key of the property. The maximum length is 255 characters. |

### Request Body (application/json)

```json
any
```
### Responses

#### 200 - Returned if the comment property is updated.

Schema (application/json):
```json
any
```

#### 201 - Returned if the comment property is created.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the comment is not found.

