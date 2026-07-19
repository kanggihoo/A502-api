# 04-Add a project to a CI/CD job token allowlist [POST]

`POST /api/v4/projects/{id}/job_token_scope/allowlist`

Adds a project to the CI/CD job token allowlist of a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of user project |

### Request Body (application/json)

```json
{
  "target_project_id": integer (required), // ID of target project
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
  "default_branch": string,
  "tag_list": [
    string
  ],
  "topics": [
    string
  ],
  "ssh_url_to_repo": string,
  "http_url_to_repo": string,
  "web_url": string,
  "readme_url": string,
  "forks_count": integer,
  "license_url": string,
  "license": {
    "key": string,
    "name": string,
    "nickname": string,
    "html_url": string,
    "source_url": string,
  },
  "avatar_url": string,
  "star_count": integer,
  "last_activity_at": string,
  "visibility": string,
  "namespace": {
    "id": integer,
    "name": string,
    "path": string,
    "kind": string,
    "full_path": string,
    "parent_id": integer,
    "avatar_url": string,
    "web_url": string,
  },
  "custom_attributes": {
    "key": string,
    "value": string,
  },
  "repository_storage": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

