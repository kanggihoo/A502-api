# 10-Get users [GET]

`GET /api/v4/users`

Get a page of a list of users. Based on query string parameters, select users from a team, channel, or select users not in a specific channel.
Since server version 4.0, some basic sorting is available using the `sort` query parameter. Sorting is currently only supported when selecting users on a team.
Some fields, like `email_verified` and `notify_props`, are only visible for the authorized user or if the authorized user has the `manage_system` permission.
##### Permissions
Requires an active session and (if specified) membership to the channel or team being selected from.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of users per page. |
| `in_team` | `string` | `query` | No | The ID of the team to get users for. |
| `not_in_team` | `string` | `query` | No | The ID of the team to exclude users for. Must not be used with "in_team" query parameter. |
| `in_channel` | `string` | `query` | No | The ID of the channel to get users for. |
| `not_in_channel` | `string` | `query` | No | The ID of the channel to exclude users for. Must be used with "in_channel" query parameter. |
| `in_group` | `string` | `query` | No | The ID of the group to get users for. Must have `manage_system` permission. |
| `group_constrained` | `boolean` | `query` | No | When used with `not_in_channel` or `not_in_team`, returns only the users that are allowed to join the channel or team based on its group constrains. |
| `abac_match_only` | `boolean` | `query` | No | When used with `not_in_channel`, restricts the result to users whose attributes satisfy the channel's Attribute-Based Access Control (ABAC) membership policy.<br><br>On private channels with an ABAC policy this filter is always applied regardless of this parameter (hard gate). On public channels with an advisory ABAC policy the full not_in_channel candidate list is returned by default; set this to `true` to fetch only the matching subset of candidates (for example to annotate recommended members in the invite UI).<br><br>__Minimum server version__: 11.8<br> |
| `without_team` | `boolean` | `query` | No | Whether or not to list users that are not on any team. This option takes precendence over `in_team`, `in_channel`, and `not_in_channel`. |
| `active` | `boolean` | `query` | No | Whether or not to list only users that are active. This option cannot be used along with the `inactive` option. |
| `inactive` | `boolean` | `query` | No | Whether or not to list only users that are deactivated. This option cannot be used along with the `active` option. |
| `role` | `string` | `query` | No | Returns users that have this role. |
| `sort` | `string` | `query` | No | Sort is only available in conjunction with certain options below. The paging parameter is also always available.<br><br>##### `in_team`<br>Can be "", "last_activity_at" or "create_at".<br>When left blank, sorting is done by username.<br>Note that when "last_activity_at" is specified, an additional "last_activity_at" field will be returned in the response packet.<br>__Minimum server version__: 4.0<br>##### `in_channel`<br>Can be "", "status".<br>When left blank, sorting is done by username. `status` will sort by User's current status (Online, Away, DND, Offline), then by Username.<br>__Minimum server version__: 4.7<br>##### `in_group`<br>Can be "", "display_name".<br>When left blank, sorting is done by username. `display_name` will sort alphabetically by user's display name.<br>__Minimum server version__: 7.7<br> |
| `roles` | `string` | `query` | No | Comma separated string used to filter users based on any of the specified system roles<br><br>Example: `?roles=system_admin,system_user` will return users that are either system admins or system users<br><br>__Minimum server version__: 5.26<br> |
| `channel_roles` | `string` | `query` | No | Comma separated string used to filter users based on any of the specified channel roles, can only be used in conjunction with `in_channel`<br><br>Example: `?in_channel=4eb6axxw7fg3je5iyasnfudc5y&channel_roles=channel_user` will return users that are only channel users and not admins or guests<br><br>__Minimum server version__: 5.26<br> |
| `team_roles` | `string` | `query` | No | Comma separated string used to filter users based on any of the specified team roles, can only be used in conjunction with `in_team`<br><br>Example: `?in_team=4eb6axxw7fg3je5iyasnfudc5y&team_roles=team_user` will return users that are only team users and not admins or guests<br><br>__Minimum server version__: 5.26<br> |

### Responses

#### 200 - User page retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a user was created
    "update_at": integer, // The time in milliseconds a user was last updated
    "delete_at": integer, // The time in milliseconds a user was deleted
    "username": string,
    "first_name": string,
    "last_name": string,
    "nickname": string,
    "email": string,
    "email_verified": boolean,
    "auth_service": string,
    "roles": string,
    "locale": string,
    "notify_props": {
      "email": string, // Set to "true" to enable email notifications, "false" to disable. Defaults to "true".
      "push": string, // Set to "all" to receive push notifications for all activity, "mention" for mentions and direct messages only, and "none" to disable. Defaults to "mention".
      "desktop": string, // Set to "all" to receive desktop notifications for all activity, "mention" for mentions and direct messages only, and "none" to disable. Defaults to "all".
      "desktop_sound": string, // Set to "true" to enable sound on desktop notifications, "false" to disable. Defaults to "true".
      "mention_keys": string, // A comma-separated list of words to count as mentions. Defaults to username and @username.
      "channel": string, // Set to "true" to enable channel-wide notifications (@channel, @all, etc.), "false" to disable. Defaults to "true".
      "first_name": string, // Set to "true" to enable mentions for first name. Defaults to "true" if a first name is set, "false" otherwise.
      "auto_responder_message": string, // The message sent to users when they are auto-responded to. Defaults to "".
      "push_threads": string, // Set to "all" to enable mobile push notifications for followed threads and "none" to disable. Defaults to "all".
      "comments": string, // Set to "any" to enable notifications for comments to any post you have replied to, "root" for comments on your posts, and "never" to disable. Only affects users with collapsed reply threads disabled. Defaults to "never".
      "desktop_threads": string, // Set to "all" to enable desktop notifications for followed threads and "none" to disable. Defaults to "all".
      "email_threads": string, // Set to "all" to enable email notifications for followed threads and "none" to disable. Defaults to "all".
    },
    "props": {},
    "last_password_update": integer,
    "last_picture_update": integer,
    "failed_attempts": integer,
    "mfa_active": boolean,
    "timezone": {
      "useAutomaticTimezone": string, // Set to "true" to use the browser/system timezone, "false" to set manually. Defaults to "true".
      "manualTimezone": string, // Value when setting manually the timezone, i.e. "Europe/Berlin".
      "automaticTimezone": string, // This value is set automatically when the "useAutomaticTimezone" is set to "true".
    },
    "terms_of_service_id": string, // ID of accepted terms of service, if any. This field is not present if empty.
    "terms_of_service_create_at": integer, // The time in milliseconds the user accepted the terms of service
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

