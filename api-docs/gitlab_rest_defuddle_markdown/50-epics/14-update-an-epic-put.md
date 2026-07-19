# 14-Update an epic [PUT]

`PUT /api/v4/groups/{id}/(-/)epics/{epic_iid}`

Updates an epic

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `epic_iid` | `integer` | `path` | Yes | The internal ID of an epic |

### Request Body (application/json)

```json
{
  "title": string, // The title of an epic
  "color": string, // The color of an epic
  "description": string, // The description of an epic
  "confidential": boolean, // Indicates if the epic is confidential
  "updated_at": string, // Date time when the epic was updated. Available only for admins and project owners
  "start_date": string, // Deprecated: use start_date_fixed instead
  "start_date_fixed": string, // The start date of an epic
  "start_date_is_fixed": boolean, // Indicates start date should be sourced from start_date_fixed field not the issue milestones
  "end_date": string, // Deprecated: use due_date_fixed instead
  "due_date_fixed": string, // The due date of an epic
  "due_date_is_fixed": boolean, // Indicates due date should be sourced from due_date_fixed field not the issue milestones
  "labels": [
    string
  ], // Comma-separated label names for an issue
  "add_labels": [
    string
  ], // Comma-separated label names to add to an issue
  "remove_labels": [
    string
  ], // Comma-separated label names to remove from an issue
  "state_event": enum("reopen" | "close"), // State event for an epic
  "parent_id": integer, // The ID of a parent epic
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "work_item_id": integer,
  "iid": integer,
  "color": string,
  "text_color": string,
  "group_id": integer,
  "parent_id": integer,
  "parent_iid": integer,
  "imported": boolean,
  "imported_from": string,
  "title": string,
  "description": string,
  "confidential": boolean,
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
  "start_date": string,
  "start_date_is_fixed": boolean,
  "start_date_fixed": string,
  "start_date_from_inherited_source": string,
  "start_date_from_milestones": string,
  "end_date": string,
  "due_date": string,
  "due_date_is_fixed": boolean,
  "due_date_fixed": string,
  "due_date_from_inherited_source": string,
  "due_date_from_milestones": string,
  "state": string,
  "web_edit_url": string,
  "web_url": string,
  "references": [
    {}
  ],
  "reference": string,
  "created_at": string,
  "updated_at": string,
  "closed_at": string,
  "labels": [
    string
  ],
  "upvotes": integer,
  "downvotes": integer,
  "subscribed": boolean,
  "_links": {},
}
```

#### 400 - Bad request

#### 403 - Forbidden

#### 404 - Not found

