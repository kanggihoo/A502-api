# 03-Get a role [GET]

`GET /api/v4/roles/name/{role_name}`

Get a role from the provided role name.

##### Permissions
Requires an active session but no other permissions.

__Minimum server version__: 4.9


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `role_name` | `string` | `path` | Yes | Role Name |

### Responses

#### 200 - Role retrieval successful

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

#### 401 - 

#### 404 - 

