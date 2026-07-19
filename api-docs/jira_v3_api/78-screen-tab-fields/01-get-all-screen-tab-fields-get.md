# 01-Get all screen tab fields [GET]

`GET /rest/api/3/screens/{screenId}/tabs/{tabId}/fields`

Returns all fields for a screen tab.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |
| `tabId` | `integer` | `path` | Yes | The ID of the screen tab. |
| `projectKey` | `string` | `query` | No | The key of the project. |

### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
[
  {
    "id": string, // The ID of the screen tab field.
    "name": string, // The name of the screen tab field. Required on create and update. The maximum length is 255 characters.
  }
]
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the screen or screen tab is not found.

