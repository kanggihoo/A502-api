# 34-Delete a comment in a commit discussion [DEL]

`DELETE /api/v4/projects/{id}/repository/commits/{noteable_id}/discussions/{discussion_id}/notes/{note_id}`

Delete a comment in a commit discussion

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `noteable_id` | `string` | `path` | Yes | The ID of the commit |
| `discussion_id` | `string` | `path` | Yes | The ID of a discussion |
| `note_id` | `integer` | `path` | Yes | The ID of a note |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "type": string,
  "body": string,
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
  "system": boolean,
  "noteable_id": integer,
  "noteable_type": string,
  "project_id": integer,
  "commit_id": string,
  "position": {},
  "resolvable": boolean,
  "resolved": boolean,
  "resolved_by": {
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
  "resolved_at": string,
  "suggestions": {
    "id": integer,
    "from_line": integer,
    "to_line": integer,
    "appliable": boolean,
    "applied": boolean,
    "from_content": string,
    "to_content": string,
  },
  "confidential": boolean,
  "internal": boolean,
  "imported": boolean,
  "imported_from": string,
  "noteable_iid": integer,
  "commands_changes": {},
}
```

#### 400 - Bad Request

#### 404 - Not Found

