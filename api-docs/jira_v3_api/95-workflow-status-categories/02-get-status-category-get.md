# 02-Get status category [GET]

`GET /rest/api/3/statuscategory/{idOrKey}`

Returns a status category. Status categories provided a mechanism for categorizing [statuses](#api-rest-api-3-status-idOrName-get).

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `idOrKey` | `string` | `path` | Yes | The ID or key of the status category. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"colorName\":\"yellow\",\"id\":1,\"key\":\"in-flight\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/1\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the status category is not found.

