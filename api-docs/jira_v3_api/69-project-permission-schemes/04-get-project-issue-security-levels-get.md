# 04-Get project issue security levels [GET]

`GET /rest/api/3/project/{projectKeyOrId}/securitylevel`

Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that the user has access to.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security levels are only returned for authenticated user with *Set Issue Security* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectKeyOrId` | `string` | `path` | Yes | The project ID or project key (case sensitive). |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"levels\":[{\"description\":\"Only the reporter and internal staff can see this issue.\",\"id\":\"100000\",\"name\":\"Reporter Only\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/securitylevel/100000\"},{\"description\":\"Only internal staff can see this issue.\",\"id\":\"100001\",\"name\":\"Staff Only\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/securitylevel/100001\"}]}"
```

#### 404 - Returned if the project is not found or the user does not have permission to view it.

