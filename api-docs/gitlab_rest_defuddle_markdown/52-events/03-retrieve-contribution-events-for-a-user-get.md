# 03-Retrieve contribution events for a user [GET]

`GET /api/v4/users/{id}/events`

Retrieves the contribution events for a specified user. Does not return events associated with epics or merge requests. Returns bulk push events with limited commit details.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or username of the user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `action` | `string` | `query` | No | Event action to filter on |
| `target_type` | `string` | `query` | No | Event target type to filter on |
| `before` | `string` | `query` | No | Include only events created before this date |
| `after` | `string` | `query` | No | Include only events created after this date |
| `sort` | `string` | `query` | No | Return events sorted in ascending and descending order |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "action_name": string,
  "target_id": integer,
  "target_iid": integer,
  "target_type": string,
  "author_id": integer,
  "target_title": string,
  "created_at": string,
  "note": {
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
  "wiki_page": {
    "format": string,
    "slug": string,
    "title": string,
    "wiki_page_meta_id": integer,
  },
  "imported": boolean,
  "imported_from": string,
  "push_data": {
    "commit_count": integer,
    "action": string,
    "ref_type": string,
    "commit_from": string,
    "commit_to": string,
    "ref": string,
    "commit_title": string,
    "ref_count": integer,
  },
  "author_username": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

