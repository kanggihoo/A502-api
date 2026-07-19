# 15-Search users [POST]

`POST /api/v4/users/search`

Get a list of users based on search criteria provided in the request body. Searches are typically done against username, full name, nickname and email unless otherwise configured by the server.
##### Permissions
Requires an active session and `read_channel` and/or `view_team` permissions for any channels or teams specified in the request body.


### Request Body (application/json)

```json
{
  "term": string (required), // The term to match against username, full name, nickname and email
  "team_id": string, // If provided, only search users on this team
  "not_in_team_id": string, // If provided, only search users not on this team
  "in_channel_id": string, // If provided, only search users in this channel
  "not_in_channel_id": string, // If provided, only search users not in this channel. Must specifiy `team_id` when using this option
  "in_group_id": string, // If provided, only search users in this group. Must have `manage_system` permission.
  "group_constrained": boolean, // When used with `not_in_channel_id` or `not_in_team_id`, returns only the users that are allowed to join the channel or team based on its group constrains.
  "allow_inactive": boolean, // When `true`, include deactivated users in the results
  "without_team": boolean, // Set this to `true` if you would like to search for users that are not on a team. This option takes precendence over `team_id`, `in_channel_id`, and `not_in_channel_id`.
  "limit": integer, // The maximum number of users to return in the results  __Available as of server version 5.6. Defaults to `100` if not provided or on an earlier server version.__ 
}
```
### Responses

#### 200 - User list retrieval successful

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

