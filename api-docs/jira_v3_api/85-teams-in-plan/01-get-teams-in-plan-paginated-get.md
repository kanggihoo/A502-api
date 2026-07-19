# 01-Get teams in plan paginated [GET]

`GET /rest/api/3/plans/plan/{planId}/team`

Returns a [paginated](#pagination) list of plan-only and Atlassian teams in a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `planId` | `integer` | `path` | Yes | The ID of the plan. |
| `cursor` | `string` | `query` | No | The cursor to start from. If not provided, the first page will be returned. |
| `maxResults` | `integer` | `query` | No | The maximum number of plan teams to return per page. The maximum value is 50. The default value is 50. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"cursor\":\"\",\"isLast\":true,\"maxResults\":2,\"nextPageCursor\":\"2\",\"total\":10,\"values\":[{\"id\":\"1\",\"name\":\"Team 1\",\"type\":\"PlanOnly\"},{\"id\":\"2\",\"type\":\"Atlassian\"}]}"
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

#### 404 - Returned if the plan is not found.

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

