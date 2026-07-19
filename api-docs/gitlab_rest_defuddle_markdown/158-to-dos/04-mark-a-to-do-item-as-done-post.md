# 04-Mark a to-do item as done [POST]

`POST /api/v4/todos/{id}/mark_as_done`

Marks a to-do item for the current user as done.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of to-do item |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "project": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
  },
  "group": {
    "id": integer,
    "name": string,
    "path": string,
    "kind": string,
    "full_path": string,
    "parent_id": integer,
    "avatar_url": string,
    "web_url": string,
  },
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
  "action_name": string,
  "target_type": string,
  "target": {},
  "target_url": string,
  "body": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

