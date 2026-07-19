# 20-Update a merge request [PUT]

`PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}`

Updates a merge request for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Request Body (application/json)

```json
{
  "title": string, // The title of the merge request.
  "target_branch": string, // The target branch.
  "state_event": enum("close" | "reopen"), // New state (close/reopen).
  "discussion_locked": boolean, // Flag indicating if the merge request’s discussion is locked. If the discussion is locked only project members can add, edit or resolve comments.
  "assignee_id": integer, // Assignee user ID.
  "assignee_ids": [
    integer
  ], // The IDs of the users to assign the merge request to, as a comma-separated list. Set to 0 or provide an empty value to unassign all assignees.
  "reviewer_ids": [
    integer
  ], // The IDs of the users to review the merge request, as a comma-separated list. Set to 0 or provide an empty value to unassign all reviewers.
  "description": string, // Description of the merge request. Limited to 1,048,576 characters.
  "labels": [
    string
  ], // Comma-separated label names for a merge request. Set to an empty string to unassign all labels.
  "add_labels": [
    string
  ], // Comma-separated label names to add to a merge request.
  "remove_labels": [
    string
  ], // Comma-separated label names to remove from a merge request.
  "milestone_id": integer, // The global ID of a milestone to assign the merge request to.
  "milestone": string, // The title of a project or ancestor-group milestone to assign the merge request to. Mutually exclusive with `milestone_id`.
  "remove_source_branch": boolean, // Flag indicating if a merge request should remove the source branch when merging.
  "allow_collaboration": boolean, // Allow commits from members who can merge to the target branch.
  "allow_maintainer_to_push": boolean, // [deprecated] See allow_collaboration
  "squash": boolean, // Squash commits into a single commit when merging.
  "merge_after": string, // Date after which the merge request can be merged.
  "approvals_before_merge": integer, // Number of approvals required before this can be merged
  "approval_rules_attributes": [
    {
      "id": integer, // The ID of a rule
      "approvals_required": integer, // Total number of approvals required
    }
  ],
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

#### 400 - Bad request

#### 404 - Not found

#### 409 - Conflict

#### 422 - Unprocessable entity

