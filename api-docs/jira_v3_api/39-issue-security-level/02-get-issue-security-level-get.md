# 02-Get issue security level [GET]

`GET /rest/api/3/securitylevel/{id}`

Returns details of an issue security level.

Use [Get issue security scheme](#api-rest-api-3-issuesecurityschemes-id-get) to obtain the IDs of issue security levels associated with the issue security scheme.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the issue security level. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"description\":\"Only the reporter and internal staff can see this issue.\",\"id\":\"10021\",\"name\":\"Reporter Only\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/securitylevel/10021\"}"
```

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if the issue security level is not found.

