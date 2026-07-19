# 10-Get related work [GET]

`GET /rest/api/3/version/{id}/relatedwork`

Returns related work items for the given version id.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the version. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"category\":\"Design\",\"issueId\":10001,\"relatedWorkId\":\"fabcdef6-7878-1234-beaf-43211234abcd\",\"title\":\"Design link\",\"url\":\"https://www.atlassian.com\"},{\"category\":\"Communications\",\"relatedWorkId\":\"fabcdef6-7878-1234-beaf-43211234abce\",\"title\":\"Chat application\",\"url\":\"https://www.atlassian.com\"},{\"category\":\"External Link\",\"issueId\":10003,\"relatedWorkId\":\"fabcdef6-7878-1234-beaf-43211234abcf\",\"url\":\"https://www.atlassian.com\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the version is not found or the user does not have the necessary permission.

#### 500 - Returned if reading related work fails

