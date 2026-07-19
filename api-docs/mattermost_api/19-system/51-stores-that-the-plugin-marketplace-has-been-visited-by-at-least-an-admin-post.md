# 51-Stores that the Plugin Marketplace has been visited by at least an admin. [POST]

`POST /api/v4/plugins/marketplace/first_admin_visit`

Stores the system-level status that specifies that at least an admin has visited the in-product Plugin Marketplace.
__Minimum server version: 5.33__
##### Permissions
Must have `manage_system` permissions.


### Request Body (application/json)

```json
{
  "name": string, // System property name
  "value": string, // System property value
}
```
### Responses

#### 200 - setting has been successfully set

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - 

#### 500 - 

