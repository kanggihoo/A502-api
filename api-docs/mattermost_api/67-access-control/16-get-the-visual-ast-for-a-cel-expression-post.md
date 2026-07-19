# 16-Get the visual AST for a CEL expression [POST]

`POST /api/v4/access_control_policies/cel/visual_ast`

Retrieves the visual AST for a CEL expression.
##### Permissions
Must have the `manage_system` permission.


### Request Body (application/json)

```json
{
  "expression": string, // The CEL expression to visualize.
  "channelId": string, // The channel ID to contextually test the expression against (required for channel admins).
}
```
### Responses

#### 200 - Visual AST retrieved successfully.

Schema (application/json):
```json
{
  "conditions": [
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
  ], // The visual AST for the CEL expression
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

