# 02-Set default share scope [PUT]

`PUT /rest/api/3/filter/defaultShareScope`

Sets the default sharing for new filters and dashboards for a user.

**[Permissions](#permissions) required:** Permission to access Jira.

### Request Body (application/json)

```json
{
  "scope": enum("GLOBAL" | "AUTHENTICATED" | "PRIVATE") (required), // The scope of the default sharing for new filters and dashboards:   *  `AUTHENTICATED` Shared with all logged-in users.  *  `GLOBAL` Shared with all logged-in users. This shows as `AUTHENTICATED` in the response.  *  `PRIVATE` Not shared with any users.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"scope\":\"GLOBAL\"}"
```

#### 400 - Returned if an invalid scope is set.

#### 401 - Returned if the authentication credentials are incorrect or missing.

