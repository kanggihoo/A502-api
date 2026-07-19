# 08-List all failed import records for a migration entity [GET]

`GET /api/v4/bulk_imports/{import_id}/entities/{entity_id}/failures`

Lists all failed import records for a group or project migration entity. This feature was introduced in GitLab 16.6.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `import_id` | `integer` | `path` | Yes | The ID of user's GitLab Migration |
| `entity_id` | `integer` | `path` | Yes | The ID of GitLab Migration entity |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "relation": string,
  "exception_message": string,
  "exception_class": string,
  "correlation_id_value": string,
  "source_url": string,
  "source_title": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

#### 503 - Service unavailable

