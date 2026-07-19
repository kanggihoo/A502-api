# 12-Create a new project snippet [POST]

`POST /api/v4/projects/{id}/snippets`

Create a new project snippet

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "title": string (required), // The title of the snippet
  "description": string, // The description of a snippet
  "visibility": enum("private" | "internal" | "public") (required), // The visibility of the snippet
  "files": [
    {
      "file_path": string (required), // The path of a snippet file
      "content": string (required), // The content of a snippet file
    }
  ], // An array of files
  "content": string, // The content of a snippet
  "file_name": string (required), // The name of a snippet file
}
```
### Responses

#### 201 - Created

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

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

