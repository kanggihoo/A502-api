# 19-Create a new merge request discussion [POST]

`POST /api/v4/projects/{id}/merge_requests/{noteable_id}/discussions`

Create a new merge request discussion

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `noteable_id` | `integer` | `path` | Yes | The ID of the merge request |

### Request Body (application/json)

```json
{
  "body": string (required), // The content of a note
  "created_at": string, // The creation date of the note
  "position": {
    "base_sha": string (required), // Base commit SHA in the source branch
    "start_sha": string (required), // SHA referencing commit in target branch
    "head_sha": string (required), // SHA referencing HEAD of this merge request
    "position_type": enum("text" | "image" | "file") (required), // Type of the position reference
    "new_path": string, // File path after change
    "new_line": integer, // Line number after change
    "old_path": string, // File path before change
    "old_line": integer, // Line number before change
    "width": integer, // Width of the image
    "height": integer, // Height of the image
    "x": integer, // X coordinate in the image
    "y": integer, // Y coordinate in the image
    "line_range": {
      "start": {
        "line_code": string, // Start line code for multi-line note
        "type": string, // Start line type for multi-line note
        "old_line": integer, // Start old_line line number
        "new_line": integer, // Start new_line line number
      }, // Start line for a multi-line note
      "end": {
        "line_code": string, // End line code for multi-line note
        "type": string, // End line type for multi-line note
        "old_line": integer, // End old_line line number
        "new_line": integer, // End new_line line number
      }, // End line for a multi-line note
    }, // Multi-line start and end
  }, // Position when creating a note
}
```
### Responses

#### 201 - Created

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

