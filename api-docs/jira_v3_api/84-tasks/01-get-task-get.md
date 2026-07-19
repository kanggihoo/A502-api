# 01-Get task [GET]

`GET /rest/api/3/task/{taskId}`

Returns the status of a [long-running asynchronous task](#async).

When a task has finished, this operation returns the JSON blob applicable to the task. See the documentation of the operation that created the task for details. Task details are not permanently retained. As of September 2019, details are retained for 14 days although this period may change without notice.

**Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

 *  `read:jira-work`

**[Permissions](#permissions) required:** either of:

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  Creator of the task.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `taskId` | `string` | `path` | Yes | The ID of the task. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"self\":\"https://your-domain.atlassian.net/rest/api/3/task/1\",\"id\":\"1\",\"description\":\"Task description\",\"status\":\"COMPLETE\",\"result\":\"the task result, this may be any JSON\",\"submittedBy\":10000,\"progress\":100,\"elapsedRuntime\":156,\"submitted\":1501708132800,\"started\":1501708132900,\"finished\":1501708133000,\"lastUpdate\":1501708133000}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the task is not found.

