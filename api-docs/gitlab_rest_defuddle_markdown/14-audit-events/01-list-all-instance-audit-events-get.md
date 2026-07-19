# 01-List all instance audit events [GET]

`GET /api/v4/audit_events`

Lists all available instance audit events, limited to a maximum of 30 days for each query.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `entity_type` | `string` | `query` | Yes | Return audit events for the specified entity type |
| `entity_id` | `integer` | `query` | No | Return audit events for the specified entity ID. If defined, the request must also include the `entity_type` attribute. |
| `created_after` | `string` | `query` | No | Return audit events created after the specified time |
| `created_before` | `string` | `query` | No | Return audit events created before the specified time |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

