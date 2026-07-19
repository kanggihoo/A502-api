# 05-Delete screen tab [DELETE]

`DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}`

Deletes a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |
| `tabId` | `integer` | `path` | Yes | The ID of the screen tab. |

### Responses

#### 204 - Returned if the request is successful.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the screen or screen tab is not found.

