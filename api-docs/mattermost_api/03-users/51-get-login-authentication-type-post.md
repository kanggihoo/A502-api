# 51-Get login authentication type [POST]

`POST /api/v4/users/login/type`

Get the authentication service type (auth_service) for a user to determine how they should authenticate. This endpoint is typically used in the login flow to determine which authentication method to use.

For this version, the endpoint only returns a non-empty `auth_service` if the user has magic_link enabled. For all other authentication methods (email/password, OAuth, SAML, LDAP), an empty string is returned.
##### Permissions
No permission required


### Request Body (application/json)

```json
{
  "id": string, // The user ID (optional, can be used with login_id)
  "login_id": string, // The login ID (email, username, or unique identifier)
  "device_id": string, // The device ID for audit logging purposes
}
```
### Responses

#### 200 - Login type retrieved successfully

Schema (application/json):
```json
{
  "auth_service": string, // The authentication service type. Returns the actual service type if guest_magic_link is enabled (in which case a magic link is also sent to the user's email). Returns an empty string for all other authentication methods.
}
```

#### 400 - 

