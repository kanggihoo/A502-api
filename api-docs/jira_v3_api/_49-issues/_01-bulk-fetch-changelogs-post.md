# 01-Bulk fetch changelogs [POST]

`POST /rest/api/3/changelog/bulkfetch`

Bulk fetch changelogs for multiple issues and filter by fields

Returns a paginated list of all changelogs for given issues sorted by changelog date and issue IDs, starting from the oldest changelog and smallest issue ID.

Issues are identified by their ID or key, and optionally changelogs can be filtered by their field IDs. You can request the changelogs of up to 1000 issues and can filter them by up to 10 field IDs.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the projects that the issues are in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issues.

### Request Body (application/json)

```json
{
  "fieldIds": [
    string
  ], // List of field IDs to filter changelogs
  "issueIdsOrKeys": [
    string
  ] (required), // List of issue IDs/keys to fetch changelogs for
  "maxResults": integer, // The maximum number of items to return per page
  "nextPageToken": string, // The cursor for pagination
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issueChangeLogs\":[{\"changeHistories\":[{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":true,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"created\":1492070429,\"id\":\"10001\",\"items\":[{\"field\":\"fields\",\"fieldId\":\"fieldId\",\"fieldtype\":\"jira\",\"fromString\":\"old summary\",\"toString\":\"new summary\"}]},{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":true,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"created\":1492071429,\"id\":\"10002\",\"items\":[{\"field\":\"fields\",\"fieldId\":\"fieldId\",\"fieldtype\":\"jira\",\"fromString\":\"old summary 2\",\"toString\":\"new summary 2\"}]}],\"issueId\":\"10100\"}],\"nextPageToken\":\"UxAQBFRF\"}"
```

#### 400 - Returned if there are input validation problems such as no issue IDs/keys were present, or more than 1000 issue IDs/keys were requested.

