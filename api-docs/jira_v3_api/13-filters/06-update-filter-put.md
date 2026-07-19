# 06-Update filter [PUT]

`PUT /rest/api/3/filter/{id}`

Updates a filter. Use this operation to update a filter's name, description, JQL, or sharing.

**[Permissions](#permissions) required:** Permission to access Jira, however the user must own the filter.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the filter to update. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.<br> *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`. |
| `overrideSharePermissions` | `boolean` | `query` | No | EXPERIMENTAL: Whether share permissions are overridden to enable the addition of any share permissions to filters. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). |

### Request Body (application/json)

```json
{
  "approximateLastUsed": string, // \[Experimental\] Approximate last used time. Returns the date and time when the filter was last used. Returns `null` if the filter hasn't been used after tracking was enabled. For performance reasons, timestamps aren't updated in real time and therefore may not be exactly accurate.
  "description": string, // A description of the filter.
  "editPermissions": [
    {
      "group": any, // The group that the filter is shared with. For a request, specify the `groupId` or `name` property for the group. As a group's name can change, use of `groupId` is recommended.
      "id": integer, // The unique identifier of the share permission.
      "project": any, // The project that the filter is shared with. This is similar to the project object returned by [Get project](#api-rest-api-3-project-projectIdOrKey-get) but it contains a subset of the properties, which are: `self`, `id`, `key`, `assigneeType`, `name`, `roles`, `avatarUrls`, `projectType`, `simplified`.   For a request, specify the `id` for the project.
      "role": any, // The project role that the filter is shared with.   For a request, specify the `id` for the role. You must also specify the `project` object and `id` for the project that the role is in.
      "type": enum("user" | "group" | "project" | "projectRole" | "global" | "loggedin" | "authenticated" | "project-unknown") (required), // The type of share permission:   *  `user` Shared with a user.  *  `group` Shared with a group. If set in a request, then specify `sharePermission.group` as well.  *  `project` Shared with a project. If set in a request, then specify `sharePermission.project` as well.  *  `projectRole` Share with a project role in a project. This value is not returned in responses. It is used in requests, where it needs to be specify with `projectId` and `projectRoleId`.  *  `global` Shared globally. If set in a request, no other `sharePermission` properties need to be specified.  *  `loggedin` Shared with all logged-in users. Note: This value is set in a request by specifying `authenticated` as the `type`.  *  `project-unknown` Shared with a project that the user does not have access to. Cannot be set in a request.
      "user": any, // The user account ID that the filter is shared with. For a request, specify the `accountId` property for the user.
    }
  ], // The groups and projects that can edit the filter.
  "favourite": boolean, // Whether the filter is selected as a favorite.
  "favouritedCount": integer, // The count of how many users have selected this filter as a favorite, including the filter owner.
  "id": string, // The unique identifier for the filter.
  "jql": string, // The JQL query for the filter. For example, *project = SSP AND issuetype = Bug*.
  "name": string (required), // The name of the filter. Must be unique.
  "owner": any, // The user who owns the filter. This is defaulted to the creator of the filter, however Jira administrators can change the owner of a shared filter in the admin settings.
  "searchUrl": string, // A URL to view the filter results in Jira, using the [Search for issues using JQL](#api-rest-api-3-filter-search-get) operation with the filter's JQL string to return the filter results. For example, *https://your-domain.atlassian.net/rest/api/3/search?jql=project+%3D+SSP+AND+issuetype+%3D+Bug*.
  "self": string, // The URL of the filter.
  "sharePermissions": [
    {
      "group": any, // The group that the filter is shared with. For a request, specify the `groupId` or `name` property for the group. As a group's name can change, use of `groupId` is recommended.
      "id": integer, // The unique identifier of the share permission.
      "project": any, // The project that the filter is shared with. This is similar to the project object returned by [Get project](#api-rest-api-3-project-projectIdOrKey-get) but it contains a subset of the properties, which are: `self`, `id`, `key`, `assigneeType`, `name`, `roles`, `avatarUrls`, `projectType`, `simplified`.   For a request, specify the `id` for the project.
      "role": any, // The project role that the filter is shared with.   For a request, specify the `id` for the role. You must also specify the `project` object and `id` for the project that the role is in.
      "type": enum("user" | "group" | "project" | "projectRole" | "global" | "loggedin" | "authenticated" | "project-unknown") (required), // The type of share permission:   *  `user` Shared with a user.  *  `group` Shared with a group. If set in a request, then specify `sharePermission.group` as well.  *  `project` Shared with a project. If set in a request, then specify `sharePermission.project` as well.  *  `projectRole` Share with a project role in a project. This value is not returned in responses. It is used in requests, where it needs to be specify with `projectId` and `projectRoleId`.  *  `global` Shared globally. If set in a request, no other `sharePermission` properties need to be specified.  *  `loggedin` Shared with all logged-in users. Note: This value is set in a request by specifying `authenticated` as the `type`.  *  `project-unknown` Shared with a project that the user does not have access to. Cannot be set in a request.
      "user": any, // The user account ID that the filter is shared with. For a request, specify the `accountId` property for the user.
    }
  ], // The groups and projects that the filter is shared with.
  "sharedUsers": any, // A paginated list of the users that the filter is shared with. This includes users that are members of the groups or can browse the projects that the filter is shared with.
  "subscriptions": any, // A paginated list of the users that are subscribed to the filter.
  "viewUrl": string, // A URL to view the filter results in Jira, using the ID of the filter. For example, *https://your-domain.atlassian.net/issues/?filter=10100*.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"approximateLastUsed\":\"2023-03-01T13:15:00.000+0000\",\"description\":\"Lists all open bugs\",\"favourite\":true,\"favouritedCount\":0,\"id\":\"10000\",\"jql\":\"type = Bug and resolution is empty\",\"name\":\"All Open Bugs\",\"owner\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"searchUrl\":\"https://your-domain.atlassian.net/rest/api/3/search?jql=type%20%3D%20Bug%20and%20resolutino%20is%20empty\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/filter/10000\",\"sharePermissions\":[],\"subscriptions\":{\"end-index\":0,\"items\":[],\"max-results\":0,\"size\":0,\"start-index\":0},\"viewUrl\":\"https://your-domain.atlassian.net/issues/?filter=10000\"}"
```

#### 400 - Returned if the request object is invalid. For example, the `name` is not unique or the project ID is not specified for a project role share permission.

#### 401 - Returned if the authentication credentials are incorrect or missing.

