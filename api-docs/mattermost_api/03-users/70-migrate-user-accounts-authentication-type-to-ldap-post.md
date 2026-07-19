# 70-Migrate user accounts authentication type to LDAP. [POST]

`POST /api/v4/users/migrate_auth/ldap`

Migrates accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to LDAP.
__Minimum server version__: 5.28
##### Permissions
Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "from": string (required), // The current authentication type for the matched users.
  "match_field": string (required), // Foreign user field name to match.
  "force": boolean (required),
}
```
### Responses

#### 200 - Successfully migrated authentication type to LDAP.

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

