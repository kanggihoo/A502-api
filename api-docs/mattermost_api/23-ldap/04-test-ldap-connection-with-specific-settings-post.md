# 04-Test LDAP connection with specific settings [POST]

`POST /api/v4/ldap/test_connection`

Test the LDAP connection using the provided settings without modifying the current server configuration.
##### Permissions
Must have `sysconsole_read_authentication_ldap` or `manage_system` permission.


### Request Body (application/json)

```json
{
  "Enable": boolean,
  "EnableSync": boolean,
  "LdapServer": string,
  "LdapPort": integer,
  "ConnectionSecurity": string,
  "BaseDN": string,
  "BindUsername": string,
  "BindPassword": string,
  "MaximumLoginAttempts": integer,
  "UserFilter": string,
  "GroupFilter": string,
  "GuestFilter": string,
  "EnableAdminFilter": boolean,
  "AdminFilter": string,
  "GroupDisplayNameAttribute": string,
  "GroupIdAttribute": string,
  "FirstNameAttribute": string,
  "LastNameAttribute": string,
  "EmailAttribute": string,
  "UsernameAttribute": string,
  "NicknameAttribute": string,
  "IdAttribute": string,
  "PositionAttribute": string,
  "LoginIdAttribute": string,
  "PictureAttribute": string,
  "SyncIntervalMinutes": integer,
  "SkipCertificateVerification": boolean,
  "PublicCertificateFile": string,
  "PrivateKeyFile": string,
  "QueryTimeout": integer,
  "MaxPageSize": integer,
  "LoginFieldName": string,
  "LoginButtonColor": string,
  "LoginButtonBorderColor": string,
  "LoginButtonTextColor": string,
}
```
### Responses

#### 200 - LDAP connection test successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

