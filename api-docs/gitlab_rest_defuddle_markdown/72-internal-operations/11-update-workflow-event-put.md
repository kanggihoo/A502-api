# 11-Update workflow event [PUT]

`PUT /api/v4/ai/duo_workflows/workflows/{id}/events/{event_id}`

Update workflow event

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow |
| `event_id` | `integer` | `path` | Yes | The ID of the event |

### Request Body (application/json)

```json
{
  "event_status": enum("queued" | "delivered") (required), // The status of the event
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

