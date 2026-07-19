# 14-Add an item to a playbook run's checklist [POST]

`POST /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/add`

The most common pattern to add a new item is to only send its title as the request payload. By default, it is an open item, with no assignee and no slash command.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose checklist will be modified. |
| `checklist` | `integer` | `path` | Yes | Zero-based index of the checklist to modify. |

### Request Body (application/json)

```json
{
  "title": string (required), // The title of the checklist item.
  "state": enum("" | "in_progress" | "closed"), // The state of the checklist item. An empty string means that the item is not done.
  "state_modified": integer, // The timestamp for the latest modification of the item's state, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the item was never modified.
  "assignee_id": string, // The identifier of the user that has been assigned to complete this item. If the item has no assignee, this is an empty string.
  "assignee_modified": integer, // The timestamp for the latest modification of the item's assignee, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the item never got an assignee.
  "command": string, // The slash command associated with this item. If the item has no slash command associated, this is an empty string
  "command_last_run": integer, // The timestamp for the latest execution of the item's command, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the command was never executed.
  "description": string, // A detailed description of the checklist item, formatted with Markdown.
}
```
### Responses

#### 200 - Item successfully added.

#### default - Error response

Schema (application/json):
```json
{
  "error": string (required), // A message with the error description.
  "details": string (required), // Further details on where and why this error happened.
}
```

