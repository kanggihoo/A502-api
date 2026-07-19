# 02-Create a new repository tag [POST]

`POST /api/v4/projects/{id}/repository/tags`

Create a new repository tag

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "tag_name": string (required), // The name of the tag
  "ref": string (required), // The commit sha or branch name
  "message": string, // Specifying a message creates an annotated tag
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "name": string,
  "message": string,
  "target": string,
  "commit": {
    "id": string,
    "short_id": string,
    "created_at": string,
    "parent_ids": [
      string
    ],
    "title": string,
    "message": string,
    "author_name": string,
    "author_email": string,
    "authored_date": string,
    "committer_name": string,
    "committer_email": string,
    "committed_date": string,
    "trailers": {},
    "extended_trailers": {},
    "web_url": string,
  },
  "release": {
    "tag_name": string,
    "description": string,
  },
  "protected": boolean,
  "created_at": string,
}
```

#### 400 - Bad request

#### 403 - Unauthenticated

#### 404 - Not found

