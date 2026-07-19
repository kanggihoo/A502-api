# 08-Link a team to a group [POST]

`POST /api/v4/groups/{group_id}/teams/{team_id}/link`

Link a team to a group.

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

#### 201 - Team linked to group

Schema (application/json):
```json
{
  "team_id": string,
  "group_id": string,
  "auto_add": boolean,
  "create_at": integer,
  "delete_at": integer,
  "update_at": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

