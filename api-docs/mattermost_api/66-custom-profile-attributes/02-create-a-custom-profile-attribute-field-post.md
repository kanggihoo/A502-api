# 02-Create a Custom Profile Attribute field [POST]

`POST /api/v4/custom_profile_attributes/fields`

Create a new Custom Profile Attribute field on the system.

__Minimum server version__: 10.5

##### Permissions
Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "name": string (required), // The internal identifier for this attribute. Must match `^[A-Za-z_][A-Za-z0-9_]*$` and must not be a CEL reserved word (true, false, null, in, as, break, const, continue, else, for, function, if, import, let, loop, package, namespace, return, var, void, while). This name is used in ABAC policy expressions as `user.attributes.<name>`. 
  "type": string (required),
  "attrs": {
    "visibility": enum("hidden" | "when_set" | "always"), // Visibility of the attribute
    "sort_order": number, // Sort order for displaying this attribute
    "options": [
      {
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
    "display_name": string, // Human-readable label shown in the UI. Defaults to the field `name` when omitted or empty. Maximum 255 characters. 
  },
}
```
### Responses

#### 201 - Custom Profile Attribute field creation successful

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

#### 422 - Validation error. Returned when `name` does not match the required identifier pattern, is a CEL reserved word, or when `attrs.display_name` exceeds 255 characters.


Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

