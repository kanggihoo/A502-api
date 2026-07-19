# 04-Move screen tab field [POST]

`POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move`

Moves a screen tab field.

If `after` and `position` are provided in the request, `position` is ignored.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `screenId` | `integer` | `path` | Yes | The ID of the screen. |
| `tabId` | `integer` | `path` | Yes | The ID of the screen tab. |
| `id` | `string` | `path` | Yes | The ID of the field. |

### Request Body (application/json)

```json
{
  "after": string, // The ID of the screen tab field after which to place the moved screen tab field. Required if `position` isn't provided.
  "position": enum("Earlier" | "Later" | "First" | "Last"), // The named position to which the screen tab field should be moved. Required if `after` isn't provided.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the screen, screen tab, or field is not found or the field can't be moved to the requested position.

