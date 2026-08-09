# 02-Cancel task [POST]

`POST /rest/api/3/task/{taskId}/cancel`

Cancels a task.

**[Permissions](#permissions) required:** either of:

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  Creator of the task.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `taskId` | `string` | `path` | Yes | The ID of the task. |

### Responses

#### 202 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if cancellation of the task is not possible.

Schema (application/json):
```json
[
  string
]
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
[
  string
]
```

#### 403 - Returned if the user does not have the necessary permission.

Schema (application/json):
```json
[
  string
]
```

#### 404 - Returned if the task is not found.

Schema (application/json):
```json
[
  string
]
```

