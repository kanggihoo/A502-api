# 01-Get plans paginated [GET]

`GET /rest/api/3/plans/plan`

Returns a [paginated](#pagination) list of plans.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `includeTrashed` | `boolean` | `query` | No | Whether to include trashed plans in the results. |
| `includeArchived` | `boolean` | `query` | No | Whether to include archived plans in the results. |
| `cursor` | `string` | `query` | No | The cursor to start from. If not provided, the first page will be returned. |
| `maxResults` | `integer` | `query` | No | The maximum number of plans to return per page. The maximum value is 50. The default value is 50. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"cursor\":\"\",\"isLast\":true,\"maxResults\":2,\"nextPageCursor\":\"2\",\"total\":10,\"values\":[{\"id\":\"100\",\"issueSources\":[{\"type\":\"Project\",\"value\":10000}],\"name\":\"Plan 1\",\"scenarioId\":\"200\",\"status\":\"Active\"},{\"id\":\"200\",\"issueSources\":[{\"type\":\"Board\",\"value\":20000}],\"name\":\"Plan 2\",\"scenarioId\":\"300\",\"status\":\"Trashed\"}]}"
```

#### 401 - Returned if the user is not logged in.

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

#### 403 - Returned if the site has no premium edition of Jira or if the user does not have the Administer Jira global permission.

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

