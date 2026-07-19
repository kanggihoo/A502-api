# 04-Delete UI modification [DELETE]

`DELETE /rest/api/3/uiModifications/{uiModificationId}`

Deletes a UI modification. All the contexts that belong to the UI modification are deleted too. UI modification can only be deleted by Forge apps.

**[Permissions](#permissions) required:** None.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `uiModificationId` | `string` | `path` | Yes | The ID of the UI modification. |

### Responses

#### 204 - Returned if the UI modification is deleted.

Schema (application/json):
```json
any
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the request is not from a Forge app.

#### 404 - Returned if the UI modification is not found.

