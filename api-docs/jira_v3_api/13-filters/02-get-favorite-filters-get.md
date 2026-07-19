# 02-Get favorite filters [GET]

`GET /rest/api/3/filter/favourite`

Returns the visible favorite filters of the user.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** A favorite filter is only visible to the user where the filter is:

 *  owned by the user.
 *  shared with a group that the user is a member of.
 *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  shared with a public project.
 *  shared with the public.

For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.<br> *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"approximateLastUsed\":\"2023-03-01T13:15:00.000+0000\",\"description\":\"Lists all open bugs\",\"favourite\":true,\"favouritedCount\":0,\"id\":\"10000\",\"jql\":\"type = Bug and resolution is empty\",\"name\":\"All Open Bugs\",\"owner\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"searchUrl\":\"https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/filter/10000\",\"sharePermissions\":[],\"subscriptions\":{\"end-index\":0,\"items\":[],\"max-results\":0,\"size\":0,\"start-index\":0},\"viewUrl\":\"https://your-domain.atlassian.net/issues/?filter=10000\"},{\"approximateLastUsed\":null,\"description\":\"Issues assigned to me\",\"favourite\":true,\"favouritedCount\":0,\"id\":\"10010\",\"jql\":\"assignee = currentUser() and resolution is empty\",\"name\":\"My issues\",\"owner\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"searchUrl\":\"https://your-domain.atlassian.net/rest/api/3/search?jql=assignee+in+%28currentUser%28%29%29+and+resolution+is+empty\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/filter/10010\",\"sharePermissions\":[{\"id\":10000,\"type\":\"global\"},{\"id\":10010,\"project\":{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/EX\",\"simplified\":false,\"style\":\"classic\"},\"type\":\"project\"}],\"subscriptions\":{\"end-index\":0,\"items\":[],\"max-results\":0,\"size\":0,\"start-index\":0},\"viewUrl\":\"https://your-domain.atlassian.net/issues/?filter=10010\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

