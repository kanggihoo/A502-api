# 10-Get create field metadata for a project and issue type id [GET]

`GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}`

Returns a page of field metadata for a specified project and issuetype id. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The ID or key of the project. |
| `issueTypeId` | `string` | `path` | Yes | The issuetype ID. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"fields\":[{\"fieldId\":\"assignee\",\"hasDefaultValue\":false,\"key\":\"assignee\",\"name\":\"Assignee\",\"operations\":[\"set\"],\"required\":true}],\"maxResults\":1,\"startAt\":0,\"total\":1}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"Parameter 'maxResults' must not exceed the limit '200'\"],\"errors\":{},\"httpStatusCode\":{\"empty\":false,\"present\":true}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

