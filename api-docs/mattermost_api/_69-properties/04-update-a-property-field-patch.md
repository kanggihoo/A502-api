# 04-Update a property field [PATCH]

`PATCH /api/v4/properties/groups/{group_name}/{object_type}/fields/{field_id}`

Partially update a property field by providing only the fields you want to update. Omitted fields will not be updated. The `attrs` object uses merge semantics: only the keys present in the patch are updated; omitted keys are preserved. Setting a key to `null` removes it from attrs.

**Immutable fields:** `target_type`, `target_id`, and `object_type` cannot be changed after creation and are ignored if included in the patch.

**Linked fields:** Fields with a `linked_field_id` cannot have their `type` or `attrs.options` modified (returns 400). The `linked_field_id` can only be cleared (set to empty string `""`) to unlink the field; it cannot be changed to a different value. For non-linked fields, `linked_field_id` cannot be set to a new value (linking is only allowed at creation time).

**Propagation:** When a template field's options are updated, the changes propagate atomically to all fields that link to it.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_name` | `string` | `path` | Yes | The name of the property group |
| `object_type` | `string` | `path` | Yes | The type of object this property field applies to |
| `field_id` | `string` | `path` | Yes | Property field ID |

### Request Body (application/json)

```json
{
  "name": string,
  "type": string,
  "attrs": {},
  "linked_field_id": string, // Set to empty string to unlink a linked field. Cannot be set to a new value on an existing field; linking is only allowed at creation time. 
}
```
### Responses

#### 200 - Property field update successful

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

#### 404 - 

#### 409 - Name conflict with an existing field, or cannot change type of a field that has active linked dependents.


