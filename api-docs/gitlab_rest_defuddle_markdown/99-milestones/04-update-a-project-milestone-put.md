# 04-Update a project milestone [PUT]

`PUT /api/v4/projects/{id}/milestones/{milestone_id}`

Updates a specified project milestone.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `milestone_id` | `integer` | `path` | Yes | The milestone ID number |

### Request Body (application/json)

```json
{
  "title": string, // The title of the milestone
  "state_event": enum("close" | "activate"), // The state event of the milestone 
  "description": string, // The description of the milestone
  "due_date": string, // The due date of the milestone. The ISO 8601 date format (%Y-%m-%d)
  "start_date": string, // The start date of the milestone. The ISO 8601 date format (%Y-%m-%d)
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
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
}
```

#### 400 - Bad Request

#### 404 - Not Found

