# 07-Retrieve a group or project migration entity [GET]

`GET /api/v4/bulk_imports/{import_id}/entities/{entity_id}`

Retrieves details of a group or project migration entity.

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
  "id": integer,
  "bulk_import_id": integer,
  "status": string,
  "entity_type": string,
  "source_full_path": string,
  "destination_full_path": string,
  "destination_name": string,
  "destination_slug": string,
  "destination_namespace": string,
  "parent_id": integer,
  "namespace_id": integer,
  "project_id": integer,
  "created_at": string,
  "updated_at": string,
  "failures": [
    {
      "relation": string,
      "exception_message": string,
      "exception_class": string,
      "correlation_id_value": string,
      "source_url": string,
      "source_title": string,
    }
  ],
  "migrate_projects": boolean,
  "migrate_memberships": boolean,
  "has_failures": boolean,
  "stats": {},
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

#### 503 - Service unavailable

