# 19-Update the assignee of an item [PUT]

`PUT /plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/assignee`

Update the assignee of an item

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose item will get a new assignee. |
| `checklist` | `integer` | `path` | Yes | Zero-based index of the checklist whose item will get a new assignee. |
| `item` | `integer` | `path` | Yes | Zero-based index of the item that will get a new assignee. |

### Request Body (application/json)

```json
{
  "assignee_id": string (required), // The user ID of the new assignee of the item.
}
```
### Responses

#### 200 - Item's assignee successfully updated.

#### 400 - 

#### 500 - 

