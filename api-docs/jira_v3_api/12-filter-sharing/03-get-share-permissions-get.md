# 03-Get share permissions [GET]

`GET /rest/api/3/filter/{id}/permission`

Returns the share permissions for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None, however, share permissions are only returned for:

 *  filters owned by the user.
 *  filters shared with a group that the user is a member of.
 *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  filters shared with a public project.
 *  filters shared with the public.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the filter. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"id\":10000,\"type\":\"global\"},{\"id\":10010,\"project\":{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/EX\",\"simplified\":false,\"style\":\"classic\"},\"type\":\"project\"},{\"id\":10010,\"project\":{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10002\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10002\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10002\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10002\"},\"deleted\":true,\"deletedBy\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"deletedDate\":\"2022-11-11T13:35:29.000+0000\",\"id\":\"10002\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"key\":\"MKY\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"retentionTillDate\":\"2023-01-10T13:35:29.000+0000\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY\",\"simplified\":false,\"style\":\"classic\"},\"role\":{\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360\",\"name\":\"Developers\",\"id\":10360,\"description\":\"A project role that represents developers in a project\",\"actors\":[{\"actorGroup\":{\"name\":\"jira-developers\",\"displayName\":\"jira-developers\",\"groupId\":\"952d12c3-5b5b-4d04-bb32-44d383afc4b2\"},\"displayName\":\"jira-developers\",\"id\":10240,\"name\":\"jira-developers\",\"type\":\"atlassian-group-role-actor\"},{\"actorUser\":{\"accountId\":\"5b10a2844c20165700ede21g\"},\"displayName\":\"Mia Krystof\",\"id\":10241,\"type\":\"atlassian-user-role-actor\"}],\"scope\":{\"project\":{\"id\":\"10000\",\"key\":\"KEY\",\"name\":\"Next Gen Project\"},\"type\":\"PROJECT\"}},\"type\":\"project\"},{\"group\":{\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"jira-administrators\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625\"},\"id\":10010,\"type\":\"group\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the filter is not found.
 *  the user does not have permission to view the filter.

