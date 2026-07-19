# 06-Get current user [GET]

`GET /rest/api/3/myself`

Returns details for the current user.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about user in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `groups` Returns all groups, including nested groups, the user belongs to.<br> *  `applicationRoles` Returns the application roles the user is assigned to. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":true,\"applicationRoles\":{\"items\":[],\"size\":1},\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"groups\":{\"items\":[],\"size\":3},\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

