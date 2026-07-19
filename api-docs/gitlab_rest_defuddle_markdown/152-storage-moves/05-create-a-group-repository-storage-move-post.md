# 05-Create a group repository storage move [POST]

`POST /api/v4/groups/{id}/repository_storage_moves`

Creates a group repository storage move for a specified group. This operation moves only group wiki repositories and does not move repositories for projects in a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

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
  "group": {
    "id": integer,
    "web_url": string,
    "name": string,
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

