# 04-Delete screen scheme [DELETE]

`DELETE /rest/api/3/screenscheme/{screenSchemeId}`

Deletes a screen scheme. A screen scheme cannot be deleted if it is used in an issue type screen scheme.

Only screens schemes used in classic projects can be deleted.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenSchemeId` | `string` | `path` | Yes | The ID of the screen scheme. |

### Responses

#### 204 - Returned if the screen scheme is deleted.

#### 400 - Returned if the screen scheme is used in an issue type screen scheme.

Example (application/json):
```json
"{\"errorMessages\":[\"The screen scheme cannot be deleted as it is in use in an issue type screen scheme.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access screen schemes.\"],\"errors\":{}}"
```

#### 404 - Returned if the screen scheme is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The screen scheme was not found.\"],\"errors\":{}}"
```

