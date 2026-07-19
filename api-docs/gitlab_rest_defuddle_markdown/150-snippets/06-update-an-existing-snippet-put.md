# 06-Update an existing snippet [PUT]

`PUT /api/v4/snippets/{id}`

This feature was introduced in GitLab 8.15.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of a snippet |

### Request Body (application/json)

```json
{
  "content": string, // The content of a snippet
  "description": string, // The description of a snippet
  "file_name": string, // The name of a snippet file
  "title": string, // The title of a snippet
  "visibility": enum("private" | "internal" | "public"), // The visibility of the snippet
  "files": [
    {
      "action": enum("create" | "update" | "delete" | "move") (required), // The type of action to perform on the file, must be one of: create, update, delete, move
      "content": string, // The content of a snippet
      "file_path": string, // The file path of a snippet file
      "previous_path": string, // The previous path of a snippet file
    }
  ], // An array of files to update
}
```
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

#### 400 - Validation error

#### 404 - Not found

#### 422 - Unprocessable entity

