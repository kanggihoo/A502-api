# 02-List all issues for the currently authenticated user [GET]

`GET /api/v4/issues`

Lists all issues accessible by the currently authenticated user. By default, returns only issues created by the current user. To list all issues, use parameter `scope=all`.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `with_labels_details` | `boolean` | `query` | No | Return titles of labels and other details |
| `state` | `string` | `query` | No | Return opened, closed, or all issues |
| `closed_by_id` | `integer` | `query` | No | Return issues which were closed by the user with the given ID. |
| `order_by` | `string` | `query` | No | Return issues ordered by `created_at`, `due_date`, `label_priority`, `milestone_due`, `popularity`, `priority`, `relative_position`, `title`, or `updated_at` fields. |
| `sort` | `string` | `query` | No | Return issues sorted in `asc` or `desc` order. |
| `due_date` | `string` | `query` | No | Return issues that have no due date (`0`), or whose due date is this week, this month, between two weeks ago and next month, or which are overdue. Accepts: `overdue`, `week`, `month`, `next_month_and_previous_two_weeks`, `0` |
| `issue_type` | `string` | `query` | No | The type of the issue. Accepts: issue, incident, test_case, requirement, task, ticket |
| `labels` | `array` | `query` | No | Comma-separated list of label names |
| `milestone` | `string` | `query` | No | Milestone title |
| `milestone_id` | `string` | `query` | No | Return issues assigned to milestones with the specified timebox value ("Any", "None", "Upcoming" or "Started") |
| `iids` | `array` | `query` | No | The IID array of issues |
| `search` | `string` | `query` | No | Search issues for text present in the title, description, or any combination of these |
| `in` | `string` | `query` | No | `title`, `description`, or a string joining them with comma |
| `author_id` | `integer` | `query` | No | Return issues which are authored by the user with the given ID |
| `author_username` | `string` | `query` | No | Return issues which are authored by the user with the given username |
| `assignee_id` | `any` | `query` | No | Return issues which are assigned to the user with the given ID |
| `assignee_username` | `array` | `query` | No | Return issues which are assigned to the user with the given username |
| `created_after` | `string` | `query` | No | Return issues created after the specified time |
| `created_before` | `string` | `query` | No | Return issues created before the specified time |
| `updated_after` | `string` | `query` | No | Return issues updated after the specified time |
| `updated_before` | `string` | `query` | No | Return issues updated before the specified time |
| `not` | `object` | `query` | No | Filters by the specified parameters |
| `not[labels]` | `array` | `query` | No | Comma-separated list of label names |
| `not[milestone]` | `string` | `query` | No | Milestone title |
| `not[milestone_id]` | `string` | `query` | No | Return issues assigned to milestones without the specified timebox value ("Any", "None", "Upcoming" or "Started") |
| `not[iids]` | `array` | `query` | No | The IID array of issues |
| `not[author_id]` | `integer` | `query` | No | Return issues which are not authored by the user with the given ID |
| `not[author_username]` | `string` | `query` | No | Return issues which are not authored by the user with the given username |
| `not[assignee_id]` | `integer` | `query` | No | Return issues which are not assigned to the user with the given ID |
| `not[assignee_username]` | `array` | `query` | No | Return issues which are not assigned to the user with the given username |
| `not[weight]` | `integer` | `query` | No | Return issues without the specified weight |
| `not[iteration_id]` | `any` | `query` | No | Return issues which are not assigned to the iteration with the given ID |
| `not[iteration_title]` | `string` | `query` | No | Return issues which are not assigned to the iteration with the given title |
| `scope` | `string` | `query` | No | Return issues for the given scope: `created_by_me`, `assigned_to_me` or `all` |
| `my_reaction_emoji` | `string` | `query` | No | Return issues reacted by the authenticated user by the given emoji |
| `confidential` | `boolean` | `query` | No | Filter confidential or public issues |
| `weight` | `any` | `query` | No | The weight of the issue |
| `epic_id` | `any` | `query` | No | The ID of an epic associated with the issues |
| `health_status` | `string` | `query` | No | The health status of the issue. Must be one of: on_track, needs_attention, at_risk, none, any |
| `iteration_id` | `any` | `query` | No | Return issues which are assigned to the iteration with the given ID |
| `iteration_title` | `string` | `query` | No | Return issues which are assigned to the iteration with the given title |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `non_archived` | `boolean` | `query` | No | Return issues from non archived projects |

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

