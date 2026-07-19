# 01-Get issue security level members by issue security scheme [GET]

`GET /rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members`

Returns issue security level members.

Only issue security level members in context of classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueSecuritySchemeId` | `integer` | `path` | Yes | The ID of the issue security scheme. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) operation to get a list of issue security scheme IDs. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `issueSecurityLevelId` | `array` | `query` | No | The list of issue security level IDs. To include multiple issue security levels separate IDs with ampersand: `issueSecurityLevelId=10000&issueSecurityLevelId=10001`. |
| `expand` | `string` | `query` | No | Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `all` Returns all expandable information.<br> *  `field` Returns information about the custom field granted the permission.<br> *  `group` Returns information about the group that is granted the permission.<br> *  `projectRole` Returns information about the project role granted the permission.<br> *  `user` Returns information about the user who is granted the permission. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":100,\"startAt\":0,\"total\":3,\"values\":[{\"id\":10000,\"issueSecurityLevelId\":10020,\"holder\":{\"expand\":\"user\",\"type\":\"user\",\"user\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":true,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"}}},{\"id\":10001,\"issueSecurityLevelId\":10020,\"holder\":{\"expand\":\"group\",\"parameter\":\"jira-core-users\",\"type\":\"group\",\"value\":\"9c559b11-6c5d-4f96-992c-a746cabab28b\"}},{\"id\":10002,\"issueSecurityLevelId\":10021,\"holder\":{\"type\":\"assignee\"}}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if no issue security level members are found.

