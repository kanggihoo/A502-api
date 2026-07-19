# 16-Import a repository from GitHub [POST]

`POST /api/v4/import/github`

Imports a repository from GitHub to GitLab.

### Request Body (application/json)

```json
{
  "personal_access_token": string (required), // GitHub personal access token
  "repo_id": integer (required), // GitHub repository ID
  "new_name": string, // New repo name
  "target_namespace": string (required), // Namespace or group to import repository into
  "github_hostname": string, // Custom GitHub enterprise hostname. For example: https://github.example.com. From GitLab 16.5 to GitLab 17.1, you must include the path `/api/v3`.
  "optional_stages": {}, // Optional stages of import to be performed
  "timeout_strategy": enum("optimistic" | "pessimistic"), // Strategy for behavior on timeouts
  "pagination_limit": integer, // Pagination limit
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
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable entity

#### 503 - Service unavailable

