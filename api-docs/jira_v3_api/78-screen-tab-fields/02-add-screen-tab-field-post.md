# 02-Add screen tab field [POST]

`POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields`

Adds a field to a screen tab.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |
| `tabId` | `integer` | `path` | Yes | The ID of the screen tab. |
| `skipFieldAssociation` | `boolean` | `query` | No |  |

### Request Body (application/json)

```json
{
  "fieldId": string (required), // The ID of the field to add.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"summary\",\"name\":\"Summary\"}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the screen, screen tab, or field is not found.

