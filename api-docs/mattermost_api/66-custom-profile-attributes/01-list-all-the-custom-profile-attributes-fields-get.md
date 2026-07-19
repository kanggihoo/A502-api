# 01-List all the Custom Profile Attributes fields [GET]

`GET /api/v4/custom_profile_attributes/fields`

List all the Custom Profile Attributes fields.

__Minimum server version__: 10.5

##### Permissions
Must be authenticated.


### Responses

#### 200 - Custom Profile Attributes fetch successful. Result may be empty.

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

#### 401 - 

