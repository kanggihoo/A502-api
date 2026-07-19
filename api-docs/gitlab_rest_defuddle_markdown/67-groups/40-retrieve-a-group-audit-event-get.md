# 40-Retrieve a group audit event [GET]

`GET /api/v4/groups/{id}/audit_events/{audit_event_id}`

Retrieves an audit event for a specified group. Only available to group Owners and administrators.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `audit_event_id` | `integer` | `path` | Yes | The ID of the audit event |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

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

