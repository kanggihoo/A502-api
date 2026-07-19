# 09-Create a user [POST]

`POST /api/v4/users`

Create a new user on the system. Password is required for email login. For other authentication types such as LDAP or SAML, auth_data and auth_service fields are required.
##### Permissions
No permission required for creating email/username accounts on an open server. Auth Token is required for other authentication types such as LDAP or SAML.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `t` | `string` | `query` | No | Token id from an email invitation |
| `iid` | `string` | `query` | No | Token id from an invitation link |

### Request Body (application/json)

```json
{
  "email": string (required),
  "username": string (required),
  "first_name": string,
  "last_name": string,
  "nickname": string,
  "position": string,
  "timezone": {
    "useAutomaticTimezone": string, // Set to "true" to use the browser/system timezone, "false" to set manually. Defaults to "true".
    "manualTimezone": string, // Value when setting manually the timezone, i.e. "Europe/Berlin".
    "automaticTimezone": string, // This value is set automatically when the "useAutomaticTimezone" is set to "true".
  },
  "auth_data": string, // Service-specific authentication data, such as email address.
  "auth_service": string, // The authentication service, one of "email", "gitlab", "ldap", "saml", "office365", "google", and "".
  "password": string, // The password used for email authentication.
  "locale": string,
  "props": {},
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
}
```
### Responses

#### 201 - User creation successful

Schema (application/json):
```json
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
```

#### 400 - 

#### 403 - 

