# 05-Test LDAP diagnostics with specific settings [POST]

`POST /api/v4/ldap/test_diagnostics`

Test LDAP diagnostics using the provided settings to validate configuration and see sample results without modifying the current server configuration. Use the `test` query parameter to specify which diagnostic to run.
##### Permissions
Must have `sysconsole_read_authentication_ldap` or `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `test` | `string` | `query` | Yes | Type of LDAP diagnostic test to run |

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

#### 200 - LDAP diagnostic test results

Schema (application/json):
```json
[
  {
    "test_name": string, // Name/type of the diagnostic test being performed
    "test_value": string, // The actual test value (filter string or attribute name)
    "total_count": integer, // Number of entries found by the filter
    "message": string, // Optional success/info message
    "error": string, // Optional error message if test failed
    "sample_results": [
      {
        "dn": string, // Distinguished Name
        "username": string, // Username
        "email": string, // Email
        "first_name": string, // First name
        "last_name": string, // Last name
        "id": string, // ID attribute
        "display_name": string, // Display name for groups
        "available_attributes": {}, // Map of all available LDAP attributes
      }
    ], // Array of sample LDAP entries found
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

