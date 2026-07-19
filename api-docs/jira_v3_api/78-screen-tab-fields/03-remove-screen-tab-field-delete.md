# 03-Remove screen tab field [DELETE]

`DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}`

Removes a field from a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |
| `tabId` | `integer` | `path` | Yes | The ID of the screen tab. |
| `id` | `string` | `path` | Yes | The ID of the field. |

### Responses

#### 204 - Returned if the request is successful.

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the screen, screen tab, or field is not found.

