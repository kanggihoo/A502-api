# 04-Update a draft note [PUT]

`PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}/draft_notes/{draft_note_id}`

Updates a draft note for a specified merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project. |
| `merge_request_iid` | `integer` | `path` | Yes | The ID of a merge request. |
| `draft_note_id` | `integer` | `path` | Yes | The ID of a draft note |

### Request Body (application/json)

```json
{
  "note": string, // The content of a note.
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
    }, // Line range for a multi-line note
  }, // Position when creating a note
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "author_id": integer,
  "merge_request_id": integer,
  "resolve_discussion": boolean,
  "discussion_id": string,
  "note": string,
  "commit_id": string,
  "line_code": string,
  "position": {},
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

