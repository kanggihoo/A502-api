# 01-List playbook conditions [GET]

`GET /plugins/playbooks/api/v0/playbooks/{id}/conditions`

Retrieve a paged list of conditions for a playbook.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook to retrieve conditions from. |
| `page` | `integer` | `query` | No | Zero-based index of the page to request. |
| `per_page` | `integer` | `query` | No | Number of conditions to return per page. |

### Responses

#### 200 - A paged list of playbook conditions.

Schema (application/json):
```json
{
  "total_count": integer, // The total number of conditions in the list, regardless of paging.
  "page_count": integer, // The total number of pages. This depends on the total number of conditions and the per_page parameter.
  "has_more": boolean, // A boolean describing whether there are more pages after the currently returned.
  "items": [
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
  ], // The conditions in this page.
}
```

#### 403 - 

#### 500 - 

