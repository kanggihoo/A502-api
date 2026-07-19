# 08-Search issue security schemes [GET]

`GET /rest/api/3/issuesecurityschemes/search`

Returns a [paginated](#pagination) list of issue security schemes.  
If you specify the project ID parameter, the result will contain issue security schemes and related project IDs you filter by. Use \{@link IssueSecuritySchemeResource\#searchProjectsUsingSecuritySchemes(String, String, Set, Set)\} to obtain all projects related to scheme.

Only issue security schemes in the context of classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `string` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `string` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No | The list of issue security scheme IDs. To include multiple issue security scheme IDs, separate IDs with an ampersand: `id=10000&id=10001`. |
| `projectId` | `array` | `query` | No | The list of project IDs. To include multiple project IDs, separate IDs with an ampersand: `projectId=10000&projectId=10001`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":10000,\"self\":\"https://your-domain.atlassian.net/rest/api/3/issuesecurityscheme/10000\",\"name\":\"Default scheme\",\"description\":\"Default scheme description\",\"defaultLevel\":10001,\"projectIds\":[10002]}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"-1000 is not a valid value. id must be zero or a positive integer.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user doesn't have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"You are not authorized to perform this action. Administrator privileges are required.\"],\"errors\":{}}"
```

