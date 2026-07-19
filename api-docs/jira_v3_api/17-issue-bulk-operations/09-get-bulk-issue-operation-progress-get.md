# 09-Get bulk issue operation progress [GET]

`GET /rest/api/3/bulk/queue/{taskId}`

Use this to get the progress state for the specified bulk operation `taskId`.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).

If the task is running, this resource will return:

    {"taskId":"10779","status":"RUNNING","progressPercent":65,"submittedBy":{"accountId":"5b10a2844c20165700ede21g"},"created":1690180055963,"started":1690180056206,"updated":169018005829}

If the task has completed, then this resource will return:

    {"processedAccessibleIssues":[10001,10002],"created":1709189449954,"progressPercent":100,"started":1709189450154,"status":"COMPLETE","submittedBy":{"accountId":"5b10a2844c20165700ede21g"},"invalidOrInaccessibleIssueCount":0,"taskId":"10000","totalIssueCount":2,"updated":1709189450354}

**Note:** You can view task progress for up to 14 days from creation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `taskId` | `string` | `path` | Yes | The ID of the task. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"created\":1704110400000,\"invalidOrInaccessibleIssueCount\":0,\"processedAccessibleIssues\":[10001,10002],\"progressPercent\":100,\"started\":1704110460000,\"status\":\"COMPLETE\",\"submittedBy\":{\"accountId\":\"5b10a2844c20165700ede21g\"},\"taskId\":\"10000\",\"totalIssueCount\":2,\"updated\":1704110520000}"
```

#### 400 - Returned if the request is invalid.

Example (application/json):
```json
"{\"errorMessages\":[\"The task associated with this taskId is not a bulk operation task\"],\"errors\":{},\"httpStatusCode\":{\"empty\":false,\"present\":true}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errors": [
    {
      "message": string,
    }
  ],
}
```

