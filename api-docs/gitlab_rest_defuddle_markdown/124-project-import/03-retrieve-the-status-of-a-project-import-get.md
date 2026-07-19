# 03-Retrieve the status of a project import [GET]

`GET /api/v4/projects/{id}/import`

Retrieves the status of the most recent import for a specified project.

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
  "import_status": string,
  "import_type": string,
  "correlation_id": string,
  "failed_relations": [
    {
      "id": integer,
      "created_at": string,
      "exception_class": string,
      "source": string,
      "exception_message": string,
      "relation_name": string,
      "line_number": integer,
    }
  ],
  "import_error": string,
  "stats": {},
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 503 - Service unavailable

