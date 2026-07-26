# 23-Set a property value for a playbook run [PUT]

`PUT /plugins/playbooks/api/v0/runs/{id}/property_fields/{field_id}/value`

Set a property value for a playbook run

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | ID of the playbook run to set property value for. |
| `field_id` | `string` | `path` | Yes | ID of the property field to set value for. |

### Request Body (application/json)

```json
{
  "value": string (required), // The JSON-encoded value to set for the property.
}
```
### Responses

#### 200 - Property value set successfully.

Schema (application/json):
```json
{
  "id": string, // A unique, 26 characters long, alphanumeric identifier for the property value.
  "field_id": string, // The identifier of the property field this value belongs to.
  "value": string, // The JSON-encoded value of the property.
  "create_at": integer, // The property value creation timestamp, formatted as the number of milliseconds since the Unix epoch.
  "update_at": integer, // The property value update timestamp, formatted as the number of milliseconds since the Unix epoch.
  "delete_at": integer, // The property value deletion timestamp, formatted as the number of milliseconds since the Unix epoch. It equals 0 if not deleted.
}
```

#### 400 - 

#### 403 - 

#### 500 - 

