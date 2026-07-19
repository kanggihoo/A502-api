# 09-Get create metadata issue types for a project [GET]

`GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes`

Returns a page of issue type metadata for a specified project. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The ID or key of the project. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueTypes\":[{\"description\":\"An error in the code\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/issuetypes/bug.png\",\"id\":\"1\",\"name\":\"Bug\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/1\",\"subtask\":false}],\"maxResults\":1,\"startAt\":0,\"total\":1}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"Parameter 'maxResults' must not exceed the limit '200'\"],\"errors\":{},\"httpStatusCode\":{\"empty\":false,\"present\":true}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

