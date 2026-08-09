# 01-Get all projects [GET]

`GET /rest/api/3/project`

Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-api-3-project-search-get) that supports search and pagination.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Projects are returned only where the user has *Browse Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:<br><br> *  `description` Returns the project description.<br> *  `issueTypes` Returns all issue types associated with the project.<br> *  `lead` Returns information about the project lead.<br> *  `projectKeys` Returns all project keys associated with the project. |
| `recent` | `integer` | `query` | No | Returns the user's most recently accessed projects. You may specify the number of results to return up to a maximum of 20. If access is anonymous, then the recently accessed projects are based on the current HTTP session. |
| `properties` | `array` | `query` | No | A list of project properties to return for the project. This parameter accepts a comma-separated list. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"insight\":{\"lastIssueUpdateTime\":1619069825000,\"totalIssueCount\":100},\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/EX\",\"simplified\":false,\"style\":\"CLASSIC\"},{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10001\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10001\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10001\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10001\"},\"id\":\"10001\",\"insight\":{\"lastIssueUpdateTime\":1619069825000,\"totalIssueCount\":100},\"key\":\"ABC\",\"name\":\"Alphabetical\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/ABC\",\"simplified\":false,\"style\":\"CLASSIC\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

