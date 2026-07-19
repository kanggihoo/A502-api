# 06-List all workflow checkpoints [GET]

`GET /api/v4/ai/duo_workflows/workflows/{id}/checkpoints`

List all workflow checkpoints

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `accept_compressed` | `boolean` | `query` | No | Return compressed checkpoints |
| `id` | `integer` | `path` | Yes | The ID of the workflow |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

