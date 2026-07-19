# 02-List all linked epics for an epic [GET]

`GET /api/v4/groups/{id}/epics/{epic_iid}/related_epics`

Lists all linked epics for a specified epic.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID or URL-encoded path of the group |
| `epic_iid` | `integer` | `path` | Yes | The internal ID of a group epic |

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
  "related_epic_link_id": integer,
  "link_type": string,
  "link_created_at": string,
  "link_updated_at": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

