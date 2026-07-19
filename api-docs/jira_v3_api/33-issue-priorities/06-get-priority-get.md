# 06-Get priority [GET]

`GET /rest/api/3/priority/{id}`

Returns an issue priority. To fetch multiple priorities at once, use [Search priorities](#api-rest-api-3-priority-search-get) instead.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue priority. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"Major loss of function.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/priorities/major.png\",\"id\":\"1\",\"name\":\"Major\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/priority/3\",\"statusColor\":\"#009900\"}"
```

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if the issue priority isn't found.

