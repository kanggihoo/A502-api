# 05-Retrieve a group or project migration [GET]

`GET /api/v4/bulk_imports/{import_id}`

Retrieves details of a group or project migration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `import_id` | `integer` | `path` | Yes | The ID of user's GitLab Migration |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "status": string,
  "source_type": string,
  "source_url": string,
  "created_at": string,
  "updated_at": string,
  "has_failures": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

#### 503 - Service unavailable

