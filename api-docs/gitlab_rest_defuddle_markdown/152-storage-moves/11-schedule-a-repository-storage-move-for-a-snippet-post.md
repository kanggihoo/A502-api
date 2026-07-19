# 11-Schedule a repository storage move for a snippet [POST]

`POST /api/v4/snippets/{id}/repository_storage_moves`

Schedules a repository storage move for a specified snippet.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a snippet |

### Request Body (application/json)

```json
{
  "destination_storage_name": string, // The destination storage shard
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "created_at": string,
  "state": string,
  "source_storage_name": string,
  "destination_storage_name": string,
  "error_message": string,
  "snippet": {
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
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

