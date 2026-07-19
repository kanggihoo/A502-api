# 08-Update a property field for a playbook [PUT]

`PUT /plugins/playbooks/api/v0/playbooks/{id}/property_fields/{field_id}`

Update a property field for a playbook

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook containing the property field. |
| `field_id` | `string` | `path` | Yes | ID of the property field to update. |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the property field.
  "type": enum("text" | "select" | "multiselect") (required), // The type of the property field.
  "attrs": {
    "visibility": enum("hidden" | "when_set" | "always"), // When to show this field.
    "sortOrder": number, // Display order of the field.
    "options": [
      {
        "id": string, // Option ID (generated if not provided).
        "name": string (required), // Display name of the option.
        "color": string, // Color associated with the option.
      }
    ], // Available options for select/multiselect fields.
    "parentID": string, // Parent field ID for hierarchical fields.
  }, // Additional attributes for the property field.
}
```
### Responses

#### 200 - Property field updated successfully.

Schema (application/json):
```json
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
```

#### 400 - 

#### 403 - 

#### 500 - 

