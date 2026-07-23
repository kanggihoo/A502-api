# 10-Link a channel to a group [POST]

`POST /api/v4/groups/{group_id}/channels/{channel_id}/link`

Link a channel to a group.

##### Permissions
Requires `manage_private_channel_members` (private channel) or
`manage_public_channel_members` (public channel) on the target channel.
If this is the group's first linkage into the channel's team context, also
requires `invite_user` on the team, or `sysconsole_write_user_management_groups`.
If the group has `allow_reference` disabled, also requires `sysconsole_read_user_management_groups`.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |
| `channel_id` | `string` | `path` | Yes | Channel GUID. |

### Responses

#### 201 - Channel linked to group

Schema (application/json):
```json
{
  "channel_id": string,
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

