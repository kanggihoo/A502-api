# 03-Patch a Custom Profile Attribute field [PATCH]

`PATCH /api/v4/custom_profile_attributes/fields/{field_id}`

Partially update a Custom Profile Attribute field by providing
only the fields you want to update. Omitted fields will not be
updated. The fields that can be updated are defined in the
request body, all other provided fields will be ignored.

**Note:** Fields with `attrs.protected = true` cannot be
modified and will return an error.

__Minimum server version__: 10.5

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `field_id` | `string` | `path` | Yes | Custom Profile Attribute field GUID |

### Request Body (application/json)

```json
{
  "name": string, // New name for the attribute. When changed, must match `^[A-Za-z_][A-Za-z0-9_]*$` and must not be a CEL reserved word. Pre-existing fields with non-conforming names remain patchable on all other attributes; the validation only fires when `name` actually changes. 
  "type": string,
  "attrs": {
    "visibility": enum("hidden" | "when_set" | "always"), // Visibility of the attribute
    "sort_order": number, // Sort order for displaying this attribute
    "options": [
      {
        "id": string,
        "name": string,
        "color": string,
      }
    ], // Options for select/multiselect fields
    "value_type": enum("email" | "url" | "phone"), // Type of text value
    "ldap": string, // LDAP attribute for syncing
    "saml": string, // SAML attribute for syncing
    "protected": boolean, // If true, the field is read-only and cannot be modified.
    "source_plugin_id": string, // The ID of the plugin that created this field. This attribute cannot be changed.
    "access_mode": enum("" | "source_only" | "shared_only"), // Access mode of the field
    "display_name": string, // Human-readable label shown in the UI. Maximum 255 characters. 
  },
}
```
### Responses

#### 200 - Custom Profile Attribute field patch successful

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

#### 422 - Validation error. Returned when a `name` change does not match the required identifier pattern, is a CEL reserved word, or when `attrs.display_name` exceeds 255 characters.


Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

