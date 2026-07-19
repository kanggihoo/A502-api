# 03-Delete a registered runner manager [DEL]

`DELETE /api/v4/runners/managers`

Delete a registered runner manager

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `token` | `string` | `query` | Yes | The runner's authentication token |
| `system_id` | `string` | `query` | Yes | The runner's system identifier. |

### Responses

#### 204 - Runner manager was deleted

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

