# 08-Get project mappings for custom field context [GET]

`GET /rest/api/3/field/{fieldId}/context/projectmapping`

Returns a [paginated](#pagination) list of context to project mappings for a custom field. The result can be filtered by `contextId`. Otherwise, all mappings are returned. Invalid IDs are ignored.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field, for example `customfield\_10000`. |
| `contextId` | `array` | `query` | No | The list of context IDs. To include multiple context, separate IDs with ampersand: `contextId=10000&contextId=10001`. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":2,\"values\":[{\"contextId\":\"10025\",\"projectId\":\"10001\"},{\"contextId\":\"10026\",\"isGlobalContext\":true}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access custom field contexts.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field was not found.\"],\"errors\":{}}"
```

