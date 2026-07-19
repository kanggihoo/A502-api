# 05-Delete a broadcast message [DEL]

`DELETE /api/v4/broadcast_messages/{id}`

Deletes a specified broadcast message.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Broadcast message ID |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "message": string,
  "starts_at": string,
  "ends_at": string,
  "color": string,
  "font": string,
  "target_access_levels": [
    any
  ],
  "target_path": string,
  "broadcast_type": string,
  "theme": string,
  "dismissable": boolean,
  "active": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

