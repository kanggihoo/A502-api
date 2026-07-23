# 71-Move an issue [POST]

`POST /api/v4/projects/{id}/issues/{issue_iid}/move`

Moves a specified issue to a different project. If the target project is the source project or the user has insufficient permissions, an error message with status code `400` is returned. If a label or milestone with the same name also exists in the target project, it is then assigned to the issue being moved.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of a project issue |

### Request Body (application/json)

```json
{
  "to_project_id": integer (required), // The ID of the new project
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
  "title": string,
  "description": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
  "closed_at": string,
  "closed_by": {
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
  "labels": [
    string
  ],
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
  "assignees": {
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
  "type": string, // One of ["ISSUE", "INCIDENT", "TEST_CASE", "REQUIREMENT", "TASK", "TICKET"]
  "assignee": {
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
  "user_notes_count": integer,
  "merge_requests_count": integer,
  "upvotes": integer,
  "downvotes": integer,
  "start_date": string,
  "due_date": string,
  "confidential": boolean,
  "discussion_locked": boolean,
  "issue_type": string,
  "web_url": string,
  "time_stats": {
    "time_estimate": integer,
    "total_time_spent": integer,
    "human_time_estimate": string,
    "human_total_time_spent": string,
  },
  "task_completion_status": {
    "count": integer,
    "completed_count": integer,
  },
  "weight": integer,
  "blocking_issues_count": integer,
  "has_tasks": boolean,
  "task_status": string,
  "_links": {},
  "references": {
    "short": string,
    "relative": string,
    "full": string,
  },
  "severity": string, // One of ["UNKNOWN", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
  "subscribed": boolean,
  "moved_to_id": integer,
  "imported": boolean,
  "imported_from": string,
  "service_desk_reply_to": string,
  "epic_iid": string,
  "epic": {
    "id": string,
    "iid": string,
    "title": string,
    "url": string,
    "group_id": string,
    "human_readable_end_date": string,
    "human_readable_timestamp": string,
  },
  "iteration": {
    "id": integer,
    "iid": integer,
    "sequence": integer,
    "group_id": integer,
    "title": string,
    "description": string,
    "state": integer,
    "created_at": string,
    "updated_at": string,
    "start_date": string,
    "due_date": string,
    "web_url": string,
  },
  "health_status": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

