# 03-Get valid project name [GET]

`GET /rest/api/3/projectvalidate/validProjectName`

Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404 response is returned.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `query` | Yes | The project name. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"\"Valid Project Name Example\""
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect.

#### 404 - Returned if a valid project name cannot be generated.

