# 06-Get a list of merge request notes [GET]

`GET /api/v4/projects/{id}/merge_requests/{noteable_id}/notes`

Get a list of merge request notes

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `noteable_id` | `integer` | `path` | Yes | The ID of the noteable |
| `order_by` | `string` | `query` | No | Return notes ordered by `created_at` or `updated_at` fields. |
| `sort` | `string` | `query` | No | Return notes sorted in `asc` or `desc` order. |
| `activity_filter` | `string` | `query` | No | The type of notables which are returned. |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

