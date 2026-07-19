# 04-Update screen tab [PUT]

`PUT /rest/api/3/screens/{screenId}/tabs/{tabId}`

Updates the name of a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |
| `tabId` | `integer` | `path` | Yes | The ID of the screen tab. |

### Request Body (application/json)

```json
{
  "id": integer, // The ID of the screen tab.
  "name": string (required), // The name of the screen tab. The maximum length is 255 characters.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":10000,\"name\":\"Fields Tab\"}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the screen or screen tab is not found.

