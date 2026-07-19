# 02-Get all screen tabs [GET]

`GET /rest/api/3/screens/{screenId}/tabs`

Returns the list of tabs for a screen.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |
| `projectKey` | `string` | `query` | No | The key of the project. |

### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
[
  {
    "id": integer, // The ID of the screen tab.
    "name": string (required), // The name of the screen tab. The maximum length is 255 characters.
  }
]
```

#### 400 - Returned if the screen ID is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the screen is not found.

