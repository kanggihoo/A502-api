# 17-Get Duo Workflows WebSocket connection details [GET]

`GET /api/v4/ai/duo_workflows/ws`

Get Duo Workflows WebSocket connection details

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `workflow_id` | `string` | `query` | No | The ID of an existing workflow. When provided and the workflow has a stored model selection, that selection is reused to ensure provider stickiness. |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

