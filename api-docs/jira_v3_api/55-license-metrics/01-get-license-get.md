# 01-Get license [GET]

`GET /rest/api/3/instance/license`

Returns licensing information about the Jira instance.

**[Permissions](#permissions) required:** None.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"applications\":[{\"id\":\"jira-core\",\"plan\":\"PAID\"},{\"id\":\"jira-product-discovery\",\"plan\":\"FREE\"},{\"id\":\"jira-servicedesk\",\"plan\":\"FREE\"},{\"id\":\"jira-software\",\"plan\":\"PAID\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

