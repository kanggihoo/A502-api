# 03-Get a playbook [GET]

`GET /plugins/playbooks/api/v0/playbooks/{id}`

Get a playbook

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook to retrieve. |

### Responses

#### 200 - Playbook.

Schema (application/json):
```json
{
  "id": string, // A unique, 26 characters long, alphanumeric identifier for the playbook.
  "title": string, // The title of the playbook.
  "description": string, // The description of the playbook.
  "team_id": string, // The identifier of the team where the playbook is in.
  "create_public_playbook_run": boolean, // A boolean indicating whether the playbook runs created from this playbook should be public or private.
  "create_at": integer, // The playbook creation timestamp, formatted as the number of milliseconds since the Unix epoch.
  "delete_at": integer, // The playbook deletion timestamp, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the playbook is not deleted.
  "num_stages": integer, // The number of stages defined in this playbook.
  "num_steps": integer, // The total number of steps from all the stages defined in this playbook.
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
  ], // The stages defined in this playbook.
  "member_ids": [
    string
  ], // The identifiers of all the users that are members of this playbook.
}
```

#### 403 - 

#### 500 - 

