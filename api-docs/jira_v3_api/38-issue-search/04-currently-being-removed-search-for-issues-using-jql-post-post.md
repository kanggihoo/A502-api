# 04-Currently being removed. Search for issues using JQL (POST) [POST]

`POST /rest/api/3/search`

Endpoint is currently being removed. [More details](https://developer.atlassian.com/changelog/#CHANGE-2046)

Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ).

There is a [GET](#api-rest-api-3-search-get) version of this resource that can be used for smaller JQL query expressions.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Issues are included in the response where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Request Body (application/json)

```json
{
  "expand": [
    string
  ], // Use [expand](#expansion) to include additional information about issues in the response. Note that, unlike the majority of instances where `expand` is specified, `expand` is defined as a list of values. The expand options are:   *  `renderedFields` Returns field values rendered in HTML format.  *  `names` Returns the display name of each field.  *  `schema` Returns the schema describing a field type.  *  `transitions` Returns all possible transitions for the issue.  *  `operations` Returns all possible operations for the issue.  *  `editmeta` Returns information about how each field can be edited.  *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.  *  `versionedRepresentations` Instead of `fields`, returns `versionedRepresentations` a JSON array containing each version of a field's value, with the highest numbered item representing the most recent version.
  "fields": [
    string
  ], // A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include:   *  `*all` Returns all fields.  *  `*navigable` Returns navigable fields.  *  Any issue field, prefixed with a minus to exclude.  The default is `*navigable`.  Examples:   *  `summary,comment` Returns the summary and comments fields only.  *  `-description` Returns all navigable (default) fields except description.  *  `*all,-comment` Returns all fields except comments.  Multiple `fields` parameters can be included in a request.  Note: All navigable fields are returned by default. This differs from [GET issue](#api-rest-api-3-issue-issueIdOrKey-get) where the default is all fields.
  "fieldsByKeys": boolean, // Reference fields by their key (rather than ID). The default is `false`.
  "jql": string, // A [JQL](https://confluence.atlassian.com/x/egORLQ) expression.
  "maxResults": integer, // The maximum number of items to return per page.
  "properties": [
    string
  ], // A list of up to 5 issue properties to include in the results. This parameter accepts a comma-separated list.
  "startAt": integer, // The index of the first item to return in the page of results (page offset). The base index is `0`.
  "validateQuery": enum("strict" | "warn" | "none" | "true" | "false"), // Determines how to validate the JQL query and treat the validation results. Supported values:   *  `strict` Returns a 400 response code if any errors are found, along with a list of all errors (and warnings).  *  `warn` Returns all errors as warnings.  *  `none` No validation is performed.  *  `true` *Deprecated* A legacy synonym for `strict`.  *  `false` *Deprecated* A legacy synonym for `warn`.  The default is `strict`.  Note: If the JQL is not correctly formed a 400 response code is returned, regardless of the `validateQuery` value.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"expand\":\"names,schema\",\"issues\":[{\"expand\":\"\",\"fields\":{\"watcher\":{\"isWatching\":false,\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/EX-1/watchers\",\"watchCount\":1},\"attachment\":[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"content\":\"https://your-domain.atlassian.net/jira/rest/api/3/attachment/content/10000\",\"created\":\"2022-10-06T07:32:47.000+0000\",\"filename\":\"picture.jpg\",\"id\":10000,\"mimeType\":\"image/jpeg\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/attachments/10000\",\"size\":23123,\"thumbnail\":\"https://your-domain.atlassian.net/jira/rest/api/3/attachment/thumbnail/10000\"}],\"sub-tasks\":[{\"id\":\"10000\",\"outwardIssue\":{\"fields\":{\"status\":{\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/statuses/open.png\",\"name\":\"Open\"}},\"id\":\"10003\",\"key\":\"ED-2\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/ED-2\"},\"type\":{\"id\":\"10000\",\"inward\":\"Parent\",\"name\":\"\",\"outward\":\"Sub-task\"}}],\"description\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"Main order flow broken\"}]}]},\"project\":{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/EX\",\"simplified\":false,\"style\":\"classic\"},\"comment\":[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"body\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.\"}]}]},\"created\":\"2021-01-17T12:34:00.000+0000\",\"id\":\"10000\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10010/comment/10000\",\"updateAuthor\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"updated\":\"2021-01-18T23:45:00.000+0000\",\"visibility\":{\"identifier\":\"Administrators\",\"type\":\"role\",\"value\":\"Administrators\"}}],\"issuelinks\":[{\"id\":\"10001\",\"outwardIssue\":{\"fields\":{\"status\":{\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/statuses/open.png\",\"name\":\"Open\"}},\"id\":\"10004L\",\"key\":\"PR-2\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/PR-2\"},\"type\":{\"id\":\"10000\",\"inward\":\"depends on\",\"name\":\"Dependent\",\"outward\":\"is depended by\"}},{\"id\":\"10002\",\"inwardIssue\":{\"fields\":{\"status\":{\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/statuses/open.png\",\"name\":\"Open\"}},\"id\":\"10004\",\"key\":\"PR-3\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/PR-3\"},\"type\":{\"id\":\"10000\",\"inward\":\"depends on\",\"name\":\"Dependent\",\"outward\":\"is depended by\"}}],\"worklog\":[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"comment\":{\"type\":\"doc\",\"version\":1,\"content\":[{\"type\":\"paragraph\",\"content\":[{\"type\":\"text\",\"text\":\"I did some work here.\"}]}]},\"id\":\"100028\",\"issueId\":\"10002\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10010/worklog/10000\",\"started\":\"2021-01-17T12:34:00.000+0000\",\"timeSpent\":\"3h 20m\",\"timeSpentSeconds\":12000,\"updateAuthor\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"updated\":\"2021-01-18T23:45:00.000+0000\",\"visibility\":{\"identifier\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"type\":\"group\",\"value\":\"jira-developers\"}}],\"updated\":1,\"timetracking\":{\"originalEstimate\":\"10m\",\"originalEstimateSeconds\":600,\"remainingEstimate\":\"3m\",\"remainingEstimateSeconds\":200,\"timeSpent\":\"6m\",\"timeSpentSeconds\":400}},\"id\":\"10002\",\"key\":\"ED-1\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/10002\"}],\"maxResults\":50,\"startAt\":0,\"total\":1,\"warningMessages\":[\"The value 'bar' does not exist for the field 'foo'.\"]}"
```

#### 400 - Returned if the JQL query is invalid.

#### 401 - Returned if the authentication credentials are incorrect.

