# 11-Unlink a channel from a group [DELETE]

`DELETE /api/v4/groups/{group_id}/channels/{channel_id}/link`

Delete a link between a channel and a group.

##### Permissions
Requires `manage_private_channel_members` (private channel) or
`manage_public_channel_members` (public channel) on the target channel.
If unlinking would leave the group with no remaining linkage in that channel's team context (last/only linkage for that team), also
requires `invite_user` on the team, or `sysconsole_write_user_management_groups`.
If the group has `allow_reference` disabled, also requires `sysconsole_read_user_management_groups`.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |
| `channel_id` | `string` | `path` | Yes | Channel GUID. |

### Responses

#### 200 - Channel unlinked from group

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

