# 01-Get screens for a field [GET]

`GET /rest/api/3/field/{fieldId}/screens`

Returns a [paginated](#pagination) list of the screens a field is used in.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the field to return screens for. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about screens in the response. This parameter accepts `tab` which returns details about the screen tabs the field is used in. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":1,\"startAt\":0,\"total\":5,\"values\":[{\"id\":10001,\"name\":\"Default Screen\",\"description\":\"Provides for the update of all system fields.\",\"tab\":{\"id\":10000,\"name\":\"Fields Tab\"}}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

