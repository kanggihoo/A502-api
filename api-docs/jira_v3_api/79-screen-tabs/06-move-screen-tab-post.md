# 06-Move screen tab [POST]

`POST /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}`

Moves a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |
| `tabId` | `integer` | `path` | Yes | The ID of the screen tab. |
| `pos` | `integer` | `path` | Yes | The position of tab. The base index is 0. |

### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the screen or screen tab is not found or the position is invalid.

