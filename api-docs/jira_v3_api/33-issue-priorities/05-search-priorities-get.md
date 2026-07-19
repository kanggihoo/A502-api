# 05-Search priorities [GET]

`GET /rest/api/3/priority/search`

Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a subset determined by any combination of these criteria:

 *  a list of priority IDs. Any invalid priority IDs are ignored.
 *  a list of project IDs. Only priorities that are available in these projects will be returned. Any invalid project IDs are ignored.
 *  whether the field configuration is a default. This returns priorities from company-managed (classic) projects only, as there is no concept of default priorities in team-managed projects.

**Deprecation notice:** The `onlyDefault` parameter is deprecated and will be removed at a later date. See [CHANGE-1655](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1655).

**Deprecation notice:** The `isDefault` property of priorities is deprecated and will be removed at a later date. See [CHANGE-1655](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1655).

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `string` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `string` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No | The list of priority IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=2&id=3`. |
| `projectId` | `array` | `query` | No | The list of projects IDs. To include multiple IDs, provide an ampersand-separated list. For example, `projectId=10010&projectId=10111`. |
| `priorityName` | `string` | `query` | No | The name of priority to search for. |
| `onlyDefault` | `boolean` | `query` | No | Whether only the default priority is returned. |
| `expand` | `string` | `query` | No | Use `schemes` to return the associated priority schemes for each priority. Limited to returning first 15 priority schemes per priority. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":2,\"values\":[{\"description\":\"Major loss of function.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/priorities/major.png\",\"id\":\"1\",\"isDefault\":true,\"name\":\"Major\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/priority/3\",\"statusColor\":\"#009900\"},{\"description\":\"Very little impact.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/priorities/trivial.png\",\"id\":\"2\",\"isDefault\":false,\"name\":\"Trivial\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/priority/5\",\"statusColor\":\"#cfcfcf\"}]}"
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

