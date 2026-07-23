# 09-List all projects contributions for a user [GET]

`GET /api/v4/users/{user_id}/contributed_projects`

Lists all contributions to visible projects for a specified user. Returns only contributions in the past year.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID or username of the user |
| `order_by` | `string` | `query` | No | Return projects ordered by field. storage_size, repository_size, wiki_size, packages_size are only available to admins. Similarity is available when searching and is limited to projects the user has access to. |
| `sort` | `string` | `query` | No | Return projects sorted in ascending and descending order |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `simple` | `boolean` | `query` | No | Return only the ID, URL, name, and path of each project |

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

#### 404 - 404 User Not Found

