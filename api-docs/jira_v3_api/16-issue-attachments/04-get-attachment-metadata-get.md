# 04-Get attachment metadata [GET]

`GET /rest/api/3/attachment/{id}`

Returns the metadata for an attachment. Note that the attachment itself is not returned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If attachments are added in private comments, the comment-level restriction will be applied.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the attachment. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"author\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":false,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"},\"content\":\"https://your-domain.atlassian.net/jira/rest/api/3/attachment/content/10000\",\"created\":\"2022-10-06T07:32:47.000+0000\",\"filename\":\"picture.jpg\",\"id\":10000,\"mimeType\":\"image/jpeg\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/attachments/10000\",\"size\":23123,\"thumbnail\":\"https://your-domain.atlassian.net/jira/rest/api/3/attachment/thumbnail/10000\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if:

 *  the attachment is not found.
 *  attachments are disabled in the Jira settings.

