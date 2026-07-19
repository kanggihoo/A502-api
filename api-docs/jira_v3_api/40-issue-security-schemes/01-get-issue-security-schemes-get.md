# 01-Get issue security schemes [GET]

`GET /rest/api/3/issuesecurityschemes`

Returns all [issue security schemes](https://confluence.atlassian.com/x/J4lKLg).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueSecuritySchemes\":[{\"defaultSecurityLevelId\":10021,\"description\":\"Description for the default issue security scheme\",\"id\":10000,\"name\":\"Default Issue Security Scheme\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issuesecurityschemes/10000\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect.

#### 403 - Returned if the user does not have permission to administer issue security schemes.

