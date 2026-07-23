# 19-Retrieve a merge request [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}`

Retrieves a merge request for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of the merge request. |
| `render_html` | `boolean` | `query` | No | If `true`, response includes rendered HTML for title and description. |
| `include_diverged_commits_count` | `boolean` | `query` | No | If `true`, response includes the commits behind the target branch. |
| `include_rebase_in_progress` | `boolean` | `query` | No | If `true`, response includes whether a rebase operation is in progress. |

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
  "subscribed": boolean,
  "changes_count": string,
  "latest_build_started_at": string,
  "latest_build_finished_at": string,
  "first_deployed_to_production_at": string,
  "pipeline": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "sha": string,
    "ref": string,
    "status": string,
    "source": string,
    "created_at": string,
    "updated_at": string,
    "web_url": string,
  },
  "head_pipeline": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "sha": string,
    "ref": string,
    "status": string,
    "source": string,
    "created_at": string,
    "updated_at": string,
    "web_url": string,
    "before_sha": string,
    "tag": boolean,
    "yaml_errors": string,
    "user": {
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
    "started_at": string,
    "finished_at": string,
    "committed_at": string,
    "duration": integer, // Time spent running in seconds
    "queued_duration": integer, // Time spent enqueued in seconds
    "coverage": number,
    "detailed_status": {
      "icon": string,
      "text": string,
      "label": string,
      "group": string,
      "tooltip": string,
      "has_details": boolean,
      "details_path": string,
      "illustration": {},
      "favicon": string,
      "action": string,
    },
    "archived": boolean,
  },
  "diff_refs": {
    "base_sha": string,
    "head_sha": string,
    "start_sha": string,
  },
  "merge_error": string,
  "rebase_in_progress": boolean,
  "diverged_commits_count": integer,
  "first_contribution": boolean,
  "user": {},
}
```

#### 400 - Bad Request

#### 404 - Not found

