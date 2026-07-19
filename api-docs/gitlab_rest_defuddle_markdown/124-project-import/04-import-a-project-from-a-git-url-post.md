# 04-Import a project from a Git URL [POST]

`POST /api/v4/projects/{id}/import/git`

This feature was introduced in GitLab 18.10.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "import_url": string (required), // The URL from which the project is imported
  "import_url_user": string, // Username for the import URL
  "import_url_password": string, // Password for the import URL
}
```
### Responses

#### 201 - Created

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

#### 409 - Conflict

#### 422 - Unprocessable Entity

