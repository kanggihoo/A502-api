# 13-Create an issue link [POST]

`POST /api/v4/projects/{id}/issues/{issue_iid}/links`

Creates a two-way relationship between two issues. The user must be allowed to update both issues to succeed.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of a project’s issue |

### Request Body (application/json)

```json
{
  "target_project_id": any (required),
  "target_issue_iid": any (required),
  "link_type": enum("relates_to" | "blocks" | "is_blocked_by"), // The type of the relation (“relates_to”, “blocks”, “is_blocked_by”),defaults to “relates_to”)
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "source_issue": {
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
  "target_issue": {
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
  "link_type": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

