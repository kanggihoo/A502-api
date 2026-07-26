# 01-Create a property field [POST]

`POST /api/v4/properties/groups/{group_name}/{object_type}/fields`

Create a new property field for a specific group and object type.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_name` | `string` | `path` | Yes | The name of the property group |
| `object_type` | `string` | `path` | Yes | The type of object this property field applies to |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the property field
  "type": enum("text" | "select" | "multiselect" | "date" | "user" | "multiuser") (required), // The type of property field
  "attrs": {}, // Additional attributes for the property field
  "target_type": string (required), // The scope level of the property
  "target_id": string, // The ID of the target
  "permission_field": enum("none" | "sysadmin" | "member" | "admin"), // Permission level for editing the field definition. Only system admins can set this; ignored for non-admin users. 
  "permission_values": enum("none" | "sysadmin" | "member" | "admin"), // Permission level for setting values on objects. Only system admins can set this; ignored for non-admin users. 
  "permission_options": enum("none" | "sysadmin" | "member" | "admin"), // Permission level for managing options on select/multiselect fields. Only system admins can set this; ignored for non-admin users. 
  "linked_field_id": string, // The ID of a template field to link to. The source must be a template field in the same group, must not itself be linked, and must not be deleted. When set, the created field inherits the source's type, options, and security attributes; the `type` field in the request body is ignored. Can only be set at creation time. 
}
```
### Responses

#### 201 - Property field creation successful

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

#### 401 - 

#### 403 - 

#### 409 - A property field with the same name already exists at the same or a conflicting hierarchy level.


