# 07-Link a LDAP group [POST]

`POST /api/v4/ldap/groups/{remote_id}/link`

##### Permissions
Must have `manage_system` permission.
__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `remote_id` | `string` | `path` | Yes | Group GUID |

### Responses

#### 201 - LDAP group successfully linked

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

