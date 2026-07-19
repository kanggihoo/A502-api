# 02-Get issue link [GET]

`GET /rest/api/3/issueLink/{linkId}`

Returns an issue link.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the linked issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `linkId` | `string` | `path` | Yes | The ID of the issue link. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"id\":\"10001\",\"inwardIssue\":{\"fields\":{\"issuetype\":{\"avatarId\":10002,\"description\":\"A problem with the software.\",\"entityId\":\"9d7dd6f7-e8b6-4247-954b-7b2c9b2a5ba2\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype\\\",\",\"id\":\"1\",\"name\":\"Bug\",\"scope\":{\"project\":{\"id\":\"10000\"},\"type\":\"PROJECT\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/1\",\"subtask\":false},\"priority\":{\"description\":\"Very little impact.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/priorities/trivial.png\",\"id\":\"2\",\"name\":\"Trivial\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/priority/5\",\"statusColor\":\"#cfcfcf\"},\"status\":{\"description\":\"The issue is closed.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/closed.gif\",\"id\":\"5\",\"name\":\"Closed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/5\",\"statusCategory\":{\"colorName\":\"green\",\"id\":9,\"key\":\"completed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/9\"}}},\"id\":\"10004\",\"key\":\"PR-3\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/PR-3\"},\"outwardIssue\":{\"fields\":{\"issuetype\":{\"avatarId\":1,\"description\":\"A task that needs to be done.\",\"hierarchyLevel\":0,\"iconUrl\":\"https://your-domain.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10299&avatarType=issuetype\\\",\",\"id\":\"3\",\"name\":\"Task\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueType/3\",\"subtask\":false},\"priority\":{\"description\":\"Major loss of function.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/priorities/major.png\",\"id\":\"1\",\"name\":\"Major\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/priority/3\",\"statusColor\":\"#009900\"},\"status\":{\"description\":\"The issue is currently being worked on.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/progress.gif\",\"id\":\"10000\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/10000\",\"statusCategory\":{\"colorName\":\"yellow\",\"id\":1,\"key\":\"in-flight\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/1\"}}},\"id\":\"10004L\",\"key\":\"PR-2\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issue/PR-2\"},\"type\":{\"id\":\"1000\",\"inward\":\"Duplicated by\",\"name\":\"Duplicate\",\"outward\":\"Duplicates\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/issueLinkType/1000\"}}"
```

#### 400 - Returned if the issue link ID is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if:

 *  issue linking is disabled.
 *  the issue link is not found.
 *  the user doesn't have the required permissions.

