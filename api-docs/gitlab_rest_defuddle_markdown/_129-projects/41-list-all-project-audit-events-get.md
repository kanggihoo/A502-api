# 41-List all project audit events [GET]

`GET /api/v4/projects/{id}/audit_events`

Lists all audit events for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `created_after` | `string` | `query` | No | Return audit events created after the specified time |
| `created_before` | `string` | `query` | No | Return audit events created before the specified time |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

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

