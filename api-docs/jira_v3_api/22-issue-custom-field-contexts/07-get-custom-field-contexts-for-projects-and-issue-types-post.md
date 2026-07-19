# 07-Get custom field contexts for projects and issue types [POST]

`POST /rest/api/3/field/{fieldId}/context/mapping`

Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping, the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the project and issue type.

If there is no custom field context assigned to the project then, if present, the custom field context that applies to all projects is returned if it also applies to the issue type or all issue types. If a custom field context is not found, the returned custom field context ID is `null`.

Duplicate project and issue type mappings cannot be provided in the request.

The order of the returned values is the same as provided in the request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Request Body (application/json)

```json
{
  "mappings": [
    {
      "issueTypeId": string (required), // The ID of the issue type.
      "projectId": string (required), // The ID of the project.
    }
  ] (required), // The project and issue type mappings.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":3,\"values\":[{\"projectId\":\"10000\",\"issueTypeId\":\"10000\",\"contextId\":\"10000\"},{\"projectId\":\"10000\",\"issueTypeId\":\"10001\",\"contextId\":null},{\"projectId\":\"10001\",\"issueTypeId\":\"10002\",\"contextId\":\"10003\"}]}"
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"Duplicate project and issue type mappings cannot be provided.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access custom field contexts.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field, project, or issue type is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"These projects were not found: 10005.\"],\"errors\":{}}"
```

