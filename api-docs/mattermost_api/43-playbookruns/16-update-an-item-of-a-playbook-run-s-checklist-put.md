# 16-Update an item of a playbook run's checklist [PUT]

`PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}`

Update the title, slash command, and description of an item in one of the playbook run's checklists.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose checklist will be modified. |
| `checklist` | `integer` | `path` | Yes | Zero-based index of the checklist to modify. |
| `item` | `integer` | `path` | Yes | Zero-based index of the item to modify. |

### Request Body (application/json)

```json
{
  "title": string (required), // The new title of the item.
  "command": string (required), // The new slash command of the item.
  "description": string, // The new description of the item, formatted with Markdown.
}
```
### Responses

#### 200 - Item updated.

#### 400 - 

#### 500 - 

