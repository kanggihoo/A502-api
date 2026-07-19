# 08-Add issue types to issue type scheme [PUT]

`PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype`

Adds issue types to an issue type scheme.

The added issue types are appended to the issue types list.

If any of the issue types exist in the issue type scheme, the operation fails and no issue types are added.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeSchemeId` | `integer` | `path` | Yes | The ID of the issue type scheme. |

### Request Body (application/json)

```json
{
  "issueTypeIds": [
    string
  ] (required), // The list of issue type IDs.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"These issue types were not added because they are already present in the issue type scheme: 10002, 10003\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type or the issue type scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"These issue types were not found: 10000, 10002\"],\"errors\":{}}"
```

