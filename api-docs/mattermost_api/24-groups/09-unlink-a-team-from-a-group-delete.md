# 09-Unlink a team from a group [DELETE]

`DELETE /api/v4/groups/{group_id}/teams/{team_id}/link`

Delete a link between a team and a group.

##### Permissions
Requires `invite_user` on the target team, or `sysconsole_write_user_management_groups`.
If the group has `allow_reference` disabled, also requires `sysconsole_read_user_management_groups`.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |
| `team_id` | `string` | `path` | Yes | Team GUID. |

### Responses

#### 200 - Team unlinked from group

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

