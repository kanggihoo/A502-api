# 03-Get plan [GET]

`GET /rest/api/3/plans/plan/{planId}`

Returns a plan.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `planId` | `integer` | `path` | Yes | The ID of the plan. |
| `useGroupId` | `boolean` | `query` | No | Whether to return group IDs instead of group names. Group names are deprecated. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"crossProjectReleases\":[{\"name\":\"x-plr\",\"releaseIds\":[345]}],\"customFields\":[{\"customFieldId\":34,\"filter\":false},{\"customFieldId\":39,\"filter\":true}],\"exclusionRules\":{\"issueIds\":[1,2],\"issueTypeIds\":[13,23],\"numberOfDaysToShowCompletedIssues\":50,\"releaseIds\":[14,24],\"workStatusCategoryIds\":[12,22],\"workStatusIds\":[11,21]},\"id\":23,\"issueSources\":[{\"type\":\"Project\",\"value\":12},{\"type\":\"Filter\",\"value\":10293}],\"lastSaved\":\"2024-10-03T10:15:30Z\",\"leadAccountId\":\"628f5e86d5ec1f006ne7363x2s\",\"name\":\"Onset TBJ Plan\",\"permissions\":[{\"holder\":{\"type\":\"AccountId\",\"value\":\"04jekw86d5jjje006ne7363x2s\"},\"type\":\"Edit\"}],\"scheduling\":{\"dependencies\":\"Concurrent\",\"endDate\":{\"dateCustomFieldId\":1098,\"type\":\"DateCustomField\"},\"estimation\":\"Hours\",\"inferredDates\":\"ReleaseDates\",\"startDate\":{\"type\":\"TargetStartDate\"}},\"status\":\"Active\"}"
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

