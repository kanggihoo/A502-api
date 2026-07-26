# 07-Restore a previously deleted group. [POST]

`POST /api/v4/groups/{group_id}/restore`

Restores a previously deleted custom group, allowing it to be used normally.
May not be used with LDAP groups.
##### Permissions Must have `restore_custom_group` permission for the given group.
__Minimum server version__: 7.7


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |

### Responses

#### 200 - Group restored successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

