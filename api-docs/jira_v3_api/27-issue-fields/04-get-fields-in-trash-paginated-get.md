# 04-Get fields in trash paginated [GET]

`GET /rest/api/3/field/search/trashed`

Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields whose field name or description partially match a string.

Only custom fields can be queried, `type` must be set to `custom`.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No |  |
| `query` | `string` | `query` | No | String used to perform a case-insensitive partial match with field names or descriptions. |
| `expand` | `string` | `query` | No |  |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `name` sorts by the field name<br> *  `trashDate` sorts by the date the field was moved to the trash<br> *  `plannedDeletionDate` sorts by the planned deletion date |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":50,\"startAt\":0,\"total\":1,\"values\":[{\"id\":\"customfield_10000\",\"name\":\"Approvers\",\"schema\":{\"custom\":\"com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker\",\"customId\":10003,\"type\":\"array\"},\"description\":\"Contains users needed for approval. This custom field was created by Jira Service Desk.\",\"key\":\"customfield_10003\",\"trashedDate\":\"2022-10-06T07:32:47.000+0000\",\"trashedBy\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":true,\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"plannedDeletionDate\":\"2022-10-24T07:32:47.000+0000\"}]}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"Only custom fields can be queried.\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access fields.\"],\"errors\":{}}"
```

