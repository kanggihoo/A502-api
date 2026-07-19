# 09-Update an existing merge request note [PUT]

`PUT /api/v4/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}`

Update an existing merge request note

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `noteable_id` | `integer` | `path` | Yes | The ID of the noteable |
| `note_id` | `integer` | `path` | Yes | The ID of a note |

### Request Body (application/json)

```json
{
  "body": string, // The content of a note
  "confidential": boolean, // [Deprecated in 14.10] No longer allowed to update confidentiality of notes
}
```
### Responses

#### 200 - OK

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

