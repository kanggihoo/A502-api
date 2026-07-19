# 18-Import repository from Bitbucket Server [POST]

`POST /api/v4/import/bitbucket_server`

Imports a repository from Bitbucket Server to GitLab. The Bitbucket Project Key is only used for finding the repository in Bitbucket. You must specify a `target_namespace` if you want to import the repository to a GitLab group.

### Request Body (application/json)

```json
{
  "bitbucket_server_url": string (required), // Bitbucket Server URL
  "bitbucket_server_username": string (required), // BitBucket Server Username
  "personal_access_token": string (required), // BitBucket Server personal access token/password
  "bitbucket_server_project": string (required), // BitBucket Server Project Key
  "bitbucket_server_repo": string (required), // BitBucket Server Repository Name
  "new_name": string, // New repo name
  "new_namespace": string, // Namespace to import repo into
  "timeout_strategy": enum("optimistic" | "pessimistic"), // Strategy for behavior on timeouts
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

