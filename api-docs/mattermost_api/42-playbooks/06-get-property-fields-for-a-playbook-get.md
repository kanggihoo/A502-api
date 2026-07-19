# 06-Get property fields for a playbook [GET]

`GET /plugins/playbooks/api/v0/playbooks/{id}/property_fields`

Get property fields for a playbook

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook to retrieve property fields from. |
| `updated_since` | `integer` | `query` | No | Filter results to only include property fields updated after this timestamp (Unix time in milliseconds). |

### Responses

#### 200 - List of property fields for the playbook.

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

#### 500 - 

