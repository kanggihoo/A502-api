# 19-Import repository from Bitbucket Cloud [POST]

`POST /api/v4/import/bitbucket`

Imports a repository from Bitbucket Cloud to GitLab. Prerequisites: - The prerequisites for Bitbucket Cloud importer. This feature was introduced in GitLab 17.0.

### Request Body (application/json)

```json
{
  "bitbucket_email": string (required), // BitBucket email
  "bitbucket_api_token": string (required), // BitBucket API token
  "repo_path": string (required), // Repository path
  "target_namespace": string (required), // Target namespace
  "new_name": string, // New repository name
}
```
### Responses

#### 201 - Created

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

#### 422 - Unprocessable entity

#### 503 - Service unavailable

