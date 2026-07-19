# 15-Retrieve the status of an relations export for a project [GET]

`GET /api/v4/projects/{id}/export_relations/status`

Retrieves the status of a relations export for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `relation` | `string` | `query` | No | Project relation name |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "relation": string,
  "status": string,
  "error": string,
  "updated_at": string,
  "batched": boolean,
  "batches_count": integer,
  "total_objects_count": integer,
  "batches": {
    "status": string,
    "batch_number": integer,
    "objects_count": integer,
    "error": string,
    "updated_at": string,
  },
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 503 - Service unavailable

