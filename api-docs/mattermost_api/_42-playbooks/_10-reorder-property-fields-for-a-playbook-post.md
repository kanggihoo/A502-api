# 10-Reorder property fields for a playbook [POST]

`POST /plugins/playbooks/api/v0/playbooks/{id}/property_fields/reorder`

Reorder property fields for a playbook

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook. |

### Request Body (application/json)

```json
{
  "field_id": string (required), // ID of the property field to move.
  "target_position": integer (required), // Target position index (zero-based) where the field should be moved.
}
```
### Responses

#### 200 - Property fields reordered successfully.

Schema (application/json):
```json
[
  {
    "id": string, // A unique, 26 characters long, alphanumeric identifier for the property field.
    "type": enum("text" | "select" | "multiselect"), // The type of the property field.
    "name": string, // The name of the property field.
    "description": string, // The description of the property field.
    "create_at": integer, // The property field creation timestamp, formatted as the number of milliseconds since the Unix epoch.
    "update_at": integer, // The property field update timestamp, formatted as the number of milliseconds since the Unix epoch.
    "delete_at": integer, // The property field deletion timestamp, formatted as the number of milliseconds since the Unix epoch. It equals 0 if not deleted.
    "attrs": {}, // Additional attributes for the property field (options for select fields, visibility, etc.).
  }
]
```

#### 400 - 

#### 403 - 

#### 404 - 

#### 500 - 

