# 02-Retrieve an instance audit event [GET]

`GET /api/v4/audit_events/{id}`

Retrieves a specified instance audit event.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of audit event |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "author_id": integer,
  "entity_id": integer,
  "entity_type": string,
  "event_name": string,
  "details": {},
  "created_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

