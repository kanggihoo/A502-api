# 06-Update issue type screen scheme [PUT]

`PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}`

Updates an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueTypeScreenSchemeId` | `string` | `path` | Yes | The ID of the issue type screen scheme. |

### Request Body (application/json)

```json
{
  "description": string, // The description of the issue type screen scheme. The maximum length is 255 characters.
  "name": string, // The name of the issue type screen scheme. The name must be unique. The maximum length is 255 characters.
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
"{\"errorMessages\":[\"The issue type screen scheme name is in use.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access issue type screen schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the issue type screen scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The issue type screen scheme was not found.\"],\"errors\":{}}"
```

