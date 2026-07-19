# 01-Migrate user accounts authentication type to SAML. [POST]

`POST /api/v4/users/migrate_auth/saml`

Migrates accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to SAML.
__Minimum server version__: 5.28
##### Permissions
Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "from": string (required), // The current authentication type for the matched users.
  "matches": {} (required), // Users map.
  "auto": boolean (required),
}
```
### Responses

#### 200 - Successfully migrated authentication type to SAML.

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

