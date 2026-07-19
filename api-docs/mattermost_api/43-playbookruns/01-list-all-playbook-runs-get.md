# 01-List all playbook runs [GET]

`GET /plugins/playbooks/api/v0/runs`

Retrieve a paged list of playbook runs, filtered by team, status, owner, name and/or members, and sorted by ID, name, status, creation date, end date, team or owner ID.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `query` | Yes | ID of the team to filter by. |
| `page` | `integer` | `query` | No | Zero-based index of the page to request. |
| `per_page` | `integer` | `query` | No | Number of playbook runs to return per page. |
| `sort` | `string` | `query` | No | Field to sort the returned playbook runs by. |
| `direction` | `string` | `query` | No | Direction (ascending or descending) followed by the sorting of the playbook runs. |
| `statuses` | `array` | `query` | No | The returned list will contain only the playbook runs with the specified statuses. |
| `owner_user_id` | `string` | `query` | No | The returned list will contain only the playbook runs commanded by this user. Specify "me" for current user. |
| `participant_id` | `string` | `query` | No | The returned list will contain only the playbook runs for which the given user is a participant. Specify "me" for current user. |
| `search_term` | `string` | `query` | No | The returned list will contain only the playbook runs whose name contains the search term. |
| `channel_id` | `string` | `query` | No | The returned list will contain only the playbook runs associated with this channel ID. |
| `omit_ended` | `boolean` | `query` | No | When set to true, only active runs (with EndAt = 0) are returned. When false or omitted, both active and ended runs are returned. |
| `since` | `integer` | `query` | No | Return only PlaybookRuns created/modified since the given timestamp (in milliseconds). |

### Responses

#### 200 - A paged list of playbook runs.

Schema (application/json):
```json
{
  "total_count": integer, // The total number of playbook runs in the list, regardless of the paging.
  "page_count": integer, // The total number of pages. This depends on the total number of playbook runs in the database and the per_page parameter sent with the request.
  "has_more": boolean, // A boolean describing whether there are more pages after the currently returned.
  "items": [
    {
      "id": string, // A unique, 26 characters long, alphanumeric identifier for the playbook run.
      "name": string, // The name of the playbook run.
      "summary": string, // The summary of the playbook run.
      "is_active": boolean, // True if the playbook run is ongoing; false if the playbook run is ended.
      "owner_user_id": string, // The identifier of the user that is commanding the playbook run.
      "team_id": string, // The identifier of the team where the playbook run's channel is in.
      "channel_id": string, // The identifier of the playbook run's channel.
      "create_at": integer, // The playbook run creation timestamp, formatted as the number of milliseconds since the Unix epoch.
      "end_at": integer, // The playbook run finish timestamp, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the playbook run is not finished.
      "delete_at": integer, // The playbook run deletion timestamp, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the playbook run is not deleted.
      "active_stage": integer, // Zero-based index of the currently active stage.
      "active_stage_title": string, // The title of the currently active stage.
      "post_id": string, // If the playbook run was created from a post, this field contains the identifier of such post. If not, this field is empty.
      "playbook_id": string, // The identifier of the playbook with from which this playbook run was created.
      "checklists": [
        {
          "id": string, // A unique, 26 characters long, alphanumeric identifier for the checklist.
          "title": string, // The title of the checklist.
          "items": [
            {
              "id": string, // A unique, 26 characters long, alphanumeric identifier for the checklist item.
              "title": string, // The title of the checklist item.
              "state": enum("" | "in_progress" | "closed"), // The state of the checklist item. An empty string means that the item is not done.
              "state_modified": integer, // The timestamp for the latest modification of the item's state, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the item was never modified.
              "assignee_id": string, // The identifier of the user that has been assigned to complete this item. If the item has no assignee, this is an empty string.
              "assignee_modified": integer, // The timestamp for the latest modification of the item's assignee, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the item never got an assignee.
              "command": string, // The slash command associated with this item. If the item has no slash command associated, this is an empty string
              "command_last_run": integer, // The timestamp for the latest execution of the item's command, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the command was never executed.
              "description": string, // A detailed description of the checklist item, formatted with Markdown.
              "delete_at": integer, // The timestamp for the last time the item was skipped, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the item was never skipped.
              "due_date": integer, // The timestamp for the due date of the checklist item, formatted as the number of milliseconds since the Unix epoch. It equals 0 if not set. For playbooks, this is a relative timestamp; for runs, this is an absolute timestamp.
              "task_actions": [
                {
                  "trigger": {}, // The trigger configuration for the task action.
                  "actions": [
                    {}
                  ], // The actions to be executed when the trigger is activated.
                }
              ], // An array of all the task actions associated with this task.
              "update_at": integer, // The timestamp for when this checklist item was last modified, formatted as the number of milliseconds since the Unix epoch.
              "condition_id": string, // The ID of the condition that created this checklist item, if any. Empty string if the item was not created by a condition.
              "condition_action": enum("" | "hidden" | "shown_because_modified"), // A string that represents the action created as a result of a condition evaluation. Empty string means no action, 'hidden' means the item is hidden due to condition not being met, 'shown_because_modified' means the item is shown despite condition not being met because it was recently modified.
              "condition_reason": string, // A string representation of the condition that affects this checklist item. Empty string if no condition is associated with this item.
            }
          ], // The list of tasks to do.
        }
      ],
    }
  ], // The playbook runs in this page.
}
```

#### 400 - 

#### 403 - 

#### 500 - 

