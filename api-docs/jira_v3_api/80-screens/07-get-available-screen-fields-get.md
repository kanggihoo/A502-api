# 07-Get available screen fields [GET]

`GET /rest/api/3/screens/{screenId}/availableFields`

Returns the fields that can be added to a tab on a screen.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |

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

#### 404 - Returned if the screen is not found.

