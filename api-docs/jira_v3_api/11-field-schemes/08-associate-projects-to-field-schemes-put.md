# 08-Associate projects to field schemes [PUT]

`PUT /rest/api/3/config/fieldschemes/projects`

Associate projects to field association schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{}
```
### Responses

#### 200 - Returned if the association was successful.

Example (application/json):
```json
"{\"results\":[{\"projectId\":10001,\"schemeId\":10000,\"success\":true},{\"projectId\":10002,\"schemeId\":10001,\"success\":true}]}"
```

#### 204 - The request completed successfully. No additional content will be sent in the response.

Schema (application/json):
```json
any
```

#### 207 - Returned if the association was partially successful.

Example (application/json):
```json
"{\"results\":[{\"projectId\":10001,\"schemeId\":10000,\"success\":true},{\"error\":\"Project #10001 doesn't exist\",\"projectId\":10002,\"schemeId\":10001,\"success\":false}]}"
```

#### 400 - Returned if the request is invalid. If request is malformed, returns a collection of errors. If request is well-formed but contains invalid scheme or project IDs, returns failure details.

Example (application/json):
```json
"{\"results\":[{\"error\":\"Field scheme #10000 doesn't exist\",\"projectId\":10001,\"schemeId\":10000,\"success\":false},{\"error\":\"Project #10001 doesn't exist\",\"projectId\":10002,\"schemeId\":10001,\"success\":false}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
any
```

#### 403 - Returned if the user does not have the required permissions

Schema (application/json):
```json
any
```

