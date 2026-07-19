# 04-Add share permission [POST]

`POST /rest/api/3/filter/{id}/permission`

Add a share permissions to a filter. If you add a global share permission (one for all logged-in users or the public) it will overwrite all share permissions for the filter.

Be aware that this operation uses different objects for updating share permissions compared to [Update filter](#api-rest-api-3-filter-id-put).

**[Permissions](#permissions) required:** *Share dashboards and filters* [global permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the filter. |

### Request Body (application/json)

```json
{
  "accountId": string, // The user account ID that the filter is shared with. For a request, specify the `accountId` property for the user.
  "groupId": string, // The ID of the group, which uniquely identifies the group across all Atlassian products.For example, *952d12c3-5b5b-4d04-bb32-44d383afc4b2*. Cannot be provided with `groupname`.
  "groupname": string, // The name of the group to share the filter with. Set `type` to `group`. Please note that the name of a group is mutable, to reliably identify a group use `groupId`.
  "projectId": string, // The ID of the project to share the filter with. Set `type` to `project`.
  "projectRoleId": string, // The ID of the project role to share the filter with. Set `type` to `projectRole` and the `projectId` for the project that the role is in.
  "rights": integer, // The rights for the share permission.
  "type": enum("user" | "project" | "group" | "projectRole" | "global" | "authenticated") (required), // The type of the share permission.Specify the type as follows:   *  `user` Share with a user.  *  `group` Share with a group. Specify `groupname` as well.  *  `project` Share with a project. Specify `projectId` as well.  *  `projectRole` Share with a project role in a project. Specify `projectId` and `projectRoleId` as well.  *  `global` Share globally, including anonymous users. If set, this type overrides all existing share permissions and must be deleted before any non-global share permissions is set.  *  `authenticated` Share with all logged-in users. This shows as `loggedin` in the response. If set, this type overrides all existing share permissions and must be deleted before any non-global share permissions is set.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"[{\"id\":10000,\"type\":\"global\"},{\"id\":10010,\"project\":{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10000\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/EX\",\"simplified\":false,\"style\":\"classic\"},\"type\":\"project\"},{\"id\":10010,\"project\":{\"avatarUrls\":{\"16x16\":\"https://your-domain.atlassian.net/secure/projectavatar?size=xsmall&pid=10002\",\"24x24\":\"https://your-domain.atlassian.net/secure/projectavatar?size=small&pid=10002\",\"32x32\":\"https://your-domain.atlassian.net/secure/projectavatar?size=medium&pid=10002\",\"48x48\":\"https://your-domain.atlassian.net/secure/projectavatar?size=large&pid=10002\"},\"deleted\":true,\"deletedBy\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"deletedDate\":\"2022-11-11T13:35:29.000+0000\",\"id\":\"10002\",\"insight\":{\"lastIssueUpdateTime\":\"2021-04-22T05:37:05.000+0000\",\"totalIssueCount\":100},\"key\":\"MKY\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"First Project Category\",\"id\":\"10000\",\"name\":\"FIRST\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/projectCategory/10000\"},\"retentionTillDate\":\"2023-01-10T13:35:29.000+0000\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY\",\"simplified\":false,\"style\":\"classic\"},\"role\":{\"self\":\"https://your-domain.atlassian.net/rest/api/3/project/MKY/role/10360\",\"name\":\"Developers\",\"id\":10360,\"description\":\"A project role that represents developers in a project\",\"actors\":[{\"actorGroup\":{\"name\":\"jira-developers\",\"displayName\":\"jira-developers\",\"groupId\":\"952d12c3-5b5b-4d04-bb32-44d383afc4b2\"},\"displayName\":\"jira-developers\",\"id\":10240,\"name\":\"jira-developers\",\"type\":\"atlassian-group-role-actor\"},{\"actorUser\":{\"accountId\":\"5b10a2844c20165700ede21g\"},\"displayName\":\"Mia Krystof\",\"id\":10241,\"type\":\"atlassian-user-role-actor\"}],\"scope\":{\"project\":{\"id\":\"10000\",\"key\":\"KEY\",\"name\":\"Next Gen Project\"},\"type\":\"PROJECT\"}},\"type\":\"project\"},{\"group\":{\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"jira-administrators\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625\"},\"id\":10010,\"type\":\"group\"}]"
```

#### 400 - Returned if:

 *  the request object is invalid. For example, it contains an invalid type, the ID does not match the type, or the project or group is not found.
 *  the user does not own the filter.
 *  the user does not have the required permissions.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  the filter is not found.
 *  the user does not have permission to view the filter.

