# 07-Set issue property [PUT]

`PUT /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}`

Sets the value of an issue's property. Use this resource to store custom data against an issue.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `propertyKey` | `string` | `path` | Yes | The key of the issue property. The maximum length is 255 characters. |

### Request Body (application/json)

```json
any
```
### Responses

#### 200 - Returned if the issue property is updated.

Schema (application/json):
```json
any
```

#### 201 - Returned if the issue property is created.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to edit the issue.

#### 404 - Returned if the issue is not found or the user does not have permission to view the issue.

