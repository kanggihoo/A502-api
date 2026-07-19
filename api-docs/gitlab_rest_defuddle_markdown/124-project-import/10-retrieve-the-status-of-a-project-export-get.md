# 10-Retrieve the status of a project export [GET]

`GET /api/v4/projects/{id}/export`

Retrieves the status of the most recent export for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "name": string,
  "name_with_namespace": string,
  "path": string,
  "path_with_namespace": string,
  "created_at": string,
  "export_status": string,
  "_links": {},
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 503 - Service unavailable

