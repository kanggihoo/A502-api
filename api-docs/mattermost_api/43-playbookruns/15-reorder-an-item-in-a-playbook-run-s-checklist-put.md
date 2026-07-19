# 15-Reorder an item in a playbook run's checklist [PUT]

`PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/reorder`

Reorder an item in a playbook run's checklist

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose checklist will be modified. |
| `checklist` | `integer` | `path` | Yes | Zero-based index of the checklist to modify. |

### Request Body (application/json)

```json
{
  "item_num": integer (required), // Zero-based index of the item to reorder.
  "new_location": integer (required), // Zero-based index of the new place to move the item to.
}
```
### Responses

#### 200 - Item successfully reordered.

#### 400 - 

#### 500 - 

