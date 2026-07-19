# 22-Add an issue to an epic [POST]

`POST /api/v4/groups/{id}/(-/)epics/{epic_iid}/issues/{epic_issue_id}`

Adds a specified issue to an epic. If the issue already belongs to another epic, it is removed from the original epic.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group owned by the authenticated user |
| `epic_iid` | `any` | `path` | Yes | The internal ID of the epic |
| `issue_id` | `any` | `path` | Yes | The ID of the issue |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer, // ID of the epic-issue relation
  "relative_position": integer, // Relative position of the issue in the epic tree
  "epic": {},
  "issue": {
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
  },
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - No matching issue found

#### 409 - Issue already assigned

