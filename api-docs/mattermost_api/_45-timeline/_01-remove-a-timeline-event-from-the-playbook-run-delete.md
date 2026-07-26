# 01-Remove a timeline event from the playbook run [DELETE]

`DELETE /plugins/playbooks/api/v0/runs/{id}/timeline/{event_id}`

Remove a timeline event from the playbook run

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run whose timeline event will be modified. |
| `event_id` | `string` | `path` | Yes | ID of the timeline event to be deleted |

### Responses

#### 204 - Item successfully deleted.

#### 400 - 

#### 500 - 

