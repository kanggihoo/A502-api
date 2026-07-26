# 04-Patch a role [PUT]

`PUT /api/v4/roles/{role_id}/patch`

Partially update a role by providing only the fields you want to update. Omitted fields will not be updated. The fields that can be updated are defined in the request body, all other provided fields will be ignored.

##### Permissions
Must have `sysconsole_write_user_management_permissions` or `manage_system` permission. When updating the role of a system admin, the `manage_system` permission is mandatory.

__Minimum server version__: 4.9


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `role_id` | `string` | `path` | Yes | Role GUID |

### Request Body (application/json)

```json
{
  "permissions": [
    string
  ], // The permissions the role should grant.
}
```
### Responses

#### 200 - Role patch successful

Schema (application/json):
```json
{
  "id": string, // The unique identifier of the role.
  "name": string, // The unique name of the role, used when assigning roles to users/groups in contexts.
  "display_name": string, // The human readable name for the role.
  "description": string, // A human readable description of the role.
  "permissions": [
    string
  ], // A list of the unique names of the permissions this role grants.
  "scheme_managed": boolean, // indicates if this role is managed by a scheme (true), or is a custom stand-alone role (false).
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

