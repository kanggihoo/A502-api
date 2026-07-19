# 02-Start a group or project migration [POST]

`POST /api/v4/bulk_imports`

Starts a group or project migration. To migrate a project, specify `entities[project_entity]`.

### Request Body (application/x-www-form-urlencoded)

```json
{
  "configuration": {
    "url": string (required), // Source GitLab instance URL
    "access_token": string (required), // Access token to the source GitLab instance
  } (required), // The source GitLab instance configuration
  "entities": [
    {
      "source_type": enum("group_entity" | "project_entity") (required), // Source entity type
      "source_full_path": string (required), // Relative path of the source entity to import
      "destination_namespace": string (required), // Destination namespace for the entity
      "destination_slug": string, // Destination slug for the entity
      "destination_name": string, // Deprecated: Use :destination_slug instead. Destination slug for the entity
      "migrate_projects": boolean, // Indicates group migration should include nested projects
      "migrate_memberships": boolean, // The option to migrate memberships or not
    }
  ] (required), // List of entities to import
}
```
### Responses

#### 201 - Created

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

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

#### 422 - Unprocessable entity

#### 503 - Service unavailable

