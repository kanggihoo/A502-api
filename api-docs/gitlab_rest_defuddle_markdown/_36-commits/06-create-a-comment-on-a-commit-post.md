# 06-Create a comment on a commit [POST]

`POST /api/v4/projects/{id}/repository/commits/{sha}/comments`

Creates a comment on a commit. To comment on a specific line in a file, specify the full commit SHA, `path`, `line`, and set `line_type` to `new`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `path` | Yes | A commit sha, or the name of a branch or tag on which to post a comment |

### Request Body (application/json)

```json
{
  "note": string (required), // The text of the comment
  "path": string, // The file path
  "line": integer (required), // The line number
  "line_type": enum("new" | "old") (required), // The type of the line
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "note": string,
  "path": string,
  "line": integer,
  "line_type": string,
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
}
```

#### 400 - Bad request

#### 404 - Not found

