# 09-Update issue type screen scheme default screen scheme [PUT]

`PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default`

Updates the default screen scheme of an issue type screen scheme. The default screen scheme is used for all unmapped issue types.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeScreenSchemeId` | `string` | `path` | Yes | The ID of the issue type screen scheme. |

### Request Body (application/json)

```json
{
  "screenSchemeId": string (required), // The ID of the screen scheme.
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
"{\"errorMessages\":[\"The screenSchemeId has to be provided.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type screen schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type screen scheme or the screen scheme is not found, or the screen scheme isn't used in classic projects.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type screen scheme was not found.\"],\"errors\":{}}"
```

