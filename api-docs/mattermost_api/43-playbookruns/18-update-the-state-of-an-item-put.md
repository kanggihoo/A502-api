# 18-Update the state of an item [PUT]

`PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/state`

Update the state of an item

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose checklist will be modified. |
| `checklist` | `integer` | `path` | Yes | Zero-based index of the checklist to modify. |
| `item` | `integer` | `path` | Yes | Zero-based index of the item to modify. |

### Request Body (application/json)

```json
{
  "new_state": enum("" | "in_progress" | "closed") (required), // The new state of the item.
}
```
### Responses

#### 200 - Item's state successfully updated.

#### 400 - 

#### 500 - 

