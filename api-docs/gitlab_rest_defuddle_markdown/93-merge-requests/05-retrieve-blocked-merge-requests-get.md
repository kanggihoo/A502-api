# 05-Retrieve blocked merge requests [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/blockees`

Retrieves merge requests blocked by a specified merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge request |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "blocking_merge_request": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "merged_by": {
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
    "merge_user": {
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
    "merged_at": string,
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
    "closed_at": string,
    "title_html": string,
    "description_html": string,
    "target_branch": string,
    "source_branch": string,
    "user_notes_count": integer,
    "upvotes": integer,
    "downvotes": integer,
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
    "reviewers": {
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
    "source_project_id": integer,
    "target_project_id": integer,
    "labels": [
      string
    ],
    "draft": boolean,
    "imported": boolean,
    "imported_from": string,
    "work_in_progress": boolean,
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
    "merge_when_pipeline_succeeds": boolean,
    "merge_status": string,
    "detailed_merge_status": string,
    "merge_after": string,
    "sha": string,
    "merge_commit_sha": string,
    "squash_commit_sha": string,
    "discussion_locked": boolean,
    "should_remove_source_branch": boolean,
    "force_remove_source_branch": boolean,
    "prepared_at": string,
    "allow_collaboration": boolean,
    "allow_maintainer_to_push": boolean,
    "reference": string,
    "references": {
      "short": string,
      "relative": string,
      "full": string,
    },
    "web_url": string,
    "time_stats": {
      "time_estimate": integer,
      "total_time_spent": integer,
      "human_time_estimate": string,
      "human_total_time_spent": string,
    },
    "squash": boolean,
    "squash_on_merge": boolean,
    "task_completion_status": {
      "count": integer,
      "completed_count": integer,
    },
    "has_conflicts": boolean,
    "blocking_discussions_resolved": boolean,
    "approvals_before_merge": integer,
  },
  "blocked_merge_request": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "merged_by": {
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
    "merge_user": {
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
    "merged_at": string,
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
    "closed_at": string,
    "title_html": string,
    "description_html": string,
    "target_branch": string,
    "source_branch": string,
    "user_notes_count": integer,
    "upvotes": integer,
    "downvotes": integer,
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
    "reviewers": {
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
    "source_project_id": integer,
    "target_project_id": integer,
    "labels": [
      string
    ],
    "draft": boolean,
    "imported": boolean,
    "imported_from": string,
    "work_in_progress": boolean,
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
    "merge_when_pipeline_succeeds": boolean,
    "merge_status": string,
    "detailed_merge_status": string,
    "merge_after": string,
    "sha": string,
    "merge_commit_sha": string,
    "squash_commit_sha": string,
    "discussion_locked": boolean,
    "should_remove_source_branch": boolean,
    "force_remove_source_branch": boolean,
    "prepared_at": string,
    "allow_collaboration": boolean,
    "allow_maintainer_to_push": boolean,
    "reference": string,
    "references": {
      "short": string,
      "relative": string,
      "full": string,
    },
    "web_url": string,
    "time_stats": {
      "time_estimate": integer,
      "total_time_spent": integer,
      "human_time_estimate": string,
      "human_total_time_spent": string,
    },
    "squash": boolean,
    "squash_on_merge": boolean,
    "task_completion_status": {
      "count": integer,
      "completed_count": integer,
    },
    "has_conflicts": boolean,
    "blocking_discussions_resolved": boolean,
    "approvals_before_merge": integer,
  },
  "project_id": integer,
}
```

#### 400 - Bad Request

#### 404 - Not Found

