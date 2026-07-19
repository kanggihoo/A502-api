# 10-Remove issue type from issue type scheme [DELETE]

`DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}`

Removes an issue type from an issue type scheme.

This operation cannot remove:

 *  any issue type used by issues.
 *  any issue types from the default issue type scheme.
 *  the last standard issue type from an issue type scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeSchemeId` | `integer` | `path` | Yes | The ID of the issue type scheme. |
| `issueTypeId` | `integer` | `path` | Yes | The ID of the issue type. |

### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Can't remove the last standard issue type from the issue type scheme.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type scheme is missing or the issue type is not found in the issue type scheme.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type was not found in the issue type scheme.\"],\"errors\":{}}"
```

