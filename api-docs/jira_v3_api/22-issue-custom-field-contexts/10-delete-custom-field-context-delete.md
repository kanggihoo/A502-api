# 10-Delete custom field context [DELETE]

`DELETE /rest/api/3/field/{fieldId}/context/{contextId}`

Deletes a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html).

This API will not allow removing the global context from April 2026. Instead, an HTTP 400 response will be returned. See [CHANGE-3019](https://developer.atlassian.com/changelog/#CHANGE-3019)

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `contextId` | `integer` | `path` | Yes | The ID of the context. |

### Responses

#### 204 - Returned if the context is deleted.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The contextId has to be provided.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access custom field contexts.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field or the context is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The context was not found.\"],\"errors\":{}}"
```

