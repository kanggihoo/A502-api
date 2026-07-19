# 05-Update status of an external status check [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/status_check_responses`

Updates the status of an external status check for a specified merge request, informing GitLab that a merge request has passed a check by an external service. To set the status of an external check, the personal access token used must belong to a user with the Developer, Maintainer, or Owner role on the target project of the merge request. Any user with permission to approve the merge request can use this operation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of a project |
| `merge_request_iid` | `integer` | `path` | Yes | IID of a merge request |

### Request Body (application/json)

```json
{
  "external_status_check_id": integer (required), // ID of an external status check
  "sha": string (required), // SHA at HEAD of the source branch
  "status": enum("passed" | "failed" | "pending") (required), // Set to `pending` to mark the check as pending, `passed` to pass the check, or `failed` to fail it
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "merge_request": {
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
  },
  "external_status_check": {
    "id": integer,
    "name": string,
    "project_id": integer,
    "external_url": string,
    "protected_branches": [
      {
        "id": integer,
        "name": string,
        "push_access_levels": [
          {
            "id": integer,
            "access_level": integer,
            "access_level_description": string,
            "deploy_key_id": integer,
            "user_id": integer,
            "group_id": integer,
            "member_role_id": integer,
            "member_role_name": string,
          }
        ],
        "merge_access_levels": [
          {
            "id": integer,
            "access_level": integer,
            "access_level_description": string,
            "deploy_key_id": integer,
            "user_id": integer,
            "group_id": integer,
            "member_role_id": integer,
            "member_role_name": string,
          }
        ],
        "allow_force_push": boolean,
        "unprotect_access_levels": [
          {
            "id": integer,
            "access_level": integer,
            "access_level_description": string,
            "deploy_key_id": integer,
            "user_id": integer,
            "group_id": integer,
            "member_role_id": integer,
            "member_role_name": string,
          }
        ],
        "code_owner_approval_required": boolean,
        "inherited": boolean,
      }
    ],
    "hmac": boolean,
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

