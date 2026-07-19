# 11-Create a group milestone [POST]

`POST /api/v4/groups/{id}/milestones`

Creates a milestone for the specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Request Body (application/json)

```json
{
  "title": string (required), // The title of the milestone
  "description": string, // The description of the milestone
  "due_date": string, // The due date of the milestone. The ISO 8601 date format (%Y-%m-%d)
  "start_date": string, // The start date of the milestone. The ISO 8601 date format (%Y-%m-%d)
}
```
### Responses

#### 201 - Created

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

