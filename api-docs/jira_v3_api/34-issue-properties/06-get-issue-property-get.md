# 06-Get issue property [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}`

Returns the key and value of an issue's property.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The key or ID of the issue. |
| `propertyKey` | `string` | `path` | Yes | The key of the property. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"key\":\"issue.support\",\"value\":{\"system.conversation.id\":\"b1bf38be-5e94-4b40-a3b8-9278735ee1e6\",\"system.support.time\":\"1m\"}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the issue or property is not found or the user does not have permission to see the issue.

