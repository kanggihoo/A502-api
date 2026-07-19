# 04-Update the workflow status [PATCH]

`PATCH /api/v4/ai/duo_workflows/workflows/{id}`

Update the workflow status

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow |

### Request Body (application/json)

```json
{
  "status_event": string (required), // The status event
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

