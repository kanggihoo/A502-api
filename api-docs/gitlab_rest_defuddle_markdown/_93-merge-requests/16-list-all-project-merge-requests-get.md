# 16-List all project merge requests [GET]

`GET /api/v4/projects/{id}/merge_requests`

Lists all project merge requests.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `author_id` | `integer` | `query` | No | Returns merge requests created by the given user `id`. Mutually exclusive with `author_username`. Combine with `scope=all` or `scope=assigned_to_me`. |
| `author_username` | `string` | `query` | No | Returns merge requests created by the given `username`. Mutually exclusive with `author_id`. |
| `assignee_id` | `any` | `query` | No | Returns merge requests assigned to the given user `id`. `None` returns unassigned merge requests. `Any` returns merge requests with an assignee. |
| `assignee_username` | `array` | `query` | No | Returns merge requests created by the given `username`. Mutually exclusive with `author_id`. |
| `reviewer_username` | `string` | `query` | No | Returns merge requests which have the user as a reviewer with the given `username`. `None` returns merge requests with no reviewers. `Any` returns merge requests with any reviewer. Mutually exclusive with `reviewer_id`. Introduced in GitLab 13.8. |
| `labels` | `array` | `query` | No | Returns merge requests matching a comma-separated list of labels. `None` lists all merge requests with no labels. `Any` lists all merge requests with at least one label. Predefined names are case-insensitive. |
| `milestone` | `string` | `query` | No | Returns merge requests for a specific milestone. `None` returns merge requests with no milestone. `Any` returns merge requests that have an assigned milestone. |
| `my_reaction_emoji` | `string` | `query` | No | Returns merge requests reacted by the authenticated user by the given `emoji`. `None` returns issues not given a reaction. `Any` returns issues given at least one reaction. |
| `reviewer_id` | `any` | `query` | No | Returns merge requests which have the user as a reviewer with the given user `id`. `None` returns merge requests with no reviewers. `Any` returns merge requests with any reviewer. Mutually exclusive with `reviewer_username`. |
| `state` | `string` | `query` | No | Returns `all` merge requests or just those that are `opened`, `closed`, `locked`, or `merged`. |
| `order_by` | `string` | `query` | No | Returns merge requests ordered by `created_at`, `label_priority`, `milestone_due`, `popularity`, `priority`, `title`, `updated_at` or `merged_at` fields. Introduced in GitLab 14.8. |
| `sort` | `string` | `query` | No | Returns merge requests sorted in `asc` or `desc` order. |
| `with_labels_details` | `boolean` | `query` | No | If `true`, response returns more details for each label in labels field: `:name`,`:color`, `:description`, `:description_html`, `:text_color` |
| `with_merge_status_recheck` | `boolean` | `query` | No | If `true`, this projection requests (but does not guarantee) that the `merge_status` field be recalculated asynchronously. Introduced in GitLab 13.0. |
| `created_after` | `string` | `query` | No | Returns merge requests created on or after the given time. Expected in ISO 8601 format. |
| `created_before` | `string` | `query` | No | Returns merge requests created on or before the given time. Expected in ISO 8601 format. |
| `updated_after` | `string` | `query` | No | Returns merge requests updated on or after the given time. Expected in ISO 8601 format. |
| `updated_before` | `string` | `query` | No | Returns merge requests updated on or before the given time. Expected in ISO 8601 format. |
| `view` | `string` | `query` | No | If simple, returns the `iid`, URL, title, description, and basic state of merge request |
| `scope` | `string` | `query` | No | Returns merge requests for the given scope: `created_by_me`, `assigned_to_me`, `reviews_for_me` or `all` |
| `source_branch` | `string` | `query` | No | Returns merge requests with the given source branch |
| `source_project_id` | `integer` | `query` | No | Returns merge requests with the given source project id |
| `target_branch` | `string` | `query` | No | Returns merge requests with the given target branch |
| `search` | `string` | `query` | No | Search merge requests against their `title` and `description`. |
| `in` | `string` | `query` | No | Modify the scope of the search attribute. `title`, `description`, or a string joining them with comma. |
| `wip` | `string` | `query` | No | Deprecated. Use `draft` instead. Filter merge requests against their `wip` status. `yes` to return only draft merge requests, `no` to return non-draft merge requests. |
| `draft` | `boolean` | `query` | No | Filter merge requests against their `draft` status. `true` to return only draft merge requests, `false` to return non-draft merge requests. |
| `not` | `object` | `query` | No | Returns merge requests that do not match the parameters supplied |
| `not[author_id]` | `integer` | `query` | No | `<Negated>` Returns merge requests created by the given user `id`. Mutually exclusive with `author_username`. Combine with `scope=all` or `scope=assigned_to_me`. |
| `not[author_username]` | `string` | `query` | No | `<Negated>` Returns merge requests created by the given `username`. Mutually exclusive with `author_id`. |
| `not[assignee_id]` | `any` | `query` | No | `<Negated>` Returns merge requests assigned to the given user `id`. `None` returns unassigned merge requests. `Any` returns merge requests with an assignee. |
| `not[assignee_username]` | `array` | `query` | No | `<Negated>` Returns merge requests created by the given `username`. Mutually exclusive with `author_id`. |
| `not[reviewer_username]` | `string` | `query` | No | `<Negated>` Returns merge requests which have the user as a reviewer with the given `username`. `None` returns merge requests with no reviewers. `Any` returns merge requests with any reviewer. Mutually exclusive with `reviewer_id`. Introduced in GitLab 13.8. |
| `not[labels]` | `array` | `query` | No | `<Negated>` Returns merge requests matching a comma-separated list of labels. `None` lists all merge requests with no labels. `Any` lists all merge requests with at least one label. Predefined names are case-insensitive. |
| `not[milestone]` | `string` | `query` | No | `<Negated>` Returns merge requests for a specific milestone. `None` returns merge requests with no milestone. `Any` returns merge requests that have an assigned milestone. |
| `not[my_reaction_emoji]` | `string` | `query` | No | `<Negated>` Returns merge requests reacted by the authenticated user by the given `emoji`. `None` returns issues not given a reaction. `Any` returns issues given at least one reaction. |
| `not[reviewer_id]` | `integer` | `query` | No | `<Negated>` Returns merge requests which have the user as a reviewer with the given user `id`. `None` returns merge requests with no reviewers. `Any` returns merge requests with any reviewer. Mutually exclusive with `reviewer_username`. |
| `deployed_before` | `string` | `query` | No | Returns merge requests deployed before the given date/time. Expected in ISO 8601 format. |
| `deployed_after` | `string` | `query` | No | Returns merge requests deployed after the given date/time. Expected in ISO 8601 format |
| `environment` | `string` | `query` | No | Returns merge requests deployed to the given environment |
| `merge_user_id` | `integer` | `query` | No | Returns merge requests which have been merged by the user with the given user `id`. Mutually exclusive with `merge_user_username`. |
| `merge_user_username` | `string` | `query` | No | Returns merge requests which have been merged by the user with the given `username`. Mutually exclusive with `merge_user_id`. |
| `approver_ids` | `any` | `query` | No | Return merge requests which have specified the users with the given IDs as an individual approver |
| `approved_by_ids` | `any` | `query` | No | Return merge requests which have been approved by the specified users with the given IDs |
| `approved_by_usernames` | `any` | `query` | No | Return merge requests which have been approved by the specified users with the given<br>            usernames |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `iids` | `array` | `query` | No | Returns the request having the given `iid`. |

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
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

#### 422 - Unprocessable entity

