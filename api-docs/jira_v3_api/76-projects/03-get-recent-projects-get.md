# 03-Get recent projects [GET]

`GET /rest/api/3/project/recent`

Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Projects are returned only where the user has one of:

 *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:<br><br> *  `description` Returns the project description.<br> *  `projectKeys` Returns all project keys associated with a project.<br> *  `lead` Returns information about the project lead.<br> *  `issueTypes` Returns all issue types associated with the project.<br> *  `url` Returns the URL associated with the project.<br> *  `permissions` Returns the permissions associated with the project.<br> *  `insight` EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project.<br> *  `*` Returns the project with all available expand options. |
| `properties` | `array` | `query` | No | EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list. Invalid property names are ignored. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"insight\":{\"lastIssueUpdateTime\":1619069825000,\"totalIssueCount\":100},\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/EX\",\"simplified\":false,\"style\":\"CLASSIC\"},{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10001\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10001\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10001\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10001\"},\"id\":\"10001\",\"insight\":{\"lastIssueUpdateTime\":1619069825000,\"totalIssueCount\":100},\"key\":\"ABC\",\"name\":\"Alphabetical\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/ABC\",\"simplified\":false,\"style\":\"CLASSIC\"}]"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

