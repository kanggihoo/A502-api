# 02-Get worklog property [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}`

Returns the value of a worklog property.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `worklogId` | `string` | `path` | Yes | The ID of the worklog. |
| `propertyKey` | `string` | `path` | Yes | The key of the property. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"key\":\"issue.support\",\"value\":{\"system.conversation.id\":\"b1bf38be-5e94-4b40-a3b8-9278735ee1e6\",\"system.support.time\":\"1m\"}}"
```

#### 400 - Returned if the worklog ID is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the issue, worklog, or property is not found.
 *  the user does not have permission to view the issue or worklog.

