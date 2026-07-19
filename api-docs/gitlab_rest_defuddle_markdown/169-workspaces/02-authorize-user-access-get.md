# 02-authorize_user_access [GET]

`GET /api/v4/internal/agents/agentw/authorize_user_access`

Returns whether the user is authorized to access the workspace.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `workspace_host` | `string` | `query` | Yes | Host of the workspace being accessed |
| `user_id` | `integer` | `query` | Yes | User ID of the user accessing the workspace |

### Responses

#### 200 - User access authorization info retrieved successfully

#### 400 - Bad Request

