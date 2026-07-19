# 08-Get property values for the system [GET]

`GET /api/v4/properties/groups/{group_name}/system/values`

Get all property values attached to the Mattermost instance itself within a group. System-scoped values are readable by any authenticated user. This endpoint is the dedicated route for `system` object type; the `{object_type}/values/{target_id}` route returns 400 for `system`.

**Delta sync via `since`:** When `since > 0`, the endpoint returns only rows whose `update_at` is greater than the cutoff, *including* tombstones.

**Cursor key must match the active ordering:** in delta mode (`since > 0`) the endpoint orders by `update_at` and pagination requires `cursor_update_at`; otherwise it orders by `create_at` and pagination requires `cursor_create_at`.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_name` | `string` | `path` | Yes | The name of the property group |
| `since` | `integer` | `query` | No | Unix timestamp in milliseconds. When greater than 0, returns values with `update_at` greater than or equal to this value, including tombstones.<br> |
| `cursor_id` | `string` | `query` | No | The ID of the last property value from the previous page, for cursor-based pagination. |
| `cursor_create_at` | `integer` | `query` | No | The `create_at` timestamp of the last property value from the previous page. Required alongside `cursor_id` when `since` is absent. Mutually exclusive with `cursor_update_at`.<br> |
| `cursor_update_at` | `integer` | `query` | No | The `update_at` timestamp of the last property value from the previous page. Required alongside `cursor_id` when `since` is present. Mutually exclusive with `cursor_create_at`.<br> |
| `per_page` | `integer` | `query` | No | The number of property values per page. |

### Responses

#### 200 - System property values retrieval successful

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

