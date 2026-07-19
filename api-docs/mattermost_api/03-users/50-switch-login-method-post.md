# 50-Switch login method [POST]

`POST /api/v4/users/login/switch`

Switch a user's login method from using email to OAuth2/SAML/LDAP or back to email. When switching to OAuth2/SAML, account switching is not complete until the user follows the returned link and completes any steps on the OAuth2/SAML service provider.

To switch from email to OAuth2/SAML, specify `current_service`, `new_service`, `email` and `password`.

To switch from OAuth2/SAML to email, specify `current_service`, `new_service`, `email` and `new_password`.

To switch from email to LDAP/AD, specify `current_service`, `new_service`, `email`, `password`, `ldap_ip` and `new_password` (this is the user's LDAP password).

To switch from LDAP/AD to email, specify `current_service`, `new_service`, `ldap_ip`, `password` (this is the user's LDAP password), `email`  and `new_password`.

Additionally, specify `mfa_code` when trying to switch an account on LDAP/AD or email that has MFA activated.

##### Permissions
No current authentication required except when switching from OAuth2/SAML to email.


### Request Body (application/json)

```json
{
  "current_service": string (required), // The service the user currently uses to login
  "new_service": string (required), // The service the user will use to login
  "email": string, // The email of the user
  "password": string, // The password used with the current service
  "mfa_code": string, // The MFA code of the current service
  "ldap_id": string, // The LDAP/AD id of the user
}
```
### Responses

#### 200 - Login method switch or request successful

Schema (application/json):
```json
{
  "follow_link": string, // The link for the user to follow to login or to complete the account switching when the current service is OAuth2/SAML
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

