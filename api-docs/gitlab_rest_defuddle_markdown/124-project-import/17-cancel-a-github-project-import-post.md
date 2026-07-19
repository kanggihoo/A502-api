# 17-Cancel a GitHub project import [POST]

`POST /api/v4/import/github/cancel`

Cancels an in-progress import of a GitHub project to GitLab.

### Request Body (application/json)

```json
{
  "project_id": integer (required), // ID of importing project to be canceled
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "full_path": string,
  "full_name": string,
  "refs_url": string,
  "forked": boolean,
  "import_source": string,
  "import_status": string,
  "human_import_status_name": string,
  "provider_link": string,
  "import_error": string,
  "import_warning": string,
  "relation_type": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 503 - Service unavailable

