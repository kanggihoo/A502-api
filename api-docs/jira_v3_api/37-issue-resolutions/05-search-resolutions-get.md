# 05-Search resolutions [GET]

`GET /rest/api/3/resolution/search`

Returns a [paginated](#pagination) list of resolutions. The list can contain all resolutions or a subset determined by any combination of these criteria:

 *  a list of resolutions IDs.
 *  whether the field configuration is a default. This returns resolutions from company-managed (classic) projects only, as there is no concept of default resolutions in team-managed projects.

**[Permissions](#permissions) required:** Permission to access Jira.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `string` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `string` | `query` | No | The maximum number of items to return per page. |
| `id` | `array` | `query` | No | The list of resolutions IDs to be filtered out |
| `onlyDefault` | `boolean` | `query` | No | When set to true, return default only, when IDs provided, if none of them is default, return empty page. Default value is false |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":1,\"values\":[{\"description\":\"This is what it is supposed to do.\",\"id\":\"10001\",\"isDefault\":true,\"name\":\"Works as designed\"}]}"
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

