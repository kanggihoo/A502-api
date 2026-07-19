# 10-List all group epics [GET]

`GET /api/v4/groups/{id}/-/epics`

Lists all epics for a specified group and its subgroups. Responses are paginated and return 20 results by default.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `order_by` | `string` | `query` | No | Return epics ordered by `created_at`, `updated_at` or `title` fields. |
| `sort` | `string` | `query` | No | Return epics sorted in `asc` or `desc` order. |
| `search` | `string` | `query` | No | Search epics for text present in the title or description |
| `state` | `string` | `query` | No | Return opened, closed, or all epics |
| `author_id` | `integer` | `query` | No | Return epics which are authored by the user with the given ID |
| `author_username` | `string` | `query` | No | Return epics which are authored by the given username |
| `labels` | `array` | `query` | No | Comma-separated list of label names |
| `with_labels_details` | `boolean` | `query` | No | Return titles of labels and other details |
| `created_after` | `string` | `query` | No | Return epics created after the specified time |
| `created_before` | `string` | `query` | No | Return epics created before the specified time |
| `updated_after` | `string` | `query` | No | Return epics updated after the specified time |
| `updated_before` | `string` | `query` | No | Return epics updated before the specified time |
| `include_ancestor_groups` | `boolean` | `query` | No | Include epics from ancestor groups |
| `include_descendant_groups` | `boolean` | `query` | No | Include epics from descendant groups |
| `my_reaction_emoji` | `string` | `query` | No | Return epics reacted by the authenticated user by the given emoji |
| `confidential` | `boolean` | `query` | No | Return epics with given confidentiality |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `not` | `object` | `query` | No | Object that contains filters |
| `not[labels]` | `array` | `query` | No | Comma-separated list of label names |
| `not[author_id]` | `integer` | `query` | No | Return epics which are not authored by the user with the given ID |
| `not[author_username]` | `string` | `query` | No | Return epics which are not authored by the given username |

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

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

