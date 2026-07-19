# 20-Run an item's slash command [PUT]

`PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/run`

Run an item's slash command

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose item will be executed. |
| `checklist` | `integer` | `path` | Yes | Zero-based index of the checklist whose item will be executed. |
| `item` | `integer` | `path` | Yes | Zero-based index of the item whose slash command will be executed. |

### Responses

#### 200 - Item's slash command successfully executed.

Schema (application/json):
```json
{
  "trigger_id": string (required), // The trigger_id returned by the slash command.
}
```

#### 400 - 

#### 500 - 

