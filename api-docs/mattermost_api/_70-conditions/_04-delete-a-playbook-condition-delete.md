# 04-Delete a playbook condition [DELETE]

`DELETE /plugins/playbooks/api/v0/playbooks/{id}/conditions/{conditionID}`

Delete a condition from a playbook. Run conditions cannot be deleted as they are read-only snapshots.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook. |
| `conditionID` | `string` | `path` | Yes | ID of the condition to delete. |

### Responses

#### 204 - Condition successfully deleted.

#### 400 - 

#### 403 - 

#### 404 - 

#### 500 - 

