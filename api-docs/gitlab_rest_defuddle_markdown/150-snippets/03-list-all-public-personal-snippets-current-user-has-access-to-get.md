# 03-List all public personal snippets current_user has access to [GET]

`GET /api/v4/snippets/public`

This feature was introduced in GitLab 8.15.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `created_after` | `string` | `query` | No | Return snippets created after the specified time |
| `created_before` | `string` | `query` | No | Return snippets created before the specified time |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "title": string,
  "description": string,
  "visibility": string,
  "author": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
    "state": string,
    "locked": boolean,
    "avatar_url": string,
    "avatar_path": string,
    "custom_attributes": [
      {
        "key": string,
        "value": string,
      }
    ],
    "web_url": string,
  },
  "created_at": string,
  "updated_at": string,
  "project_id": integer,
  "web_url": string,
  "raw_url": string,
  "ssh_url_to_repo": string,
  "http_url_to_repo": string,
  "file_name": string,
  "files": [
    {}
  ],
  "imported": boolean,
  "imported_from": string,
  "repository_storage": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

