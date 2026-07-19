# 05-Find playbook run by channel ID [GET]

`GET /plugins/playbooks/api/v0/runs/channel/{channel_id}`

Find playbook run by channel ID

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | ID of the channel associated to the playbook run to retrieve. |

### Responses

#### 200 - Playbook run associated to the channel.

Schema (application/json):
```json
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
```

#### 404 - 

#### 500 - 

