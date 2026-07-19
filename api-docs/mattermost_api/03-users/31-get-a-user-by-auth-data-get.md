# 31-Get a user by auth data [GET]

`GET /api/v4/users/auth_data`

Get a user by their external auth data identifier. The `value` is matched against what is stored in `Users.AuthData`, which for most identity providers is the identifier as the provider issues it.

The exception is Active Directory `objectGUID`: under `auth_service: ldap` it is stored as the LDAP filter hex-escape form (e.g. `\61\14\e1\d1\c5\35\18\4a\b6\60\d6\78\50\fd\0d\5d`), and under `auth_service: saml` it is stored as the standard Base64 of the same bytes (e.g. `YRTh0cU1GEq2YNZ4UP0NXQ==`). Use the form matching the user's current `AuthService`.

##### Permissions
Must be a system admin.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `value` | `string` | `query` | Yes | The user's AuthData as stored in `Users.AuthData`. Must be URL-encoded; in particular, Base64 `+` characters must be sent as `%2B` so they are not decoded as spaces.<br> |

### Responses

#### 200 - User retrieval successful

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

#### 401 - 

#### 403 - 

#### 404 - 

