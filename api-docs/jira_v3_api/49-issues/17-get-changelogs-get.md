# 17-Get changelogs [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/changelog`

Returns a [paginated](#pagination) list of all changelogs for an issue sorted by date, starting from the oldest.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":2,\"nextPage\":\"https://your-domain.atlassian.net/rest/api/3/issue/TT-1/changelog?&startAt=4&maxResults=2\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/TT-1/changelog?startAt=2&maxResults=2\",\"startAt\":2,\"total\":5,\"values\":[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":true,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"created\":\"1970-01-18T06:27:50.429+0000\",\"id\":\"10001\",\"items\":[{\"field\":\"fields\",\"fieldtype\":\"jira\",\"fieldId\":\"fieldId\",\"from\":null,\"fromString\":\"\",\"to\":null,\"toString\":\"label-1\"}]},{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":true,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"created\":\"1970-01-18T06:27:51.429+0000\",\"id\":\"10002\",\"items\":[{\"field\":\"fields\",\"fieldtype\":\"jira\",\"fieldId\":\"fieldId\",\"from\":null,\"fromString\":\"label-1\",\"to\":null,\"toString\":\"label-1 label-2\"}]}]}"
```

#### 404 - Returned if the issue is not found or the user does not have permission to view it.

