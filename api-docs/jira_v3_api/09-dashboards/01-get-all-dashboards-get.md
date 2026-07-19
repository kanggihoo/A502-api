# 01-Get all dashboards [GET]

`GET /rest/api/3/dashboard`

Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `filter` | `string` | `query` | No | The filter applied to the list of dashboards. Valid values are:<br><br> *  `favourite` Returns dashboards the user has marked as favorite.<br> *  `my` Returns dashboards owned by the user. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"dashboards\":[{\"id\":\"10000\",\"isFavourite\":false,\"name\":\"System Dashboard\",\"popularity\":1,\"self\":\"https://your-domain.atlassian.net/rest/api/3/dashboard/10000\",\"sharePermissions\":[{\"type\":\"global\"}],\"view\":\"https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=10000\"},{\"id\":\"20000\",\"isFavourite\":true,\"name\":\"Build Engineering\",\"owner\":{\"key\":\"Mia\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"name\":\"mia\",\"displayName\":\"Mia Krystof\",\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"}},\"popularity\":1,\"self\":\"https://your-domain.atlassian.net/rest/api/3/dashboard/20000\",\"sharePermissions\":[{\"group\":{\"name\":\"administrators\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupname=administrators\"},\"id\":10105,\"type\":\"group\"}],\"view\":\"https://your-domain.atlassian.net/secure/Dashboard.jspa?selectPageId=20000\"}],\"maxResults\":10,\"next\":\"https://your-domain.atlassian.net/rest/api/3/dashboard?startAt=10\",\"prev\":\"https://your-domain.atlassian.net/rest/api/3/dashboard?startAt=0\",\"startAt\":10,\"total\":143}"
```

#### 400 - Returned if the request is invalid.

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

#### 401 - Returned if the authentication credentials are incorrect or missing.

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

