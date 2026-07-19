# 02-Get events [GET]

`GET /rest/api/3/events`

Returns all issue events.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"id\":1,\"name\":\"Issue Created\"},{\"id\":2,\"name\":\"Issue Updated\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to complete this request.

