# 10-Get projects associated with a runner [GET]

`GET /api/v4/runners/{id}/projects`

Get a paginated list of all projects associated with the specified runner. Access is restricted based on user permissions.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of a runner |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

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

#### 403 - No access granted

#### 404 - Runner not found

