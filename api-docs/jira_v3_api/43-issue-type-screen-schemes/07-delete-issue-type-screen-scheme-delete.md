# 07-Delete issue type screen scheme [DELETE]

`DELETE /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}`

Deletes an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeScreenSchemeId` | `string` | `path` | Yes | The ID of the issue type screen scheme. |

### Responses

#### 204 - Returned if the issue type screen scheme is deleted.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type screen scheme cannot be deleted because it is assigned to one or more projects.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

#### 404 - Returned if the issue type screen scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type screen scheme was not found.\"],\"errors\":{}}"
```

