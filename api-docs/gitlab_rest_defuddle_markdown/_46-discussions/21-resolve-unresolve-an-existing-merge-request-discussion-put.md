# 21-Resolve/unresolve an existing merge request discussion [PUT]

`PUT /api/v4/projects/{id}/merge_requests/{noteable_id}/discussions/{discussion_id}`

Resolve/unresolve an existing merge request discussion

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `noteable_id` | `integer` | `path` | Yes | The ID of the merge request |
| `discussion_id` | `string` | `path` | Yes | The ID of a discussion |

### Request Body (application/json)

```json
{
  "resolved": boolean (required), // Mark discussion resolved/unresolved
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "individual_note": boolean,
  "resolvable": boolean,
  "resolved": boolean,
  "notes": {
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
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

