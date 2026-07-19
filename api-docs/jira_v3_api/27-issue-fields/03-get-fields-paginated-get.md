# 03-Get fields paginated [GET]

`GET /rest/api/3/field/search`

Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:

 *  all fields
 *  specific fields, by defining `id`
 *  fields that contain a string in the field name or description, by defining `query`
 *  specific fields that contain a string in the field name or description, by defining `id` and `query`

Use `type` must be set to `custom` to show custom fields only.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `type` | `array` | `query` | No | The type of fields to search. |
| `id` | `array` | `query` | No | The IDs of the custom fields to return or, where `query` is specified, filter. |
| `query` | `string` | `query` | No | String used to perform a case-insensitive partial match with field names or descriptions. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by:<br><br> *  `contextsCount` sorts by the number of contexts related to a field<br> *  `lastUsed` sorts by the date when the value of the field last changed<br> *  `name` sorts by the field name<br> *  `screensCount` sorts by the number of screens related to a field |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `key` returns the key for each field<br> *  `stableId` returns the stableId for each field<br> *  `lastUsed` returns the date when the value of the field last changed<br> *  `screensCount` returns the number of screens related to a field<br> *  `contextsCount` returns the number of contexts related to a field<br> *  `isLocked` returns information about whether the field is locked<br> *  `searcherKey` returns the searcher key for each custom field |
| `projectIds` | `array` | `query` | No | The IDs of the projects to filter the fields by. Fields belonging to project Ids that the user does not have access to will not be returned |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":50,\"startAt\":0,\"total\":2,\"values\":[{\"id\":\"customfield_10000\",\"name\":\"Approvers\",\"schema\":{\"custom\":\"com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker\",\"customId\":10000,\"items\":\"user\",\"type\":\"array\"},\"description\":\"Contains users needed for approval. This custom field was created by Jira Service Desk.\",\"key\":\"customfield_10000\",\"stableId\":\"sfid:approvers\",\"isLocked\":true,\"searcherKey\":\"com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher\",\"screensCount\":2,\"contextsCount\":2,\"lastUsed\":{\"type\":\"TRACKED\",\"value\":\"2021-01-28T07:37:40.000+0000\"}},{\"id\":\"customfield_10001\",\"name\":\"Change reason\",\"schema\":{\"custom\":\"com.atlassian.jira.plugin.system.customfieldtypes:select\",\"customId\":10001,\"type\":\"option\"},\"description\":\"Choose the reason for the change request\",\"key\":\"customfield_10001\",\"stableId\":\"sfid:change-reason\",\"isLocked\":false,\"searcherKey\":\"com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher\",\"screensCount\":2,\"contextsCount\":2,\"projectsCount\":2,\"lastUsed\":{\"type\":\"NOT_TRACKED\"}}]}"
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

