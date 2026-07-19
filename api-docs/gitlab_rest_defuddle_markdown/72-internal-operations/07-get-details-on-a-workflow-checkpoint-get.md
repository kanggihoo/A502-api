# 07-Get details on a workflow checkpoint [GET]

`GET /api/v4/ai/duo_workflows/workflows/{id}/checkpoints/{checkpoint_id}`

Get details on a workflow checkpoint

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `checkpoint_id` | `integer` | `path` | Yes | The ID of the checkpoint |
| `accept_compressed` | `boolean` | `query` | No | Return compressed checkpoint |
| `id` | `integer` | `path` | Yes | The ID of the workflow |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

