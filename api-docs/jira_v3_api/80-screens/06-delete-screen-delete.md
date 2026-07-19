# 06-Delete screen [DELETE]

`DELETE /rest/api/3/screens/{screenId}`

Deletes a screen. A screen cannot be deleted if it is used in a screen scheme, workflow, or workflow draft.

Only screens used in classic projects can be deleted.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The screen is used in a screen scheme.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can manage screens.\"],\"errors\":{}}"
```

#### 404 - Returned if the screen is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The screen was not found.\"],\"errors\":{}}"
```

