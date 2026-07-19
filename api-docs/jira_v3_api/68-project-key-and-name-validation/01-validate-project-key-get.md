# 01-Validate project key [GET]

`GET /rest/api/3/projectvalidate/key`

Validates a project key by confirming the key is a valid string and not in use.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `query` | No | The project key. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"errorMessages\":[],\"errors\":{\"projectKey\":\"A project with that project key already exists.\"}}"
```

#### 401 - Returned if the authentication credentials are incorrect.

