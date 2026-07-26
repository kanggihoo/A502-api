# 11-Get if the Plugin Marketplace has been visited by at least an admin. [GET]

`GET /api/v4/plugins/marketplace/first_admin_visit`

Retrieves the status that specifies that at least one System Admin has visited the in-product Plugin Marketplace.
__Minimum server version: 5.33__
##### Permissions
Must have `manage_system` permissions.


### Responses

#### 200 - Retrieves the system-level status

Schema (application/json):
```json
{
  "name": string, // System property name
  "value": string, // System property value
}
```

#### 403 - 

#### 500 - 

