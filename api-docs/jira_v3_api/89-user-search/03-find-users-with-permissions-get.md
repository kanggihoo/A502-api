# 03-Find users with permissions [GET]

`GET /rest/api/3/user/permission/search`

Returns a list of users who fulfill these criteria:

 *  their user attributes match a search string.
 *  they have a set of permissions for a project or issue.

If no search string is provided, a list of all users with the permissions is returned.

This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission for the project or issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission for the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users for any project.
 *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project, to get users for that project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `query` | `string` | `query` | No | A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified. |
| `username` | `string` | `query` | No | This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. |
| `accountId` | `string` | `query` | No | A query string that is matched exactly against user `accountId`. Required, unless `query` is specified. |
| `permissions` | `string` | `query` | Yes | A comma separated list of permissions. Permissions can be specified as any:<br><br> *  permission returned by [Get all permissions](#api-rest-api-3-permissions-get).<br> *  custom project permission added by Connect apps.<br> *  (deprecated) one of the following:<br>    <br>     *  ASSIGNABLE\_USER<br>     *  ASSIGN\_ISSUE<br>     *  ATTACHMENT\_DELETE\_ALL<br>     *  ATTACHMENT\_DELETE\_OWN<br>     *  BROWSE<br>     *  CLOSE\_ISSUE<br>     *  COMMENT\_DELETE\_ALL<br>     *  COMMENT\_DELETE\_OWN<br>     *  COMMENT\_EDIT\_ALL<br>     *  COMMENT\_EDIT\_OWN<br>     *  COMMENT\_ISSUE<br>     *  CREATE\_ATTACHMENT<br>     *  CREATE\_ISSUE<br>     *  DELETE\_ISSUE<br>     *  EDIT\_ISSUE<br>     *  LINK\_ISSUE<br>     *  MANAGE\_WATCHER\_LIST<br>     *  MODIFY\_REPORTER<br>     *  MOVE\_ISSUE<br>     *  PROJECT\_ADMIN<br>     *  RESOLVE\_ISSUE<br>     *  SCHEDULE\_ISSUE<br>     *  SET\_ISSUE\_SECURITY<br>     *  TRANSITION\_ISSUE<br>     *  VIEW\_VERSION\_CONTROL<br>     *  VIEW\_VOTERS\_AND\_WATCHERS<br>     *  VIEW\_WORKFLOW\_READONLY<br>     *  WORKLOG\_DELETE\_ALL<br>     *  WORKLOG\_DELETE\_OWN<br>     *  WORKLOG\_EDIT\_ALL<br>     *  WORKLOG\_EDIT\_OWN<br>     *  WORK\_ISSUE |
| `issueKey` | `string` | `query` | No | The issue key for the issue. |
| `projectKey` | `string` | `query` | No | The project key for the project (case sensitive). |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},{\"accountId\":\"5b10ac8d82e05b22cc7d4ef5\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/AA-3.png?size=48&s=48\"},\"displayName\":\"Emma Richards\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10ac8d82e05b22cc7d4ef5\"}]"
```

#### 400 - Returned if:

 *  `issueKey` or `projectKey` is missing.
 *  `query` or `accountId` is missing.
 *  `query` and `accountId` are provided.
 *  `permissions` is empty or contains an invalid entry.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the issue or project is not found.

#### 429 - Returned if the rate limit is exceeded. User search endpoints share a collective rate limit for the tenant, in addition to Jira's normal rate limiting you may receive a rate limit for user search. Please respect the Retry-After header.

