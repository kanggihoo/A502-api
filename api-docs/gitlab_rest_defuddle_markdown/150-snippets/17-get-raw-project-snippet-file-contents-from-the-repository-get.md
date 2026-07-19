# 17-Get raw project snippet file contents from the repository [GET]

`GET /api/v4/projects/{id}/snippets/{snippet_id}/files/{ref}/{file_path}/raw`

Get raw project snippet file contents from the repository

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `file_path` | `string` | `path` | Yes | The URL-encoded path to the file, like lib%2Fclass%2Erb |
| `ref` | `string` | `path` | Yes | The name of branch, tag or commit |
| `snippet_id` | `integer` | `path` | Yes | The ID of a project snippet |

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

