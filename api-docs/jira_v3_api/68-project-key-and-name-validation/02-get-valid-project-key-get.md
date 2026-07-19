# 02-Get valid project key [GET]

`GET /rest/api/3/projectvalidate/validProjectKey`

Validates a project key and, if the key is invalid or in use, generates a valid random string for the project key.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `query` | No | The project key. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"\"VPNE\""
```

#### 401 - Returned if the authentication credentials are incorrect.

