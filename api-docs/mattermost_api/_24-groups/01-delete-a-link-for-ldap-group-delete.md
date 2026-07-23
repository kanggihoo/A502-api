# 01-Delete a link for LDAP group [DELETE]

`DELETE /api/v4/ldap/groups/{remote_id}/link`

##### Permissions
Must have `manage_system` permission.
__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `remote_id` | `string` | `path` | Yes | Group GUID |

### Responses

#### 200 - Successfully deleted ldap group link

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

