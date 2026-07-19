# 06-Get field project associations [GET]

`GET /rest/api/3/field/{fieldId}/association/project`

Returns a [paginated](#pagination) list of project associations for the given custom field. Each association contains the ID of a project the field is associated with.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the field, for example `customfield_10000`. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":50,\"startAt\":0,\"total\":2,\"values\":[{\"projectId\":\"10010\"},{\"projectId\":\"10020\"}]}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

