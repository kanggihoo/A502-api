# 05-Get account IDs for users [GET]

`GET /rest/api/3/user/bulk/migration`

Returns the account IDs for the users specified in the `key` or `username` parameters. Note that multiple `key` or `username` parameters can be specified.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `username` | `array` | `query` | No | Username of a user. To specify multiple users, pass multiple copies of this parameter. For example, `username=fred&username=barney`. Required if `key` isn't provided. Cannot be provided if `key` is present. |
| `key` | `array` | `query` | No | Key of a user. To specify multiple users, pass multiple copies of this parameter. For example, `key=fred&key=barney`. Required if `username` isn't provided. Cannot be provided if `username` is present. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"username\":\"mia\",\"accountId\":\"5b10a2844c20165700ede21g\"},{\"username\":\"emma\",\"accountId\":\"5b10ac8d82e05b22cc7d4ef5\"}]"
```

#### 400 - Returned if `key` or `username`

#### 401 - Returned if the authentication credentials are incorrect or missing.

