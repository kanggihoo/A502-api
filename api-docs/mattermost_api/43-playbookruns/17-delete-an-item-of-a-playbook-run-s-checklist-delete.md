# 17-Delete an item of a playbook run's checklist [DELETE]

`DELETE /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}`

Delete an item of a playbook run's checklist

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose checklist will be modified. |
| `checklist` | `integer` | `path` | Yes | Zero-based index of the checklist to modify. |
| `item` | `integer` | `path` | Yes | Zero-based index of the item to modify. |

### Responses

#### 204 - Item successfully deleted.

#### 400 - 

#### 500 - 

