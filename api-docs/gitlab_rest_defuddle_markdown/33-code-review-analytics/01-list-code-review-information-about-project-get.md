# 01-List code review information about project [GET]

`GET /api/v4/analytics/code_review`

List code review information about project

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `project_id` | `integer` | `query` | Yes | Project ID |
| `label_name` | `array` | `query` | No | Array of label names to filter by |
| `milestone_title` | `string` | `query` | No | Milestone title to filter by |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `not` | `object` | `query` | No | Filters by the specified parameters |
| `not[label_name]` | `array` | `query` | No | Array of label names to filter by |
| `not[milestone_title]` | `string` | `query` | No | Milestone title to filter by |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "project_id": integer,
  "title": string,
  "description": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
  "web_url": string,
  "milestone": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "group_id": string,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "due_date": string,
    "start_date": string,
    "expired": boolean,
    "web_url": string,
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
  "approved_by": {
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
  "notes_count": integer,
  "review_time": integer, // Review time in hours
  "diff_stats": string,
}
```

#### 400 - Bad Request

