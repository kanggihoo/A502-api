# 05-Login with Microsoft Intune MAM [POST]

`POST /oauth/intune`

Authenticate a mobile user using a Microsoft Entra ID (Azure AD) access token for Intune Mobile Application Management (MAM) protected apps.

This endpoint enables authentication for mobile apps protected by Microsoft Intune MAM policies. The access token is obtained via the Microsoft Authentication Library (MSAL) and validated against the configured Azure AD tenant and Intune MAM app registration.

**Authentication Flow:**
1. Mobile app acquires an Entra ID access token via MSAL with the Intune MAM scope
2. Token is sent to this endpoint for validation
3. Server validates the token signature, claims, and tenant configuration
4. User is authenticated or created based on the token claims
5. Session token is returned for subsequent API requests

**User Provisioning:**
- **Office365 AuthService**: Users are automatically created on first login using the `oid` (Azure AD object ID) claim as the unique identifier
- **SAML AuthService**: Users must first login via web/desktop to establish their account with the `oid` (Azure AD object ID) as AuthData. Intune MAM  always uses objectId for SAML users. For Entra ID Domain Services LDAP sync, configure LdapSettings.IdAttribute to `msDS-aadObjectId` to ensure consistency.

**Error Handling:**
This endpoint returns specific HTTP status codes to help mobile apps handle different error scenarios:
- `428 Precondition Required`: SAML user needs to login via web/desktop first
- `403 Forbidden`: Configuration issues or bot accounts
- `409 Conflict`: User account is deactivated
- `401 Unauthorized`: Token has expired
- `400 Bad Request`: Invalid token format, claims, or configuration

##### Permissions

No permission required. Authentication is performed via the Entra ID access token.

##### Enterprise Feature

Requires Mattermost Enterprise Advanced license and proper Intune MAM configuration (tenant ID, client ID, and auth service).


### Request Body (application/json)

```json
{
  "access_token": string (required), // Microsoft Entra ID access token obtained via MSAL (Microsoft Authentication Library). This token must be scoped to the Intune MAM app registration and will be validated against the configured tenant.
  "device_id": string, // Optional mobile device identifier used for push notifications. If provided, the device will be registered for receiving push notifications.
  "voip_device_id": string, // Optional VoIP push token. Same prefix shape as device_id. When provided, enables ring-style call push notifications.
}
```
### Responses

#### 200 - User authentication successful

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

#### 400 - Bad request - Invalid token format, signature, claims, or configuration. Common causes include: invalid JSON body, missing access_token, malformed JWT, invalid token issuer/audience/tenant, missing required claims (oid, email), or empty auth data after extraction.


Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 401 - Unauthorized - The Entra ID access token has expired

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 403 - Forbidden - Access denied. Common causes include: Intune MAM not properly configured or enabled, or user is a bot account (bots cannot use Intune login).


Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 409 - Conflict - User account has been deactivated (DeleteAt != 0)

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 428 - Precondition Required - SAML user account not found. The user must first login via web or desktop application to establish their Mattermost account with objectId as AuthData before using mobile Intune MAM authentication. For Entra ID Domain Services LDAP sync, ensure SamlSettings.IdAttribute references the objectidentifier claim and LdapSettings.IdAttribute is set to 'msDS-aadObjectId'.


Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 500 - Internal Server Error - Server-side error. Common causes include: failed to initialize JWKS (JSON Web Key Set) from Microsoft's OpenID configuration, or failed to create user session.


Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 501 - Not Implemented - Intune MAM feature is not available. This occurs when running Mattermost Team Edition or when enterprise features are not loaded.


Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

