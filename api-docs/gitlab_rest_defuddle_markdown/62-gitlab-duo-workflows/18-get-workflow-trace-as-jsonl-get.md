# 18-Get workflow trace as JSONL [GET]

`GET /api/v4/ai/duo_workflows/workflows/{workflow_id}/trace.jsonl`

Returns the full trace of a workflow session as JSON Lines (JSONL). Each line is a JSON object representing one checkpoint event in chronological order.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `workflow_id` | `integer` | `path` | Yes | The ID of the workflow |
| `full` | `boolean` | `query` | No | Include internal channels (conversation history, handover, etc). Restricted to the workflow owner; non-owners receive a 403. |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

