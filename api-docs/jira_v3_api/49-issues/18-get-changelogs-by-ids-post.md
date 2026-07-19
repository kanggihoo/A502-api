# 18-Get changelogs by IDs [POST]

`POST /rest/api/3/issue/{issueIdOrKey}/changelog/list`

Returns changelogs for an issue specified by a list of changelog IDs.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |

### Request Body (application/json)

```json
{
  "changelogIds": [
    integer
  ] (required), // The list of changelog IDs.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"histories\":[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":true,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"created\":\"1970-01-18T06:27:50.429+0000\",\"id\":\"10001\",\"items\":[{\"field\":\"fields\",\"fieldtype\":\"jira\",\"fieldId\":\"fieldId\",\"from\":null,\"fromString\":\"\",\"to\":null,\"toString\":\"label-1\"}]},{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":true,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"created\":\"1970-01-18T06:27:51.429+0000\",\"id\":\"10002\",\"items\":[{\"field\":\"fields\",\"fieldtype\":\"jira\",\"fieldId\":\"fieldId\",\"from\":null,\"fromString\":\"label-1\",\"to\":null,\"toString\":\"label-1 label-2\"}]}],\"maxResults\":2,\"startAt\":0,\"total\":2}"
```

#### 400 - Returned if the request is not valid.

#### 404 - Returned if the issue is not found or the user does not have the necessary permission.

