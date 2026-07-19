# 65-Create an issue [POST]

`POST /api/v4/projects/{id}/issues`

Creates an issue for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "title": string (required), // The title of an issue
  "created_at": string, // Date time when the issue was created. Available only for admins and project owners.
  "merge_request_to_resolve_discussions_of": integer, // The IID of a merge request for which to resolve discussions
  "discussion_to_resolve": string, // The ID of a discussion to resolve, also pass `merge_request_to_resolve_discussions_of`
  "iid": integer, // The internal ID of a project issue. Available only for admins and project owners.
  "description": string, // The description of an issue
  "assignee_ids": [
    integer
  ], // The array of user IDs to assign issue
  "assignee_id": integer, // [Deprecated] The ID of a user to assign issue
  "milestone_id": integer, // The ID of a milestone to assign issue
  "milestone": string, // The title of a project or ancestor-group milestone to assign the issue to. Mutually exclusive with `milestone_id`.
  "labels": [
    string
  ], // Comma-separated list of label names
  "add_labels": [
    string
  ], // Comma-separated list of label names
  "remove_labels": [
    string
  ], // Comma-separated list of label names
  "due_date": string, // Date string in the format YEAR-MONTH-DAY
  "start_date": string, // Date string in the format YEAR-MONTH-DAY
  "confidential": boolean, // Boolean parameter if the issue should be confidential
  "discussion_locked": boolean, //  Boolean parameter indicating if the issue's discussion is locked
  "issue_type": enum("issue" | "incident" | "test_case" | "requirement" | "task" | "ticket"), // The type of the issue. Accepts: issue, incident, test_case, requirement, task, ticket
  "severity": enum("unknown" | "low" | "medium" | "high" | "critical"), // The severity of the issue. Only applies to incidents. Accepts: unknown, low, medium, high, critical
  "weight": integer, // The weight of the issue
  "epic_id": integer, // The ID of an epic to associate the issue with
  "epic_iid": integer, // The IID of an epic to associate the issue with (deprecated)
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

