# 01-Get worklog property keys [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties`

Returns the keys of all properties for a worklog.

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

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"keys\":[{\"key\":\"issue.support\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/EX-2/properties/issue.support\"}]}"
```

#### 400 - Returned if the worklog ID is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the issue or worklog is not found.
 *  the user does not have permission to view the issue or worklog.

