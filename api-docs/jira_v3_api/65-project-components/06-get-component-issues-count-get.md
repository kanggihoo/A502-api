# 06-Get component issues count [GET]

`GET /rest/api/3/component/{id}/relatedIssueCounts`

Returns the counts of issues assigned to the component.

This operation can be accessed anonymously.

**Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

 *  **Classic**: `read:jira-work`
 *  **Granular**: `read:field:jira`, `read:project.component:jira`

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the component. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueCount\":23,\"self\":\"https://your-domain.atlassian.net/rest/api/3/component/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the component is not found.

