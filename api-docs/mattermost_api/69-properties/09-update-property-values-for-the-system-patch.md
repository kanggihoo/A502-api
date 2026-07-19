# 09-Update property values for the system [PATCH]

`PATCH /api/v4/properties/groups/{group_name}/system/values`

Update one or more property values attached to the Mattermost instance itself. Uses upsert semantics: creates the value if it doesn't exist, updates it if it does. Requires system administrator access. All field IDs must reference `system` object-type fields in the specified group; template field IDs are rejected with 400.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_name` | `string` | `path` | Yes | The name of the property group |

### Request Body (application/json)

```json
[
  {
    "field_id": string (required), // The ID of the property field
    "value": any (required), // The value to set for this property. Can be any JSON type.
  }
]
```
### Responses

#### 200 - System property values update successful

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

#### 401 - 

#### 403 - 

