# 01-Get project issue security scheme [GET]

`GET /rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme`

Returns the [issue security scheme](https://confluence.atlassian.com/x/J4lKLg) associated with the project.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or the *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectKeyOrId` | `string` | `path` | Yes | The project ID or project key (case sensitive). |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultSecurityLevelId\":10021,\"description\":\"Description for the default issue security scheme\",\"id\":10000,\"levels\":[{\"description\":\"Only the reporter and internal staff can see this issue.\",\"id\":\"10021\",\"name\":\"Reporter Only\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/securitylevel/10021\"}],\"name\":\"Default Issue Security Scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issuesecurityschemes/10000\"}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the project is visible to the user but the user doesn't have administrative permissions.

#### 404 - Returned if the project is not found or the user does not have permission to view it.

