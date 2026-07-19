# 06-Get resolution [GET]

`GET /rest/api/3/resolution/{id}`

Returns an issue resolution value.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue resolution value. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"A fix for this issue is checked into the tree and tested.\",\"id\":\"10000\",\"name\":\"Fixed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/resolution/1\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the issue resolution value is not found.

