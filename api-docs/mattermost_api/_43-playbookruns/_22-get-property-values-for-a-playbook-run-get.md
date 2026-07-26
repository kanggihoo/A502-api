# 22-Get property values for a playbook run [GET]

`GET /plugins/playbooks/api/v0/runs/{id}/property_values`

Get property values for a playbook run

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run to retrieve property values from. |
| `updated_since` | `integer` | `query` | No | Filter results to only include property values updated after this timestamp (Unix time in milliseconds). |

### Responses

#### 200 - List of property values for the playbook run.

Schema (application/json):
```json
[
  {
    "id": string, // A unique, 26 characters long, alphanumeric identifier for the property value.
    "field_id": string, // The identifier of the property field this value belongs to.
    "value": string, // The JSON-encoded value of the property.
    "create_at": integer, // The property value creation timestamp, formatted as the number of milliseconds since the Unix epoch.
    "update_at": integer, // The property value update timestamp, formatted as the number of milliseconds since the Unix epoch.
    "delete_at": integer, // The property value deletion timestamp, formatted as the number of milliseconds since the Unix epoch. It equals 0 if not deleted.
  }
]
```

#### 400 - 

#### 403 - 

#### 500 - 

