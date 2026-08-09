# 11-Get issue limit report [GET]

`GET /rest/api/3/issue/limit/report`

Returns all issues breaching and approaching per-issue limits.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) is required for the project the issues are in. Results may be incomplete otherwise
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `isReturningKeys` | `boolean` | `query` | No | Return issue keys instead of issue ids in the response.<br><br>Usage: Add `?isReturningKeys=true` to the end of the path to request issue keys. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"issuesApproachingLimit\":{\"attachment\":{\"15070L\":1822,\"15111L\":1999},\"comment\":{\"10000L\":4997,\"15073L\":4999,\"15110L\":5000},\"remoteIssueLinks\":{\"15107L\":2000},\"worklog\":{\"15101L\":10342}},\"issuesBreachingLimit\":{\"attachment\":{\"15057L\":2005,\"15116L\":2065,\"15117L\":3005},\"comment\":{\"15055L\":5202},\"issuelinks\":{\"15058L\":2120},\"remoteIssueLinks\":{\"15059L\":2094},\"worklog\":{\"15056L\":10085,\"15169L\":120864}},\"limits\":{\"attachment\":2000,\"comment\":5000,\"issuelinks\":2000,\"remoteIssueLinks\":2000,\"worklog\":10000}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to complete this request.

