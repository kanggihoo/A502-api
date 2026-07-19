# 03-Get approximate application license count [GET]

`GET /rest/api/3/license/approximateLicenseCount/product/{applicationKey}`

Returns the total approximate number of user accounts for a single Jira license. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `applicationKey` | `string` | `path` | Yes | The ID of the application, represents a specific version of Jira. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"key\":\"license.jira-software.approximateUserCount\",\"value\":\"115\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

#### 403 - Returned if the user does not have permission to complete this request.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access license details.\"],\"errors\":{}}"
```

