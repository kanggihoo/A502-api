# 06-List all group or project migration entities [GET]

`GET /api/v4/bulk_imports/{import_id}/entities`

Lists all group or project migration entities for a specified migration.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `import_id` | `integer` | `path` | Yes | The ID of user's GitLab Migration |
| `status` | `string` | `query` | No | Return import entities with specified status |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

