# 07-Update property values for a target [PATCH]

`PATCH /api/v4/properties/groups/{group_name}/{object_type}/values/{target_id}`

Update one or more property values for a specific target within a group. Uses upsert semantics: creates the value if it doesn't exist, updates it if it does. All field IDs must belong to the specified group. The `template` object type cannot have values and will return 400. The `system` object type must use the dedicated `/api/v4/properties/groups/{group_name}/system/values` endpoint and will return 400 on this route.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_name` | `string` | `path` | Yes | The name of the property group |
| `object_type` | `string` | `path` | Yes | The type of object |
| `target_id` | `string` | `path` | Yes | The ID of the target object |

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

#### 200 - Property values update successful

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

