# 03-Search property fields across multiple object types [POST]

`POST /api/v4/properties/groups/{group_name}/fields/search`

Returns matching fields across every requested object type in one response. The request body is a `PropertyFieldSearch` object whose `object_types` field lists the object types to include.
Scope, `since`, cursor, and permission semantics are identical to the get property fields endpoint, including the system-object collapse: when `object_types` is exactly `["system"]`, any scope or target params in the body are ignored and the endpoint resolves to `target_type=system`. Any other combination without an explicit scope returns 400.
Requesting a single value in `object_types` is equivalent to calling the singular endpoint and is supported for client uniformity.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_name` | `string` | `path` | Yes | The name of the property group |

### Request Body (application/json)

```json
{
  "object_types": [
    enum("post" | "channel" | "user" | "template" | "system")
  ] (required), // One or more object types to include in the response. At least one value is required; unknown values return 400. 
  "channel_id": string, // Hierarchical scope. When set, the response includes system-level rows, team-level rows for the channel's team, and channel-level rows for this channel across every requested `object_types`. Mutually exclusive with `target_type`/`target_id`. Requires `read_channel` on the channel. 
  "team_id": string, // Hierarchical scope. When set without `channel_id`, the response includes system-level and team-level rows for this team across every requested `object_types`. When `channel_id` is also set, this value is ignored — the channel's team is resolved server-side and used instead. Mutually exclusive with `target_type`/`target_id`. Requires `view_team` on the team. 
  "target_type": enum("system" | "team" | "channel"), // Single-target scope. Mutually exclusive with `channel_id` and `team_id`. Required if no hierarchical scope is given, except when `object_types` is exactly `["system"]` — in that case any scope or target params are ignored and the endpoint resolves to `target_type=system`. 
  "target_id": string, // Single-target scope. Required when `target_type` is `channel` or `team`. Mutually exclusive with `channel_id` and `team_id`. 
  "since": integer, // Unix timestamp in milliseconds. When greater than 0, returns fields with `update_at` greater than or equal to this value, including tombstones. 
  "cursor_id": string, // The ID of the last property field from the previous page, for cursor-based pagination.
  "cursor_create_at": integer, // The `create_at` timestamp of the last property field from the previous page. Required alongside `cursor_id` when `since` is absent. Mutually exclusive with `cursor_update_at`. 
  "cursor_update_at": integer, // The `update_at` timestamp of the last property field from the previous page. Required alongside `cursor_id` when `since` is present. Mutually exclusive with `cursor_create_at`. 
  "per_page": integer, // The number of property fields per page.
}
```
### Responses

#### 200 - Property fields retrieval successful

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

#### 401 - 

#### 403 - 

#### 404 - 

