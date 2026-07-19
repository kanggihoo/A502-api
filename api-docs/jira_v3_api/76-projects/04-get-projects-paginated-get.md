# 04-Get projects paginated [GET]

`GET /rest/api/3/project/search`

Returns a [paginated](#pagination) list of projects visible to the user.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Projects are returned only where the user has one of:

 *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. Must be less than or equal to 100. If a value greater than 100 is provided, the `maxResults` parameter will default to 100. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field.<br><br> *  `category` Sorts by project category. A complete list of category IDs is found using [Get all project categories](#api-rest-api-3-projectCategory-get).<br> *  `issueCount` Sorts by the total number of issues in each project.<br> *  `key` Sorts by project key.<br> *  `lastIssueUpdatedTime` Sorts by the last issue update time.<br> *  `name` Sorts by project name.<br> *  `owner` Sorts by project lead.<br> *  `archivedDate` EXPERIMENTAL. Sorts by project archived date.<br> *  `deletedDate` EXPERIMENTAL. Sorts by project deleted date. |
| `id` | `array` | `query` | No | The project IDs to filter the results by. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. Up to 50 project IDs can be provided. |
| `keys` | `array` | `query` | No | The project keys to filter the results by. To include multiple keys, provide an ampersand-separated list. For example, `keys=PA&keys=PB`. Up to 50 project keys can be provided. |
| `query` | `string` | `query` | No | Filter the results using a literal string. Projects with a matching `key` or `name` are returned (case insensitive). |
| `typeKey` | `string` | `query` | No | Orders results by the [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes). This parameter accepts a comma-separated list. Valid values are `business`, `service_desk`, and `software`. |
| `categoryId` | `integer` | `query` | No | The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation. |
| `action` | `string` | `query` | No | Filter results by projects for which the user can:<br><br> *  `view` the project, meaning that they have one of the following permissions:<br>    <br>     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.<br>     *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.<br>     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).<br> *  `browse` the project, meaning that they have the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.<br> *  `edit` the project, meaning that they have one of the following permissions:<br>    <br>     *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.<br>     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).<br> *  `create` the project, meaning that they have the *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue is created. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:<br><br> *  `description` Returns the project description.<br> *  `projectKeys` Returns all project keys associated with a project.<br> *  `lead` Returns information about the project lead.<br> *  `issueTypes` Returns all issue types associated with the project.<br> *  `url` Returns the URL associated with the project.<br> *  `insight` EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project. |
| `status` | `array` | `query` | No | EXPERIMENTAL. Filter results by project status:<br><br> *  `live` Search live projects.<br> *  `archived` Search archived projects.<br> *  `deleted` Search deleted projects, those in the recycle bin. |
| `properties` | `array` | `query` | No | EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list. |
| `propertyQuery` | `string` | `query` | No | EXPERIMENTAL. A query string used to search properties. The query string cannot be specified using a JSON object. For example, to search for the value of `nested` from `{"something":{"nested":1,"other":2}}` use `[thepropertykey].something.nested=1`. Note that the propertyQuery key is enclosed in square brackets to enable searching where the propertyQuery key includes dot (.) or equals (=) characters. Note that `thepropertykey` is only returned when included in `properties`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":2,\"nextPage\":\"https://your-domain.atlassian.net/rest/api/3/project/search?startAt=2&maxResults=2\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/search?startAt=0&maxResults=2\",\"startAt\":0,\"total\":7,\"values\":[{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/EX\",\"simplified\":false,\"style\":\"classic\"},{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10001\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10001\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10001\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10001\"},\"id\":\"10001\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"key\":\"ABC\",\"name\":\"Alphabetical\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/ABC\",\"simplified\":false,\"style\":\"classic\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if no projects matching the search criteria are found.

