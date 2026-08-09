# 14-Get version's unresolved issues count [GET]

`GET /rest/api/3/version/{id}/unresolvedIssueCount`

Returns counts of the issues and unresolved issues for the project version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the version. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issuesCount\":30,\"issuesUnresolvedCount\":23,\"self\":\"https://your-domain.atlassian.net/rest/api/3/version/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the version is not found.
 *  the user does not have the required permissions.

