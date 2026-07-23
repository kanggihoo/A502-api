# 18-Get group users [GET]

`GET /api/v4/groups/{group_id}/members`

Retrieve the list of users associated with a given group.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.11


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | Group GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of groups per page. |

### Responses

#### 200 - User list retrieval successful

Schema (application/json):
```json
{
  "members": [
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
  ],
  "total_member_count": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

