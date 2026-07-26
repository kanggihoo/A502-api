# 02-Create a playbook condition [POST]

`POST /plugins/playbooks/api/v0/playbooks/{id}/conditions`

Create a new condition for a playbook.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook to create a condition for. |

### Request Body (application/json)

```json
{
  "id": string, // A unique, 26 characters long, alphanumeric identifier for the condition.
  "condition_expr": {
    "and": [
      Ref(ConditionExprV1) [recursive]
    ], // Logical AND operation. All conditions in the array must be true.
    "or": [
      Ref(ConditionExprV1) [recursive]
    ], // Logical OR operation. At least one condition in the array must be true.
    "is": {
      "field_id": string (required), // The identifier of the field to compare against.
      "value": any (required), // The value to compare with. Format depends on the field type. Stored as JSON.
    },
    "isNot": {
      "field_id": string (required), // The identifier of the field to compare against.
      "value": any (required), // The value to compare with. Format depends on the field type. Stored as JSON.
    },
  } (required),
  "version": integer (required), // Version number of the condition expression format. Currently only version 1 is supported.
  "playbook_id": string, // The identifier of the playbook this condition belongs to.
  "run_id": string, // If this is a run condition (read-only snapshot), the identifier of the run. Empty for playbook conditions.
  "create_at": integer, // The condition creation timestamp, formatted as the number of milliseconds since the Unix epoch.
  "update_at": integer, // The condition update timestamp, formatted as the number of milliseconds since the Unix epoch.
}
```
### Responses

#### 201 - Created condition.

Schema (application/json):
```json
{
  "id": string, // A unique, 26 characters long, alphanumeric identifier for the condition.
  "condition_expr": {
    "and": [
      Ref(ConditionExprV1) [recursive]
    ], // Logical AND operation. All conditions in the array must be true.
    "or": [
      Ref(ConditionExprV1) [recursive]
    ], // Logical OR operation. At least one condition in the array must be true.
    "is": {
      "field_id": string (required), // The identifier of the field to compare against.
      "value": any (required), // The value to compare with. Format depends on the field type. Stored as JSON.
    },
    "isNot": {
      "field_id": string (required), // The identifier of the field to compare against.
      "value": any (required), // The value to compare with. Format depends on the field type. Stored as JSON.
    },
  } (required),
  "version": integer (required), // Version number of the condition expression format. Currently only version 1 is supported.
  "playbook_id": string, // The identifier of the playbook this condition belongs to.
  "run_id": string, // If this is a run condition (read-only snapshot), the identifier of the run. Empty for playbook conditions.
  "create_at": integer, // The condition creation timestamp, formatted as the number of milliseconds since the Unix epoch.
  "update_at": integer, // The condition update timestamp, formatted as the number of milliseconds since the Unix epoch.
}
```

#### 400 - 

#### 403 - 

#### 500 - 

