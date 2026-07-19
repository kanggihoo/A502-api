# 05-Search for dashboards [GET]

`GET /rest/api/3/dashboard/search`

Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include dashboards that have specific attributes. For example, dashboards with a particular name. When multiple attributes are specified only filters matching all attributes are returned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** The following dashboards that match the query parameters are returned:

 *  Dashboards owned by the user. Not returned for anonymous users.
 *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.
 *  Dashboards shared with a private project that the user can browse. Not returned for anonymous users.
 *  Dashboards shared with a public project.
 *  Dashboards shared with the public.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `dashboardName` | `string` | `query` | No | String used to perform a case-insensitive partial match with `name`. |
| `accountId` | `string` | `query` | No | User account ID used to return dashboards with the matching `owner.accountId`. This parameter cannot be used with the `owner` parameter. |
| `owner` | `string` | `query` | No | This parameter is deprecated because of privacy changes. Use `accountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return dashboards with the matching `owner.name`. This parameter cannot be used with the `accountId` parameter. |
| `groupname` | `string` | `query` | No | As a group's name can change, use of `groupId` is recommended. Group name used to return dashboards that are shared with a group that matches `sharePermissions.group.name`. This parameter cannot be used with the `groupId` parameter. |
| `groupId` | `string` | `query` | No | Group ID used to return dashboards that are shared with a group that matches `sharePermissions.group.groupId`. This parameter cannot be used with the `groupname` parameter. |
| `projectId` | `integer` | `query` | No | Project ID used to returns dashboards that are shared with a project that matches `sharePermissions.project.id`. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `description` Sorts by dashboard description. Note that this sort works independently of whether the expand to display the description field is in use.<br> *  `favourite_count` Sorts by dashboard popularity.<br> *  `id` Sorts by dashboard ID.<br> *  `is_favourite` Sorts by whether the dashboard is marked as a favorite.<br> *  `name` Sorts by dashboard name.<br> *  `owner` Sorts by dashboard owner name. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `status` | `string` | `query` | No | The status to filter by. It may be active, archived or deleted. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about dashboard in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `description` Returns the description of the dashboard.<br> *  `owner` Returns the owner of the dashboard.<br> *  `viewUrl` Returns the URL that is used to view the dashboard.<br> *  `favourite` Returns `isFavourite`, an indicator of whether the user has set the dashboard as a favorite.<br> *  `favouritedCount` Returns `popularity`, a count of how many users have set this dashboard as a favorite.<br> *  `sharePermissions` Returns details of the share permissions defined for the dashboard.<br> *  `editPermissions` Returns details of the edit permissions defined for the dashboard.<br> *  `isWritable` Returns whether the current user has permission to edit the dashboard. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"self\":\"https://your-domain.atlassian.net/rest/api/3/dashboard/search?expand=owner&maxResults=50&startAt=0\",\"startAt\":0,\"total\":2,\"values\":[{\"description\":\"Testing program\",\"id\":\"1\",\"isFavourite\":true,\"name\":\"Testing\",\"owner\":{\"self\":\"https://your-domain.atlassian.net/user?accountId=5b10a2844c20165700ede21g\",\"displayName\":\"Mia\",\"active\":true,\"accountId\":\"5b10a2844c20165700ede21g\",\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"}},\"popularity\":1,\"self\":\"https://your-domain.atlassian.net/rest/api/3/dashboard/1\",\"sharePermissions\":[{\"type\":\"global\"}],\"view\":\"https://your-domain.atlassian.net/Dashboard.jspa?selectPageId=1\"},{\"description\":\"Quantum initiative\",\"id\":\"2\",\"isFavourite\":false,\"name\":\"Quantum \",\"owner\":{\"self\":\"https://your-domain.atlassian.net/user?accountId=5b10a2844c20165700ede21g\",\"displayName\":\"Mia\",\"active\":true,\"accountId\":\"5b10a2844c20165700ede21g\",\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"}},\"popularity\":0,\"self\":\"https://your-domain.atlassian.net/rest/api/3/dashboard/2\",\"sharePermissions\":[{\"type\":\"loggedin\"}],\"view\":\"https://your-domain.atlassian.net/Dashboard.jspa?selectPageId=2\"}]}"
```

#### 400 - Returned if:

 *  `orderBy` is invalid.
 *  `expand` includes an invalid value.
 *  `accountId` and `owner` are provided.
 *  `groupname` and `groupId` are provided.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

#### 401 - 401 response

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

