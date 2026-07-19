# 09-Get issue security scheme [GET]

`GET /rest/api/3/issuesecurityschemes/{id}`

Returns an issue security scheme along with its security levels.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project that uses the requested issue security scheme.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the issue security scheme. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) operation to get a list of issue security scheme IDs. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultSecurityLevelId\":10021,\"description\":\"Description for the default issue security scheme\",\"id\":10000,\"levels\":[{\"description\":\"Only the reporter and internal staff can see this issue.\",\"id\":\"10021\",\"name\":\"Reporter Only\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/securitylevel/10021\"}],\"name\":\"Default Issue Security Scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issuesecurityschemes/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the administrator permission and the scheme is not used in any project where the user has administrative permission.

